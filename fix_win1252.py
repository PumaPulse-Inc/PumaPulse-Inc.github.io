import glob

# Windows-1252 special chars that appear as raw bytes in HTML files
WIN1252_FIXES = [
    (b'\x97', '\u2014'.encode('utf-8')),  # em dash
    (b'\x96', '\u2013'.encode('utf-8')),  # en dash
    (b'\x91', b"'"),                       # left single quote
    (b'\x92', b"'"),                       # right single quote
    (b'\x93', b'"'),                       # left double quote
    (b'\x94', b'"'),                       # right double quote
    (b'\x85', b'...'),                     # ellipsis
    (b'\x95', b'\xe2\x80\xa2'),            # bullet
    (b'\x99', b'\xe2\x84\xa2'),            # trademark
]

files = glob.glob('**/*.html', recursive=True)
for f in files:
    if 'fintech' in f and 'fintech_new' not in f:
        print('Skipped (locked):', f)
        continue
    try:
        with open(f, 'rb') as fh:
            raw = fh.read()
        fixed = raw
        for bad, good in WIN1252_FIXES:
            fixed = fixed.replace(bad, good)
        if fixed != raw:
            with open(f, 'wb') as fh:
                fh.write(fixed)
            print('Fixed:', f)
        else:
            print('Clean:', f)
    except Exception as e:
        print('Error:', f, str(e))

print('\nDone!')
