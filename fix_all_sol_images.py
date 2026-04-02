with open('index.html', 'rb') as f:
    raw = f.read()
c = raw.decode('utf-8', errors='replace')

FIXES = [
    # Exchange panel
    ('9577240/pexels-photo-9577240.jpeg?auto=compress&cs=tinysrgb&w=500" alt="CEX',
     '844124/pexels-photo-844124.jpeg?auto=compress&cs=tinysrgb&w=500" alt="CEX'),
    ('8358134/pexels-photo-8358134.jpeg?auto=compress&cs=tinysrgb&w=500" alt="DEX',
     '7567443/pexels-photo-7567443.jpeg?auto=compress&cs=tinysrgb&w=500" alt="DEX'),
    # P2P - already ok (6802042)
    # Hybrid
    ('1181671/pexels-photo-1181671.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Hybrid',
     '3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Hybrid'),
    # White-label
    ('3184339/pexels-photo-3184339.jpeg?auto=compress&cs=tinysrgb&w=500" alt="White',
     '3184291/pexels-photo-3184291.jpeg?auto=compress&cs=tinysrgb&w=500" alt="White'),
    # Derivatives
    ('14832157/pexels-photo-14832157.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Derivatives',
     '6770610/pexels-photo-6770610.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Derivatives'),

    # Banking panel - all three have generic blockchain phone images
    ('9577253/pexels-photo-9577253.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Neobank',
     '3943716/pexels-photo-3943716.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Neobank'),
    ('9577250/pexels-photo-9577250.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Digital Banking',
     '4386431/pexels-photo-4386431.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Digital Banking'),
    ('9577236/pexels-photo-9577236.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Fintech',
     '3184338/pexels-photo-3184338.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Fintech'),

    # Payments panel
    ('9577231/pexels-photo-9577231.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Gateway',
     '4386370/pexels-photo-4386370.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Gateway'),
    ('9577233/pexels-photo-9577233.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Cross Border',
     '3943723/pexels-photo-3943723.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Cross Border'),

    # Trading panel
    ('7267598/pexels-photo-7267598.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Algo',
     '6801648/pexels-photo-6801648.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Algo'),

    # Forex panel
    ('9577254/pexels-photo-9577254.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Forex CRM',
     '6770520/pexels-photo-6770520.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Forex CRM'),
    ('9588213/pexels-photo-9588213.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Back Office',
     '3184418/pexels-photo-3184418.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Back Office'),
]

count = 0
for old, new in FIXES:
    if old in c:
        c = c.replace(old, new)
        count += 1
        print(f'Fixed: {old[:50]}')
    else:
        print(f'Not found: {old[:50]}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print(f'\nDone! {count} fixes applied.')
