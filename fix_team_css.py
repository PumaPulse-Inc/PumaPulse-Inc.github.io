with open('css/style.css', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8', errors='replace')

old = '.team-photo{height:240px;overflow:hidden}\r\n.team-photo img{width:100%;height:100%;object-fit:cover;transition:transform 0.5s}\r\n.team-card:hover .team-photo img{transform:scale(1.05)}\r\n'
new = '.team-avatar{height:200px;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden}\r\n.team-initials{font-size:3rem;font-weight:800;color:#fff;letter-spacing:-2px;position:relative;z-index:2}\r\n.team-avatar-icon{position:absolute;bottom:-10px;right:-10px;width:80px;height:80px;opacity:0.25}\r\n.team-avatar-icon svg{width:100%;height:100%}\r\n'

if old in content:
    content = content.replace(old, new)
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed team CSS')
else:
    print('Not found, trying without \\r')
    old2 = '.team-photo{height:240px;overflow:hidden}\n.team-photo img{width:100%;height:100%;object-fit:cover;transition:transform 0.5s}\n.team-card:hover .team-photo img{transform:scale(1.05)}\n'
    new2 = '.team-avatar{height:200px;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden}\n.team-initials{font-size:3rem;font-weight:800;color:#fff;letter-spacing:-2px;position:relative;z-index:2}\n.team-avatar-icon{position:absolute;bottom:-10px;right:-10px;width:80px;height:80px;opacity:0.25}\n.team-avatar-icon svg{width:100%;height:100%}\n'
    if old2 in content:
        content = content.replace(old2, new2)
        with open('css/style.css', 'w', encoding='utf-8') as f:
            f.write(content)
        print('Fixed team CSS (no \\r)')
    else:
        print('Still not found')
