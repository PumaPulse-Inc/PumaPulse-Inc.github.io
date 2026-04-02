import re

# ── CAREERS: remove CEO/CTO reviewer block ──────────────────────────────────
with open('careers/index.html', 'rb') as f:
    raw = f.read()
c = raw.decode('utf-8', errors='replace')

# Remove the two reviewer rows (CEO + CTO with photos)
c = re.sub(
    r'<div style="display:flex;flex-direction:column;gap:16px;margin-bottom:28px;">.*?</div>\s*</div>',
    '', c, count=1, flags=re.DOTALL
)

# Also remove the duplicate img tags that appear twice (artifact from earlier)
c = re.sub(r'(<img [^>]+>)\s*\1', r'\1', c)

with open('careers/index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed careers CEO/CTO block')


# ── PORTFOLIO: replace client photos with initial avatars ────────────────────
COLORS = ['#10b981','#3b82f6','#a78bfa','#f59e0b','#ef4444','#06b6d4']

# Map: alt text -> initials, color index
CLIENTS = {
    'Mario Butler':      ('MB', 0),
    'Steven Kim':        ('SK', 1),
    'Kooban Naidoo':     ('KN', 2),
    'Chandravadan Raut': ('CR', 3),
    'Manoj Kumaran':     ('MK', 4),
    'Client':            ('SC', 5),
}

with open('portfolio/index.html', 'rb') as f:
    raw = f.read()
p = raw.decode('utf-8', errors='replace')

# Replace each client img with an initial avatar div
for name, (initials, ci) in CLIENTS.items():
    color = COLORS[ci]
    avatar = (
        f'<div style="width:44px;height:44px;border-radius:50%;'
        f'background:{color};display:flex;align-items:center;'
        f'justify-content:center;font-size:0.85rem;font-weight:700;'
        f'color:#fff;flex-shrink:0;">{initials}</div>'
    )
    # Match the img tag for this client
    p = re.sub(
        r'<img src="[^"]*" alt="' + re.escape(name) + r'"[^>]*>',
        avatar, p
    )

with open('portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(p)
print('Fixed portfolio client avatars')


# ── CAREERS apply form: also fix duplicate img tags ─────────────────────────
print('Done!')
