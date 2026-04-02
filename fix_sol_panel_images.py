import re

with open('index.html', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8', errors='replace')

# Find all sol-panel sections and their images
panels = re.findall(r'id="sol-(\w+)".*?(?=id="sol-|\Z)', content, re.DOTALL)
for p in panels:
    imgs = re.findall(r'sol-card-img.*?src="([^"]+)"', p, re.DOTALL)
    name = p[:20]
    print(name[:15], ':', [i.split('/')[-1][:30] for i in imgs])
