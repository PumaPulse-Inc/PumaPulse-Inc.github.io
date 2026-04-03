import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = 'https://pumapulse-inc.github.io'

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all local img/ references with absolute GitHub Pages CDN URLs
# Match: src="img/...", url('img/...'), href="img/..."
html = re.sub(r'(src|href)="img/', rf'\1="{BASE}/img/', html)
html = re.sub(r"url\('img/", f"url('{BASE}/img/", html)
html = re.sub(r'url\("img/', f'url("{BASE}/img/', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Verify
matches = re.findall(r'(?:src|href|url\().*?img/', html)
local_remaining = [m for m in matches if BASE not in m and 'http' not in m]
print(f"Replaced. Local img/ refs remaining: {len(local_remaining)}")

# Show all img refs now
all_img = re.findall(r'(?:src|href)="([^"]*img/[^"]*)"', html)
for u in sorted(set(all_img)):
    print(u)
