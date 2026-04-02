import re

with open('index.html', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8', errors='replace')

# Fix 1: "Learn more ?" broken arrow - replace with clean arrow SVG
ARROW = ' <svg viewBox="0 0 14 14" fill="none" style="width:11px;height:11px;vertical-align:middle;margin-left:2px"><path d="M1 7h12M7 1l6 6-6 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
content = re.sub(r'Learn more\s*[?û›»→✓]', 'Learn more' + ARROW, content)
content = content.replace('Learn more ?', 'Learn more' + ARROW)

# Fix 2: Replace duplicate/generic images in sol-panel cards with unique ones
# Exchange panel
content = content.replace(
    'photos/844124/pexels-photo-844124.jpeg?auto=compress&cs=tinysrgb&w=500" alt="CEX',
    'photos/6801648/pexels-photo-6801648.jpeg?auto=compress&cs=tinysrgb&w=500" alt="CEX'
)
content = content.replace(
    'photos/7567443/pexels-photo-7567443.jpeg?auto=compress&cs=tinysrgb&w=500" alt="DEX',
    'photos/3184291/pexels-photo-3184291.jpeg?auto=compress&cs=tinysrgb&w=500" alt="DEX'
)
content = content.replace(
    'photos/6802042/pexels-photo-6802042.jpeg?auto=compress&cs=tinysrgb&w=500" alt="P2P',
    'photos/3943716/pexels-photo-3943716.jpeg?auto=compress&cs=tinysrgb&w=500" alt="P2P'
)
content = content.replace(
    'photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&w=500" alt="White',
    'photos/3184339/pexels-photo-3184339.jpeg?auto=compress&cs=tinysrgb&w=500" alt="White'
)
content = content.replace(
    'photos/6770610/pexels-photo-6770610.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Deriv',
    'photos/844124/pexels-photo-844124.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Deriv'
)

# Fix Hybrid Exchange image (laptop with blockchain logo - same as others)
content = content.replace(
    'photos/6770520/pexels-photo-6770520.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Hybrid',
    'photos/1181671/pexels-photo-1181671.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Hybrid'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
