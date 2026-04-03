import urllib.request, urllib.parse, hashlib, hmac, time, json, os, sys, io, base64, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

CLOUD = 'dtvnifa3t'
API_KEY = '995725632836223'
API_SECRET = 'XjBtx9ZpNoXYy5cM8rGeKOwPaiQ'

IMG_DIR = 'img'
images = ['logo.png','icon.png','user1.jpg','user2.jpg','user3.jpg','user4.jpg',
          '1.png','2.png','3.png','4.png','background.png']

def upload(filepath, public_id):
    timestamp = str(int(time.time()))
    # Build signature
    params = f"public_id={public_id}&timestamp={timestamp}"
    sig = hashlib.sha1((params + API_SECRET).encode()).hexdigest()
    
    with open(filepath, 'rb') as f:
        file_data = f.read()
    
    b64 = base64.b64encode(file_data).decode()
    ext = os.path.splitext(filepath)[1].lower().replace('.','')
    if ext == 'jpg': ext = 'jpeg'
    data_uri = f"data:image/{ext};base64,{b64}"
    
    post_data = urllib.parse.urlencode({
        'file': data_uri,
        'public_id': public_id,
        'timestamp': timestamp,
        'api_key': API_KEY,
        'signature': sig,
    }).encode()
    
    url = f"https://api.cloudinary.com/v1_1/{CLOUD}/image/upload"
    req = urllib.request.Request(url, data=post_data, method='POST')
    
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read())
            return result.get('secure_url', '')
    except Exception as e:
        return f"ERROR: {e}"

url_map = {}
for img in images:
    path = os.path.join(IMG_DIR, img)
    if not os.path.exists(path):
        print(f"SKIP (not found): {img}")
        continue
    pub_id = f"pumapulse/{os.path.splitext(img)[0]}"
    print(f"Uploading {img}...", end=' ', flush=True)
    url = upload(path, pub_id)
    url_map[img] = url
    print(url[:80] if url else 'FAILED')

print("\n=== URL MAP ===")
for k, v in url_map.items():
    print(f"{k}: {v}")

# Save map
with open('_img_urls.json', 'w') as f:
    json.dump(url_map, f, indent=2)
print("\nSaved to _img_urls.json")
