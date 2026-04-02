import re

EM = '\u2014'

with open('about/index.html', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8', errors='replace')

# Fix replacement char (was em dash)
content = content.replace('\ufffd', EM)

# Fix title: "About PumaPulse —" Beyond Services" -> clean dash
content = content.replace('About PumaPulse ' + EM + '" Beyond Services', 'About PumaPulse - Beyond Services')

# Fix timeline "2016 —"" -> "2016 —"
content = re.sub(r'(\d{4})\s*' + EM + '"', r'\g<1> ' + EM, content)

# Remove entire Our Team section
content = re.sub(
    r'<section[^>]*>\s*<div class="container">\s*<div class="text-center reveal">\s*<span class="eyebrow">Our Team</span>.*?</section>',
    '', content, flags=re.DOTALL
)

with open('about/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
