import re

with open('index.html', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8', errors='replace')

# 1. Fix duplicate live card inner divs (triple repeated)
# Pattern: <div>...<div class="live-card-label">...</div>...</div> repeated 3x
content = re.sub(
    r'(<div class="live-card-icon"><img[^>]+></div>)\s*(<div>.*?</div>)\s*\2\s*\2',
    r'\1\n          \2',
    content, flags=re.DOTALL
)

# 2. Update live card styles - square corners like v2
content = content.replace(
    'border-radius:16px;padding:18px 22px;display:flex;align-items:center;gap:14px;animation:slideDown 0.6s both}',
    'padding:18px 22px;display:flex;align-items:center;gap:14px;animation:slideDown 0.6s both;position:relative;overflow:hidden}'
)
# Add red top border line like v2 dash-widget
content = content.replace(
    '.live-card:nth-child(2){animation-delay:0.15s}',
    '.live-card::before{content:"";position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,rgba(192,32,42,0.8),transparent)}.live-card:nth-child(2){animation-delay:0.15s}'
)

# 3. Remove border-radius from live-card-icon
content = content.replace(
    '.live-card-icon{width:44px;height:44px;border-radius:12px;overflow:hidden;flex-shrink:0}',
    '.live-card-icon{width:44px;height:44px;overflow:hidden;flex-shrink:0}'
)

# 4. Add hero grid overlay and orbs to hero section
# Find the hero section and add grid + orbs
old_hero_bg = '<div class="hero-grid-line"></div>'
new_hero_bg = '''<div class="hero-grid-line"></div>
  <div class="hero-grid-overlay" style="position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,0.025) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.025) 1px,transparent 1px);background-size:80px 80px;pointer-events:none;z-index:1"></div>
  <div style="position:absolute;top:-180px;left:-120px;width:900px;height:700px;border-radius:50%;background:radial-gradient(ellipse,rgba(192,32,42,0.15) 0%,transparent 65%);pointer-events:none;z-index:1"></div>
  <div style="position:absolute;bottom:-200px;right:-80px;width:700px;height:600px;border-radius:50%;background:radial-gradient(ellipse,rgba(59,130,246,0.08) 0%,transparent 65%);pointer-events:none;z-index:1"></div>'''

content = content.replace(old_hero_bg, new_hero_bg, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
