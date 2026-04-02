import re

with open('css/style.css', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8', errors='replace')

# Replace the :root block with light theme values
new_root = ''':root {
  --bg:       #f4f7ff;
  --bg2:      #e8eef9;
  --bg3:      #dde5f5;
  --card:     #ffffff;
  --border:   rgba(0,0,0,0.09);
  --border2:  rgba(0,0,0,0.16);
  --text:     #0f172a;
  --muted:    rgba(15,23,42,0.42);
  --muted2:   rgba(15,23,42,0.65);
  --primary:  #1d4ed8;
  --accent:   #10b981;
  --purple:   #7c3aed;
  --pd:       rgba(29,78,216,0.10);
  --ad:       rgba(16,185,129,0.10);
  --vd:       rgba(124,58,237,0.10);
  --grad:     linear-gradient(135deg,#1d4ed8,#10b981);
  --grad2:    linear-gradient(135deg,#7c3aed,#1d4ed8);
  --grad3:    linear-gradient(135deg,#10b981,#7c3aed);
  --shadow:   0 8px 32px rgba(0,0,0,0.10);
  --font:     'Inter', sans-serif;
  --rl:       16px;
}'''

fixed = re.sub(r':root\s*\{[^}]+\}', new_root, content, count=1)

if fixed != content:
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(fixed)
    print('Fixed :root vars')
else:
    print('Not found')
