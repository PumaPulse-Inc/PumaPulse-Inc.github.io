import re

# ── Fix careers apply section broken HTML ──
with open('careers/index.html', 'rb') as f:
    raw = f.read()
c = raw.decode('utf-8', errors='replace')

# Fix the broken apply section - remove stray closing div and fix structure
c = re.sub(
    r'(<p style="margin-bottom:28px;">Send us your application.*?rejections\.</p>)\s*\n\s*\n\s*</div>\s*\n',
    r'\1\n',
    c, flags=re.DOTALL
)

with open('careers/index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed careers')

# ── Fix contact page - replace — bullet with checkmark ──
with open('contact/index.html', 'rb') as f:
    raw = f.read()
c = raw.decode('utf-8', errors='replace')

# Replace the — bullet spans with proper checkmark SVG
c = c.replace(
    'font-size:0.62rem;font-weight:700;color:var(--accent);flex-shrink:0;">— </span>',
    'color:var(--accent);flex-shrink:0;"><svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" style="width:10px;height:10px"><path d="M1 6l3 3 7-7"/></svg></span>'
)

with open('contact/index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed contact')

# ── Fix portfolio breadcrumb paths ──
with open('portfolio/index.html', 'rb') as f:
    raw = f.read()
c = raw.decode('utf-8', errors='replace')

# Fix wrong relative links (contact/ -> ../contact/ etc)
c = c.replace('href="contact/"', 'href="../contact/"')
c = c.replace('href="about/"', 'href="../about/"')
c = c.replace('href="index/"', 'href="../"')

with open('portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed portfolio links')

# ── Fix careers breadcrumb ──
with open('careers/index.html', 'rb') as f:
    raw = f.read()
c = raw.decode('utf-8', errors='replace')
c = c.replace('href="index/"', 'href="../"')
with open('careers/index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed careers breadcrumb')

print('All done!')
