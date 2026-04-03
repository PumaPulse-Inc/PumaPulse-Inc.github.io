import re

with open('about/index.html', 'rb') as f:
    raw = f.read()
c = raw.decode('utf-8', errors='replace')

# Remove duplicate image - keep only one, replace with better image
c = re.sub(
    r'(<div class="reveal-right">\s*)<img[^>]*546819[^>]*>\s*\r?\n\s*<img[^>]*546819[^>]*>',
    r'\1<img src="https://images.pexels.com/photos/3184338/pexels-photo-3184338.jpeg?auto=compress&cs=tinysrgb&w=900" alt="PumaPulse Team at Work" style="width:100%;height:480px;object-fit:cover;border-radius:20px">',
    c
)

# Also fix if only one duplicate exists
c = re.sub(
    r'(<div class="reveal-right">\s*)<img[^>]*546819[^>]*>',
    r'\1<img src="https://images.pexels.com/photos/3184338/pexels-photo-3184338.jpeg?auto=compress&cs=tinysrgb&w=900" alt="PumaPulse Team at Work" style="width:100%;height:480px;object-fit:cover;border-radius:20px">',
    c, count=1
)

with open('about/index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Done')
