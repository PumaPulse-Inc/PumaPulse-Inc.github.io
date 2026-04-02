import glob, re

# Fix 1: "Learn more ?" -> "Learn more" with arrow SVG
ARROW = ' <svg viewBox="0 0 14 14" fill="none" style="width:12px;height:12px;vertical-align:middle"><path d="M1 7h12M7 1l6 6-6 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

# Fix 2: broken simpleicons CDN logos -> use inline SVG or alternative
# Avalanche: red A logo
AVALANCHE_SVG = '<svg viewBox="0 0 24 24" fill="#E84142" style="width:32px;height:32px"><path d="M9.17 15.5H6.33a.5.5 0 01-.43-.75l5.67-9.83a.5.5 0 01.86 0l5.67 9.83a.5.5 0 01-.43.75h-2.84l-2.46-4.26-2.46 4.26z"/></svg>'
# Arbitrum: blue logo
ARBITRUM_SVG = '<svg viewBox="0 0 24 24" fill="none" style="width:32px;height:32px"><circle cx="12" cy="12" r="10" fill="#28A0F0"/><path d="M8 16l2.5-4.5L13 16M11 13.5l1.5-2.5 1.5 2.5" stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
# Optimism: red circle
OPTIMISM_SVG = '<svg viewBox="0 0 24 24" style="width:32px;height:32px"><circle cx="12" cy="12" r="10" fill="#FF0420"/><text x="12" y="16" text-anchor="middle" fill="white" font-size="10" font-weight="bold">OP</text></svg>'
# zkSync: blue
ZKSYNC_SVG = '<svg viewBox="0 0 24 24" fill="none" style="width:32px;height:32px"><circle cx="12" cy="12" r="10" fill="#1B5EE4"/><path d="M7 12l3 3 7-7" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

files = glob.glob('**/*.html', recursive=True)
for f in files:
    if 'fintech/index' in f:
        continue
    try:
        with open(f, 'rb') as fh:
            raw = fh.read()
        content = raw.decode('utf-8', errors='replace')
        fixed = content

        # Fix "Learn more ?" broken arrow
        fixed = re.sub(r'Learn more\s*[?â€º›»→]', 'Learn more' + ARROW, fixed)
        fixed = fixed.replace('Learn more ?', 'Learn more' + ARROW)

        # Fix broken simpleicons for chains
        fixed = re.sub(
            r'<img src="https://cdn\.simpleicons\.org/avalanche/[^"]*"[^>]*>',
            AVALANCHE_SVG, fixed
        )
        fixed = re.sub(
            r'<img src="https://cdn\.simpleicons\.org/arbitrum/[^"]*"[^>]*>',
            ARBITRUM_SVG, fixed
        )
        fixed = re.sub(
            r'<img src="https://cdn\.simpleicons\.org/optimism/[^"]*"[^>]*>',
            OPTIMISM_SVG, fixed
        )
        fixed = re.sub(
            r'<img src="https://cdn\.simpleicons\.org/zksync/[^"]*"[^>]*>',
            ZKSYNC_SVG, fixed
        )

        if fixed != content:
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(fixed)
            print('Fixed:', f)
        else:
            print('Clean:', f)
    except Exception as e:
        print('Error:', f, e)

print('Done!')
