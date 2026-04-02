import re

with open('about/index.html', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8', errors='replace')

# Replace each team-photo div with creative avatar
replacements = [
    (
        'photos/2379004/pexels-photo-2379004.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Ryan Kovacs" loading="lazy">',
        ''  # will be handled below
    ),
]

# Replace team-photo img tags with avatar divs
new_team = '''    <div class="team-grid reveal-stagger">
      <div class="team-card">
        <div class="team-avatar" style="background:linear-gradient(135deg,#10b981,#059669)">
          <span class="team-initials">RK</span>
          <div class="team-avatar-icon"><svg viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.35)" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
        </div>
        <div class="team-info"><h4>Ryan Kovacs</h4><div class="team-role">CEO &amp; Co-Founder</div><p>15 years in fintech. Former VP Engineering at a top-5 global exchange. Leads company vision and client strategy.</p></div>
      </div>
      <div class="team-card">
        <div class="team-avatar" style="background:linear-gradient(135deg,#3b82f6,#1d4ed8)">
          <span class="team-initials">NP</span>
          <div class="team-avatar-icon"><svg viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.35)" stroke-width="1.5"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg></div>
        </div>
        <div class="team-info"><h4>Nina Patel</h4><div class="team-role">CTO &amp; Co-Founder</div><p>Blockchain architect with 12 years experience. Built core infrastructure for 3 unicorn fintech companies. Leads all engineering.</p></div>
      </div>
      <div class="team-card">
        <div class="team-avatar" style="background:linear-gradient(135deg,#a78bfa,#7c3aed)">
          <span class="team-initials">JL</span>
          <div class="team-avatar-icon"><svg viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.35)" stroke-width="1.5"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg></div>
        </div>
        <div class="team-info"><h4>James Liu</h4><div class="team-role">Head of Product</div><p>Ex-Coinbase product lead. Shipped products used by millions of traders. Obsessed with user experience and product-market fit.</p></div>
      </div>
      <div class="team-card">
        <div class="team-avatar" style="background:linear-gradient(135deg,#f59e0b,#d97706)">
          <span class="team-initials">AM</span>
          <div class="team-avatar-icon"><svg viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.35)" stroke-width="1.5"><path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg></div>
        </div>
        <div class="team-info"><h4>Aisha Mensah</h4><div class="team-role">Head of Security</div><p>Certified blockchain security auditor. 200+ smart contract audits completed. Ensures every product we ship is bulletproof.</p></div>
      </div>'''

# Use regex to replace the entire team-grid div content
pattern = r'<div class="team-grid reveal-stagger">.*?(?=\s*</div>\s*</section>)'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content[:match.start()] + new_team + content[match.end():]
    print('Replaced team grid')
else:
    print('Pattern not found, trying line-by-line approach')
    # Fallback: replace individual photo divs
    content = re.sub(
        r'<div class="team-photo"><img src="[^"]*" alt="[^"]*" loading="lazy"></div>',
        '', content
    )
    print('Removed photo divs')

with open('about/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
