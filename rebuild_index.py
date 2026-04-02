import re

# Read source full version (UTF-16)
with open('index_full.html', 'rb') as f:
    raw = f.read()
src = raw.decode('utf-16', errors='replace')

# Read current index.html (has the correct hero)
with open('index.html', 'rb') as f:
    raw2 = f.read()
cur = raw2.decode('utf-8', errors='replace')

# From current: extract everything up to end of hero section (keep hero intact)
# Hero ends after the closing </section> of the hero
hero_end = cur.rfind('</section>')
if hero_end == -1:
    print('ERROR: no </section> found in current index')
    exit()
hero_part = cur[:hero_end + 10]
print('Hero part length:', len(hero_part))

# From source: extract all sections AFTER the hero
# Find where the hero ends in source
src_hero_end = src.find('<!-- Ticker -->')
if src_hero_end == -1:
    # try finding after the hero section
    src_hero_end = src.find('<!-- Stats -->')
if src_hero_end == -1:
    src_hero_end = src.find('stats-row')
    src_hero_end = src.rfind('\n', 0, src_hero_end) + 1
print('Source sections start at:', src_hero_end)

# Get everything from source after hero up to footer
src_footer = src.find('<div id="footer-placeholder">')
if src_footer == -1:
    src_footer = src.find('footer-placeholder')
    src_footer = src.rfind('<div', 0, src_footer)
print('Source footer at:', src_footer)

middle_sections = src[src_hero_end:src_footer]
print('Middle sections length:', len(middle_sections))

# Get footer and scripts from current index
cur_footer_idx = cur.find('</section>')
# Actually get the last part - scripts
scripts = '\n\n<div id="footer-placeholder"></div>\n<script src="js/nav.js"></script>\n<script src="js/main.js"></script>\n<script src="js/animations.js"></script>\n</body>\n</html>\n'

# Combine
result = hero_part + '\n\n' + middle_sections + scripts

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(result)

# Verify
print('\nVerification:')
print('Has process:', 'process-step' in result)
print('Has FAQ:', 'faq-item' in result)
print('Has testi:', 'testi-card' in result)
print('Has portfolio:', 'portfolio-card' in result)
print('Has tech:', 'tech-logo' in result)
print('Total chars:', len(result))
