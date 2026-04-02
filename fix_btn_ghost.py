with open('css/style.css', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8', errors='replace')

old = 'btn-ghost{background:rgba(255,255,255,0.06);color:var(--muted2);border:1px solid var(--border)}\r\r\n.btn-ghost:hover{background:rgba(255,255,255,0.10);color:var(--text);border-color:var(--border2)}'
new = 'btn-ghost{background:rgba(255,255,255,0.08);color:#fff;border:1.5px solid rgba(255,255,255,0.28)}\r\n.btn-ghost:hover{background:rgba(255,255,255,0.14);color:#fff;border-color:rgba(255,255,255,0.5)}'

if old in content:
    content = content.replace(old, new)
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed btn-ghost')
else:
    print('Not found, trying without extra \\r')
    old2 = 'btn-ghost{background:rgba(255,255,255,0.06);color:var(--muted2);border:1px solid var(--border)}\r\n.btn-ghost:hover{background:rgba(255,255,255,0.10);color:var(--text);border-color:var(--border2)}'
    if old2 in content:
        content = content.replace(old2, new)
        with open('css/style.css', 'w', encoding='utf-8') as f:
            f.write(content)
        print('Fixed btn-ghost (v2)')
    else:
        # brute force
        import re
        content = re.sub(
            r'\.btn-ghost\{[^}]+\}',
            '.btn-ghost{background:rgba(255,255,255,0.08);color:#fff;border:1.5px solid rgba(255,255,255,0.28)}',
            content
        )
        content = re.sub(
            r'\.btn-ghost:hover\{[^}]+\}',
            '.btn-ghost:hover{background:rgba(255,255,255,0.14);color:#fff;border-color:rgba(255,255,255,0.5)}',
            content
        )
        with open('css/style.css', 'w', encoding='utf-8') as f:
            f.write(content)
        print('Fixed btn-ghost (regex)')
