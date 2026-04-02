import re

# Map of old image IDs to new unique, contextually appropriate ones
# Format: (old_url_fragment, new_url)
REPLACEMENTS = [
    # Service cards on main page - each gets a unique relevant image
    # Crypto Exchange card
    ('photos/7267598/pexels-photo-7267598.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Crypto Exchange',
     'photos/844124/pexels-photo-844124.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Crypto Exchange'),
    # Trading Bots card
    ('photos/9577236/pexels-photo-9577236.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Trading Bots',
     'photos/6801648/pexels-photo-6801648.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Trading Bots'),
    # Fintech/Neobank card
    ('photos/9577253/pexels-photo-9577253.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Fintech Banking',
     'photos/3943716/pexels-photo-3943716.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Fintech Banking'),
    # Forex card
    ('photos/9577250/pexels-photo-9577250.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Forex Trading',
     'photos/6770610/pexels-photo-6770610.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Forex Trading'),

    # Solutions panel - Exchange tab
    ('photos/9577240/pexels-photo-9577240.jpeg?auto=compress&cs=tinysrgb&w=500" alt="CEX',
     'photos/844124/pexels-photo-844124.jpeg?auto=compress&cs=tinysrgb&w=500" alt="CEX'),
    ('photos/8358134/pexels-photo-8358134.jpeg?auto=compress&cs=tinysrgb&w=500" alt="DEX',
     'photos/7567443/pexels-photo-7567443.jpeg?auto=compress&cs=tinysrgb&w=500" alt="DEX'),
    ('photos/9577243/pexels-photo-9577243.jpeg?auto=compress&cs=tinysrgb&w=500" alt="P2P',
     'photos/6802042/pexels-photo-6802042.jpeg?auto=compress&cs=tinysrgb&w=500" alt="P2P'),
    ('photos/9577254/pexels-photo-9577254.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Hybrid',
     'photos/6770520/pexels-photo-6770520.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Hybrid'),
    ('photos/9588213/pexels-photo-9588213.jpeg?auto=compress&cs=tinysrgb&w=500" alt="White',
     'photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&w=500" alt="White'),
    ('photos/14832157/pexels-photo-14832157.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Deriv',
     'photos/6770610/pexels-photo-6770610.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Deriv'),

    # Solutions panel - Trading tab
    ('photos/7267598/pexels-photo-7267598.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Algo',
     'photos/6801648/pexels-photo-6801648.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Algo'),

    # Solutions panel - Banking tab
    ('photos/9577253/pexels-photo-9577253.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Neobank',
     'photos/3943716/pexels-photo-3943716.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Neobank'),
    ('photos/9577250/pexels-photo-9577250.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Digital Banking',
     'photos/4386431/pexels-photo-4386431.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Digital Banking'),
    ('photos/9577236/pexels-photo-9577236.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Fintech',
     'photos/3184291/pexels-photo-3184291.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Fintech'),

    # Solutions panel - Payments tab
    ('photos/9577231/pexels-photo-9577231.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Gateway',
     'photos/4386370/pexels-photo-4386370.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Gateway'),
    ('photos/9577233/pexels-photo-9577233.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Cross Border',
     'photos/3943723/pexels-photo-3943723.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Cross Border'),

    # Process/Why section images
    ('photos/9577236/pexels-photo-9577236.jpeg?auto=compress&cs=tinysrgb&w=700" alt="',
     'photos/3184338/pexels-photo-3184338.jpeg?auto=compress&cs=tinysrgb&w=700" alt="'),
    ('photos/9577250/pexels-photo-9577250.jpeg?auto=compress&cs=tinysrgb&w=700" alt="',
     'photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=700" alt="'),

    # Hero live cards - use crypto/fintech icons instead of generic photos
    ('photos/7267598/pexels-photo-7267598.jpeg?auto=compress&cs=tinysrgb&w=100" alt="Exchange',
     'photos/844124/pexels-photo-844124.jpeg?auto=compress&cs=tinysrgb&w=100" alt="Exchange'),
    ('photos/9577236/pexels-photo-9577236.jpeg?auto=compress&cs=tinysrgb&w=100" alt="Bot',
     'photos/6801648/pexels-photo-6801648.jpeg?auto=compress&cs=tinysrgb&w=100" alt="Bot'),
    ('photos/9577253/pexels-photo-9577253.jpeg?auto=compress&cs=tinysrgb&w=100" alt="Neobank',
     'photos/3943716/pexels-photo-3943716.jpeg?auto=compress&cs=tinysrgb&w=100" alt="Neobank'),
    ('photos/9577231/pexels-photo-9577231.jpeg?auto=compress&cs=tinysrgb&w=100" alt="Payment',
     'photos/4386370/pexels-photo-4386370.jpeg?auto=compress&cs=tinysrgb&w=100" alt="Payment'),
]

with open('index.html', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8', errors='replace')

fixed = content
count = 0
for old, new in REPLACEMENTS:
    if old in fixed:
        fixed = fixed.replace(old, new)
        count += 1
        print(f'Replaced: ...{old[:60]}...')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(fixed)

print(f'\nDone! {count} replacements made.')
