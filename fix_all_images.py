import re, os

# Per-file image replacements: (file, old_fragment, new_fragment)
FIXES = [
    # ── PORTFOLIO ──
    # Cryptinum card - was same as hero live card
    ('portfolio/index.html',
     'photos/9577236/pexels-photo-9577236.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Cryptinum',
     'photos/844124/pexels-photo-844124.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Cryptinum'),
    # Apzor card - neobank/fintech
    ('portfolio/index.html',
     'photos/9577253/pexels-photo-9577253.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Apzor',
     'photos/3943716/pexels-photo-3943716.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Apzor'),
    # MetaStation card
    ('portfolio/index.html',
     'photos/9577240/pexels-photo-9577240.jpeg?auto=compress&cs=tinysrgb&w=700" alt="MetaStation',
     'photos/7567443/pexels-photo-7567443.jpeg?auto=compress&cs=tinysrgb&w=700" alt="MetaStation'),
    # MarginFX card
    ('portfolio/index.html',
     'photos/9577250/pexels-photo-9577250.jpeg?auto=compress&cs=tinysrgb&w=700" alt="MarginFX',
     'photos/6770610/pexels-photo-6770610.jpeg?auto=compress&cs=tinysrgb&w=700" alt="MarginFX'),
    # Neobank Platform card
    ('portfolio/index.html',
     'photos/9577254/pexels-photo-9577254.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Neobank Platform',
     'photos/4386431/pexels-photo-4386431.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Neobank Platform'),
    # Portfolio hero bg - same as about
    ('portfolio/index.html',
     'photos/3184338/pexels-photo-3184338.jpeg?auto=compress&cs=tinysrgb&w=1800" alt="Portfolio',
     'photos/1181671/pexels-photo-1181671.jpeg?auto=compress&cs=tinysrgb&w=1800" alt="Portfolio'),

    # ── ABOUT ──
    # About hero - change to team/office photo
    ('about/index.html',
     'photos/3184338/pexels-photo-3184338.jpeg?auto=compress&cs=tinysrgb&w=1800" alt="About PumaPulse',
     'photos/1181406/pexels-photo-1181406.jpeg?auto=compress&cs=tinysrgb&w=1800" alt="About PumaPulse'),
    # About main image - team working
    ('about/index.html',
     'photos/3184291/pexels-photo-3184291.jpeg?auto=compress&cs=tinysrgb&w=900" alt="PumaPulse Team',
     'photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&w=900" alt="PumaPulse Team'),
    # About services image
    ('about/index.html',
     'photos/3861969/pexels-photo-3861969.jpeg?auto=compress&cs=tinysrgb&w=900" alt="PumaPulse Services',
     'photos/546819/pexels-photo-546819.jpeg?auto=compress&cs=tinysrgb&w=900" alt="PumaPulse Services'),
    # About journey image
    ('about/index.html',
     'photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&w=900" alt="PumaPulse Journey',
     'photos/3184339/pexels-photo-3184339.jpeg?auto=compress&cs=tinysrgb&w=900" alt="PumaPulse Journey'),

    # ── BLOG ──
    # Blog hero
    ('blog/index.html',
     'photos/3184338/pexels-photo-3184338.jpeg?auto=compress&cs=tinysrgb&w=1800" alt="PumaPulse Blog',
     'photos/546819/pexels-photo-546819.jpeg?auto=compress&cs=tinysrgb&w=1800" alt="PumaPulse Blog'),

    # ── CAREERS ──
    # Careers hero
    ('careers/index.html',
     'photo-1522071820081-009f0129c71c?w=1800',
     'photo-1522071820081-009f0129c71c?w=1800&q=90'),
]

for filepath, old, new in FIXES:
    if not os.path.exists(filepath):
        print(f'SKIP (not found): {filepath}')
        continue
    with open(filepath, 'rb') as f:
        raw = f.read()
    content = raw.decode('utf-8', errors='replace')
    if old in content:
        content = content.replace(old, new)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed [{filepath}]: {old[:60]}')
    else:
        print(f'Not found [{filepath}]: {old[:60]}')

print('\nDone!')
