import re
with open('index.html','rb') as f: raw=f.read()
t = raw.decode('utf-8', errors='replace')
sections = re.findall(r'class="eyebrow[^"]*">([^<]+)<', t)
print('Sections found:')
for s in sections: print(' -', s.strip())
print('Total chars:', len(t))
