import re

# Update style.css - reduce border-radius values for squarer look
with open('css/style.css', 'rb') as f:
    raw = f.read()
c = raw.decode('utf-8', errors='replace')

# Change --rl variable from 16px to 6px (main card radius)
c = re.sub(r'--rl:\s*\d+px', '--rl:6px', c)

# Reduce large border-radius values
c = re.sub(r'border-radius:20px', 'border-radius:4px', c)
c = re.sub(r'border-radius:16px', 'border-radius:4px', c)
c = re.sub(r'border-radius:14px', 'border-radius:4px', c)
c = re.sub(r'border-radius:var\(--rl\)', 'border-radius:4px', c)
# Keep 50px for pills/tags and 50% for circles
# Reduce medium ones
c = re.sub(r'border-radius:12px', 'border-radius:3px', c)
c = re.sub(r'border-radius:10px', 'border-radius:3px', c)
c = re.sub(r'border-radius:9px', 'border-radius:3px', c)
c = re.sub(r'border-radius:8px', 'border-radius:2px', c)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed style.css')

# Update theme.css
with open('css/theme.css', 'rb') as f:
    raw = f.read()
c = raw.decode('utf-8', errors='replace')
c = re.sub(r'--rl:\s*\d+px', '--rl:6px', c)
c = re.sub(r'border-radius:20px', 'border-radius:4px', c)
c = re.sub(r'border-radius:16px', 'border-radius:4px', c)
c = re.sub(r'border-radius:14px', 'border-radius:4px', c)
c = re.sub(r'border-radius:var\(--rl\)', 'border-radius:4px', c)
with open('css/theme.css', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed theme.css')
