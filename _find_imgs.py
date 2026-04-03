import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all external image URLs
urls = set(re.findall(r'https://images\.unsplash\.com/[^\s\'")?]+', html))
urls2 = set(re.findall(r'https://images\.pexels\.com/[^\s\'")?]+', html))
all_urls = sorted(urls | urls2)

print(f"Found {len(all_urls)} unique external image URLs:\n")
for u in all_urls:
    print(u)
