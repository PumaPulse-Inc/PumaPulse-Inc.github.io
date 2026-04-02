import re
with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()
imgs = re.findall(r'src="(https?://[^"]+)"', content)
for i, img in enumerate(imgs):
    print(f'{i}: {img[:120]}')
