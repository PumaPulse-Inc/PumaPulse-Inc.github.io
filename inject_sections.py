import re

# Read source (UTF-16)
with open('index_full.html', 'rb') as f:
    raw = f.read()
src = raw.decode('utf-16', errors='replace')

# Read current index.html
with open('index.html', 'rb') as f:
    raw2 = f.read()
cur = raw2.decode('utf-8', errors='replace')

def extract_section(html, marker_start, marker_end=None):
    """Extract content between two markers"""
    start = html.find(marker_start)
    if start == -1:
        return None
    if marker_end:
        end = html.find(marker_end, start)
        if end == -1:
            return None
        return html[start:end + len(marker_end)]
    # Find the closing </section>
    depth = 0
    i = start
    while i < len(html):
        if html[i:i+8] == '<section':
            depth += 1
        elif html[i:i+10] == '</section>':
            depth -= 1
            if depth == 0:
                return html[start:i+10]
        i += 1
    return None

# Extract sections from source
sections_to_add = []

# Process section
proc = extract_section(src, '<!-- Process -->')
if not proc:
    proc = extract_section(src, '<section class="section">\n\n\n  <div class="container">\n\n\n    <div class="text-center reveal">\n\n\n      <span class="eyebrow">How We Work</span>')
if proc:
    sections_to_add.append(('process', proc))
    print('Found process section, length:', len(proc))

# Portfolio preview section
port = extract_section(src, '<!-- Portfolio -->')
if not port:
    # find by eyebrow
    idx = src.find('Our Work')
    if idx > -1:
        start = src.rfind('<section', 0, idx)
        port = extract_section(src[start:], '<section')
        if port:
            port = src[start:start+len(port)]
if port:
    sections_to_add.append(('portfolio', port))
    print('Found portfolio section, length:', len(port))

# Testimonials section
testi = extract_section(src, '<!-- Testimonials -->')
if not testi:
    idx = src.find('testi-card')
    if idx > -1:
        start = src.rfind('<section', 0, idx)
        end = src.find('</section>', idx) + 10
        testi = src[start:end]
if testi:
    sections_to_add.append(('testimonials', testi))
    print('Found testimonials section, length:', len(testi))

# Tech stack section
tech = extract_section(src, '<!-- Tech Stack -->')
if not tech:
    idx = src.find('tech-logo-grid')
    if idx > -1:
        start = src.rfind('<section', 0, idx)
        end = src.find('</section>', idx) + 10
        tech = src[start:end]
if tech:
    sections_to_add.append(('tech', tech))
    print('Found tech section, length:', len(tech))

# FAQ section
faq = extract_section(src, '<!-- FAQ -->')
if not faq:
    idx = src.find('faq-item')
    if idx > -1:
        start = src.rfind('<section', 0, idx)
        end = src.find('</section>', idx) + 10
        faq = src[start:end]

# Now inject into current index.html before the footer placeholder
inject_point = cur.find('<div id="footer-placeholder">')
if inject_point == -1:
    print('ERROR: footer placeholder not found')
else:
    insert = '\n'
    for name, section in sections_to_add:
        insert += f'\n<!-- {name.upper()} -->\n' + section + '\n'
    
    # Also add FAQ if not present
    if 'faq-item' not in cur and faq:
        insert += '\n<!-- FAQ -->\n' + faq + '\n'
    
    cur = cur[:inject_point] + insert + cur[inject_point:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(cur)
    print('Injected sections into index.html')
