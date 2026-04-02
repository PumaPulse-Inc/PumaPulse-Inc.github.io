import glob

files = glob.glob('**/*.html', recursive=True)

# All broken byte sequences mapped to their correct replacement
FIXES = [
    # Triple-encoded em dash (pattern 1)
    (b'\xc3\x83\xc2\xa2\xc3\xa2\xe2\x80\x9a\xc2\xac\xc3\xa2\xe2\x82\xac\xc2\x9d', '\u2014'.encode()),
    # Triple-encoded en dash (pattern 1)
    (b'\xc3\x83\xc2\xa2\xc3\xa2\xe2\x80\x9a\xc2\xac\xc3\xa2\xe2\x82\xac\xc2\x9c', '\u2013'.encode()),
    # Triple-encoded right single quote
    (b'\xc3\x83\xc2\xa2\xc3\xa2\xe2\x80\x9a\xc2\xac\xc3\xa2\xe2\x82\xac\xc2\x99', b"'"),
    # Triple-encoded left single quote
    (b'\xc3\x83\xc2\xa2\xc3\xa2\xe2\x80\x9a\xc2\xac\xc3\xa2\xe2\x82\xac\xc2\x98', b"'"),
    # Triple-encoded ellipsis
    (b'\xc3\x83\xc2\xa2\xc3\xa2\xe2\x80\x9a\xc2\xac\xc3\xa2\xe2\x82\xac\xc2\xa6', b'...'),
    # Triple-encoded left double quote
    (b'\xc3\x83\xc2\xa2\xc3\xa2\xe2\x80\x9a\xc2\xac\xc5\x93', b'"'),
    # Triple-encoded right double quote
    (b'\xc3\x83\xc2\xa2\xc3\xa2\xe2\x80\x9a\xc2\xac\xc2\x9d', b'"'),
    # Triple-encoded em dash (pattern 3 - careers style)
    (b'\xc3\x83\xc2\xa2\xc3\xa2\xe2\x80\x9a\xc2\xac\xc3\xa2\xe2\x80\x94', '\u2014'.encode()),
    # Triple-encoded en dash (pattern 3)
    (b'\xc3\x83\xc2\xa2\xc3\xa2\xe2\x80\x9a\xc2\xac\xc3\xa2\xe2\x80\x93', '\u2013'.encode()),
    # Triple-encoded right single quote (pattern 3)
    (b'\xc3\x83\xc2\xa2\xc3\xa2\xe2\x80\x9a\xc2\xac\xc3\xa2\xe2\x80\x99', b"'"),
    # Triple-encoded left single quote (pattern 3)
    (b'\xc3\x83\xc2\xa2\xc3\xa2\xe2\x80\x9a\xc2\xac\xc3\xa2\xe2\x80\x98', b"'"),
    # Triple-encoded ellipsis (pattern 3)
    (b'\xc3\x83\xc2\xa2\xc3\xa2\xe2\x80\x9a\xc2\xac\xc3\xa2\xe2\x80\xa6', b'...'),
    # Ends in ascii quote (careers 1-3 days)
    (b'\xc3\x83\xc2\xa2\xc3\xa2\xe2\x80\x9a\xc2\xac\x22', b'-'),
    # Double-encoded em dash (pattern 2)
    (b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9d', '\u2014'.encode()),
    # Double-encoded en dash (pattern 2)
    (b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9c', '\u2013'.encode()),
    # Double-encoded right single quote
    (b'\xc3\xa2\xe2\x82\xac\xe2\x84\xa2', b"'"),
    # Double-encoded left single quote
    (b'\xc3\xa2\xe2\x82\xac\xcb\x9c', b"'"),
    # Double-encoded ellipsis
    (b'\xc3\xa2\xe2\x82\xac\xc2\xa6', b'...'),
    # Double-encoded left double quote
    (b'\xc3\xa2\xe2\x82\xac\xc5\x93', b'"'),
    # contact checkmark glyph used as tick
    (b'\xc3\x83\xc2\xa2\xc3\x85\xe2\x80\x9c', b'\xe2\x9c\x93'),
    # blockchain title garbage: c2 a2 ... c5 a1 c3 82 c2 ac c3 a2 e2 82 ac c2 9d
    (b'\xc2\xa2\xc3\x83\xc2\xa2\xc3\xa2\xe2\x82\xac\xc5\xa1\xc3\x82\xc2\xac\xc3\xa2\xe2\x82\xac\xc2\x9d', b'\xe2\x80\x94'),
    # title variant: e2 80 9x a2 c3 83 c2 a2 c3 a2 e2 82 ac c5 a1 c2 ac c3 83 c2 a2 c3 a2
    (b'\xe2\x80\x9d\xc2\xa2\xc3\x83\xc2\xa2\xc3\xa2\xe2\x82\xac\xc5\xa1\xc2\xac\xc3\x83\xc2\xa2\xc3\xa2', b' \xe2\x80\x94 '),
    (b'\xc2\xa2\xc3\x83\xc2\xa2\xc3\xa2\xe2\x82\xac\xc5\xa1\xc2\xac\xc3\x83\xc2\xa2\xc3\xa2', b'\xe2\x80\x94'),
    # stray c3 82 c2 9d (right quote artifact)
    (b'\xc3\x82\xc2\x9d', b''),
    # stray non-breaking space
    (b'\xc3\x82\xc2\xa0', b' '),
    # stray c3 82 alone
    (b'\xc3\x82', b''),
]

for f in files:
    if 'fintech' in f:
        print('Skipped (locked):', f)
        continue
    try:
        with open(f, 'rb') as fh:
            raw = fh.read()
        fixed = raw
        for bad, good in FIXES:
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
