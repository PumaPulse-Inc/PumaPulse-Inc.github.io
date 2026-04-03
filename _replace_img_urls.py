import json, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('_img_urls.json', 'r') as f:
    url_map = json.load(f)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace each local img reference with Cloudinary URL
for filename, cdn_url in url_map.items():
    # Match: img/filename in src, href, url()
    local = f'img/{filename}'
    html = html.replace(local, cdn_url)
    print(f"Replaced: {local} -> {cdn_url[:70]}")

# Also replace Background.png (capital B variant)
if 'background.png' in url_map:
    html = html.replace("img/Background.png", url_map['background.png'])
    print(f"Replaced: img/Background.png -> {url_map['background.png'][:70]}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Verify no local img/ refs remain
remaining = re.findall(r'["\']img/[^"\']+["\']', html)
print(f"\nLocal img/ refs remaining: {len(remaining)}")
for r in remaining:
    print(f"  {r}")
