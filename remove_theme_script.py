import glob, re

files = glob.glob('**/*.html', recursive=True)
for f in files:
    if 'fintech/index' in f:
        continue
    try:
        with open(f, 'rb') as fh:
            raw = fh.read()
        content = raw.decode('utf-8', errors='replace')
        fixed = re.sub(r'\s*<script src="[^"]*theme\.js"[^>]*></script>', '', content)
        if fixed != content:
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(fixed)
            print('Fixed:', f)
        else:
            print('Clean:', f)
    except Exception as e:
        print('Error:', f, e)
print('Done!')
