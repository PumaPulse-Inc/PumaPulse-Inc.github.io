with open('index.html', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8', errors='replace')
fixed = content.replace("onclick=\"showSol('", "onclick=\"switchSol('")
fixed = fixed.replace(",this)", ",this)")
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(fixed)
print('Fixed sol tabs')
