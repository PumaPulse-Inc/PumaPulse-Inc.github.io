import re

with open('about/index.html', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8', errors='replace')

# Remove the entire section containing "Dedicated Teams" / "Our Team"
# Match from <section opening before the team heading to </section>
fixed = re.sub(
    r'<section[^>]*>[\s\S]*?Dedicated Teams[\s\S]*?</section>',
    '', content, count=1
)

if fixed == content:
    # Try matching by team-grid class
    fixed = re.sub(
        r'<section[^>]*>[\s\S]*?team-grid[\s\S]*?</section>',
        '', content, count=1
    )

if fixed != content:
    with open('about/index.html', 'w', encoding='utf-8') as f:
        f.write(fixed)
    print('Removed team section')
else:
    print('Not found via regex, trying manual boundary search')
    # Find start: look for the section containing team-grid
    start = content.find('<section', content.find('team-grid') - 500)
    # Find matching </section>
    depth = 0
    i = start
    while i < len(content):
        if content[i:i+8] == '<section':
            depth += 1
        elif content[i:i+10] == '</section>':
            depth -= 1
            if depth == 0:
                end = i + 10
                break
        i += 1
    fixed = content[:start] + content[end:]
    with open('about/index.html', 'w', encoding='utf-8') as f:
        f.write(fixed)
    print(f'Removed team section (manual: chars {start}-{end})')
