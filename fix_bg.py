with open('index.html', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8', errors='replace')

old = 'https://images.pexels.com/photos/3861969/pexels-photo-3861969.jpeg?auto=compress&cs=tinysrgb&w=1920'

# Dark futuristic neon city lights - deep blue/purple, cinematic
# Photo 1181671: dark office with screens - professional fintech feel
# Photo 373543: dark city lights bokeh - cinematic
# Photo 1181244: dark server room - tech
# Photo 2004161: dark abstract tech lines
# Photo 1181675: dark office tech
# Best choice: abstract dark blue tech network
new = 'https://images.pexels.com/photos/2004161/pexels-photo-2004161.jpeg?auto=compress&cs=tinysrgb&w=1920'

content = content.replace(old, new, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
