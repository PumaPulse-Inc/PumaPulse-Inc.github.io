import re

with open('careers/index.html', 'rb') as f:
    raw = f.read()
c = raw.decode('utf-8', errors='replace')

# Remove the entire reviewer block - find from first reviewer div to closing div
# Pattern: the flex column containing the two reviewer rows
c = re.sub(
    r'<div style="display:flex;gap:12px;align-items:flex-start;">\s*<img[^>]*alt="CTO"[^>]*>\s*<div>.*?</div>\s*</div>',
    '', c, flags=re.DOTALL
)

# Also remove any leftover unsplash CTO photo
c = re.sub(r'<img[^>]*photo-1494790108377[^>]*>', '', c)

# Remove the outer wrapper div if now empty
c = re.sub(r'<div style="display:flex;flex-direction:column;gap:16px;margin-bottom:28px;">\s*</div>', '', c)

with open('careers/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

# Verify
with open('careers/index.html', 'rb') as f:
    raw2 = f.read()
t = raw2.decode('utf-8', errors='replace')
print('CTO present:', 'CTO' in t)
print('Nina Patel present:', 'Nina Patel' in t)
print('CTO photo present:', 'photo-1494790108377' in t)
print('Done!')
