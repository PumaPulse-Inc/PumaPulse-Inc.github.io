import re

with open('about/index.html', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8', errors='replace')

NEW_VALUES = '''<section class="section" style="background:var(--bg2)">
  <div class="container">
    <div class="text-center reveal">
      <span class="eyebrow">Our Values</span>
      <h2>What Drives <span class="grad-text2">Everything We Do</span></h2>
      <div class="section-divider"></div>
    </div>
    <div class="svc-grid reveal-stagger" style="grid-template-columns:repeat(3,1fr)">
      <div class="svc-card" style="padding:32px">
        <div style="width:52px;height:52px;border-radius:14px;background:var(--ad);display:flex;align-items:center;justify-content:center;margin-bottom:20px">
          <svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" style="width:24px;height:24px"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        </div>
        <h3 style="margin-bottom:10px">Security First</h3>
        <p>Every product we ship is built with security as a foundation, not an afterthought. We follow industry best practices and conduct thorough audits before launch.</p>
      </div>
      <div class="svc-card" style="padding:32px">
        <div style="width:52px;height:52px;border-radius:14px;background:var(--pd);display:flex;align-items:center;justify-content:center;margin-bottom:20px">
          <svg viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="2" stroke-linecap="round" style="width:24px;height:24px"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
        </div>
        <h3 style="margin-bottom:10px">Speed Without Compromise</h3>
        <p>We move fast and ship on time. Our agile process and pre-built modules let us deliver production-ready products in weeks, not months.</p>
      </div>
      <div class="svc-card" style="padding:32px">
        <div style="width:52px;height:52px;border-radius:14px;background:var(--vd);display:flex;align-items:center;justify-content:center;margin-bottom:20px">
          <svg viewBox="0 0 24 24" fill="none" stroke="#7c3aed" stroke-width="2" stroke-linecap="round" style="width:24px;height:24px"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
        </div>
        <h3 style="margin-bottom:10px">Client Partnership</h3>
        <p>We treat every client as a long-term partner. Transparent communication, honest advice, and genuine investment in your success.</p>
      </div>
      <div class="svc-card" style="padding:32px">
        <div style="width:52px;height:52px;border-radius:14px;background:rgba(245,158,11,0.12);display:flex;align-items:center;justify-content:center;margin-bottom:20px">
          <svg viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2" stroke-linecap="round" style="width:24px;height:24px"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/></svg>
        </div>
        <h3 style="margin-bottom:10px">On-Time Delivery</h3>
        <p>We respect your timeline. Our project management process ensures milestones are hit, scope is controlled, and you always know exactly where things stand.</p>
      </div>
      <div class="svc-card" style="padding:32px">
        <div style="width:52px;height:52px;border-radius:14px;background:var(--ad);display:flex;align-items:center;justify-content:center;margin-bottom:20px">
          <svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" style="width:24px;height:24px"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
        </div>
        <h3 style="margin-bottom:10px">Performance Obsessed</h3>
        <p>We benchmark everything. From matching engine throughput to API response times, we optimize relentlessly to ensure your product performs at scale.</p>
      </div>
      <div class="svc-card" style="padding:32px">
        <div style="width:52px;height:52px;border-radius:14px;background:var(--pd);display:flex;align-items:center;justify-content:center;margin-bottom:20px">
          <svg viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="2" stroke-linecap="round" style="width:24px;height:24px"><path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
        </div>
        <h3 style="margin-bottom:10px">Compliance Built-In</h3>
        <p>Regulatory compliance is not optional in fintech. We build KYC, AML, and reporting requirements into every product from the ground up.</p>
      </div>
    </div>
  </div>
</section>'''

NEW_WHY = '''<!-- Why PumaPulse -->
<section class="section">
  <div class="container">
    <div class="split">
      <div class="reveal-left">
        <span class="eyebrow">Why Choose Us</span>
        <h2>We Don't Just Build Software <span class="grad-text">We Build Businesses</span></h2>
        <div class="section-divider" style="margin:0 0 24px"></div>
        <p style="margin-bottom:28px">Most dev shops take your requirements and disappear. We stay engaged throughout — from architecture review to post-launch support. Our clients don't just get a product, they get a technical partner who's invested in their success.</p>
        <div style="display:flex;flex-direction:column;gap:16px">'''

# Replace the values section
fixed = re.sub(
    r'<section class="section" style="background:var\(--bg2\)">\s*<div class="container">\s*<div class="text-center reveal">\s*<span class="eyebrow">Our Values</span>[\s\S]*?</section>',
    NEW_VALUES,
    content, count=1
)

# Fix the broken Why section opening
fixed = re.sub(
    r'<!-- Why PumaPulse -->[\s\S]*?<div class="reveal-left">.*?</div>\s*\n\s*<span class="eyebrow">Why Choose Us</span>',
    NEW_WHY,
    fixed, count=1
)

if fixed != content:
    with open('about/index.html', 'w', encoding='utf-8') as f:
        f.write(fixed)
    print('Fixed!')
else:
    print('No changes made')
