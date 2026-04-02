import os

FIXES = [
    # Blog featured - crypto exchange guide
    ('blog/index.html',
     'photos/9577236/pexels-photo-9577236.jpeg?auto=compress&cs=tinysrgb&w=900" alt="Crypto Exchange Guide',
     'photos/844124/pexels-photo-844124.jpeg?auto=compress&cs=tinysrgb&w=900" alt="Crypto Exchange Guide'),
    # Arbitrage bots
    ('blog/index.html',
     'photos/7267598/pexels-photo-7267598.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Arbitrage Bots',
     'photos/6801648/pexels-photo-6801648.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Arbitrage Bots'),
    # Neobank
    ('blog/index.html',
     'photos/9577253/pexels-photo-9577253.jpeg?auto=compress&cs=tinysrgb&w=600" alt="Neobank',
     'photos/3943716/pexels-photo-3943716.jpeg?auto=compress&cs=tinysrgb&w=600" alt="Neobank'),
    # DEX
    ('blog/index.html',
     'photos/9577231/pexels-photo-9577231.jpeg?auto=compress&cs=tinysrgb&w=700" alt="DEX',
     'photos/7567443/pexels-photo-7567443.jpeg?auto=compress&cs=tinysrgb&w=700" alt="DEX'),
    # Forex CRM
    ('blog/index.html',
     'photos/9577250/pexels-photo-9577250.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Forex CRM',
     'photos/6770610/pexels-photo-6770610.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Forex CRM'),
    # Grid Trading
    ('blog/index.html',
     'photos/7267598/pexels-photo-7267598.jpeg?auto=compress&cs=tinysrgb&w=600" alt="Grid Trading',
     'photos/6802042/pexels-photo-6802042.jpeg?auto=compress&cs=tinysrgb&w=600" alt="Grid Trading'),
    # Crypto Payments
    ('blog/index.html',
     'photos/9588213/pexels-photo-9588213.jpeg?auto=compress&cs=tinysrgb&w=600" alt="Crypto Payments',
     'photos/4386370/pexels-photo-4386370.jpeg?auto=compress&cs=tinysrgb&w=600" alt="Crypto Payments'),
]

for filepath, old, new in FIXES:
    with open(filepath, 'rb') as f:
        raw = f.read()
    content = raw.decode('utf-8', errors='replace')
    if old in content:
        content = content.replace(old, new)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed: {old[:70]}')
    else:
        print(f'Not found: {old[:70]}')

print('Done!')
