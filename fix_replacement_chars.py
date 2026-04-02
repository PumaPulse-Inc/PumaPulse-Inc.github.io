import glob, re

EM = '\u2014'

files = glob.glob('**/*.html', recursive=True)
for f in files:
    if 'fintech/index' in f:
        print('Skipped:', f)
        continue
    try:
        with open(f, 'rb') as fh:
            raw = fh.read()
        content = raw.decode('utf-8', errors='replace')
        fixed = content.replace('\ufffd', EM)
        # Fix "—"" pattern (em dash followed by stray quote)
        fixed = fixed.replace(EM + '"', EM + ' ')
        fixed = fixed.replace(EM + ' "', EM + ' ')
        if fixed != content:
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(fixed)
            print('Fixed:', f)
        else:
            print('Clean:', f)
    except Exception as e:
        print('Error:', f, e)
print('Done!')
