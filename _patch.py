import re

# ── portfolio/index.html ─────────────────────────────────────────────────────
with open('portfolio/index.html', 'rb') as f:
    c = f.read()

# Replace stats row
old_stats = (
    b'<div class="stat-cell"><div class="stat-num" data-target="36" data-suffix="+">36+</div><p>Projects Delivered</p></div>'
)
new_stats = (
    b'<div class="stat-cell"><div class="stat-num" data-target="120" data-suffix="+">120+</div><p>Projects Delivered</p></div>'
)
c = c.replace(old_stats, new_stats)

old_sat = b'<div class="stat-cell"><div class="stat-num" data-target="95" data-suffix="%">95%</div><p>Client Satisfaction</p></div>'
new_sat = b'<div class="stat-cell"><div class="stat-num" data-target="98" data-suffix="%">98%</div><p>Client Satisfaction</p></div>'
c = c.replace(old_sat, new_sat)

old_ot = b'<div class="stat-cell"><div class="stat-num" data-target="98" data-suffix="%">98%</div><p>On-Time Delivery</p></div>'
new_ot = b'<div class="stat-cell"><div class="stat-num" data-target="40" data-suffix="+">40+</div><p>Countries Served</p></div>'
c = c.replace(old_ot, new_ot)

old_cs = b'<div class="stat-cell"><div class="stat-num" data-target="25" data-suffix="+">25+</div><p>Countries Served</p></div>'
new_cs = b'<div class="stat-cell"><div class="stat-num" data-target="2" data-prefix="$" data-suffix="B+">$2B+</div><p>Client Transaction Volume</p></div>'
c = c.replace(old_cs, new_cs)

# Add Industries section before Recognition section
industries_html = b'''
<!-- Industries We've Served -->
<section class="section">
  <div class="container">
    <div class="text-center reveal">
      <span class="eyebrow">Industries</span>
      <h2>Industries We&#39;ve <span class="grad-text">Served</span></h2>
      <div class="section-divider"></div>
      <p style="max-width:600px;margin:16px auto 0">From crypto exchanges to enterprise blockchain, we&#39;ve built production systems across every major vertical in fintech and Web3.</p>
    </div>
    <div class="svc-grid reveal-stagger" style="grid-template-columns:repeat(3,1fr);margin-top:48px">
      <div class="svc-card" style="padding:32px">
        <div style="width:52px;height:52px;border-radius:14px;background:var(--ad);display:flex;align-items:center;justify-content:center;margin-bottom:20px">
          <svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" style="width:24px;height:24px"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
        </div>
        <h3 style="margin-bottom:10px">Crypto Exchange</h3>
        <p>CEX, DEX, P2P, and hybrid exchange platforms with matching engines, liquidity management, and full compliance tooling.</p>
      </div>
      <div class="svc-card" style="padding:32px">
        <div style="width:52px;height:52px;border-radius:14px;background:var(--pd);display:flex;align-items:center;justify-content:center;margin-bottom:20px">
          <svg viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="2" stroke-linecap="round" style="width:24px;height:24px"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
        </div>
        <h3 style="margin-bottom:10px">DeFi / Web3</h3>
        <p>AMMs, lending protocols, yield aggregators, NFT marketplaces, and DAO governance platforms on EVM and non-EVM chains.</p>
      </div>
      <div class="svc-card" style="padding:32px">
        <div style="width:52px;height:52px;border-radius:14px;background:var(--vd);display:flex;align-items:center;justify-content:center;margin-bottom:20px">
          <svg viewBox="0 0 24 24" fill="none" stroke="#7c3aed" stroke-width="2" stroke-linecap="round" style="width:24px;height:24px"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/></svg>
        </div>
        <h3 style="margin-bottom:10px">Neobanking</h3>
        <p>Full-stack digital banking platforms with multi-currency accounts, virtual cards, KYC/AML, and core banking integrations.</p>
      </div>
      <div class="svc-card" style="padding:32px">
        <div style="width:52px;height:52px;border-radius:14px;background:rgba(245,158,11,0.12);display:flex;align-items:center;justify-content:center;margin-bottom:20px">
          <svg viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2" stroke-linecap="round" style="width:24px;height:24px"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
        </div>
        <h3 style="margin-bottom:10px">Forex / Trading</h3>
        <p>MT4/MT5 integrations, broker CRMs, traders rooms, IB portals, and AI-powered trading bots for FX and CFD brokers.</p>
      </div>
      <div class="svc-card" style="padding:32px">
        <div style="width:52px;height:52px;border-radius:14px;background:var(--ad);display:flex;align-items:center;justify-content:center;margin-bottom:20px">
          <svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" style="width:24px;height:24px"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        </div>
        <h3 style="margin-bottom:10px">Payments</h3>
        <p>Crypto and fiat payment gateways, cross-border remittance platforms, and merchant processing solutions with multi-currency support.</p>
      </div>
      <div class="svc-card" style="padding:32px">
        <div style="width:52px;height:52px;border-radius:14px;background:var(--pd);display:flex;align-items:center;justify-content:center;margin-bottom:20px">
          <svg viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="2" stroke-linecap="round" style="width:24px;height:24px"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>
        </div>
        <h3 style="margin-bottom:10px">Enterprise Blockchain</h3>
        <p>Private and consortium blockchain networks, supply chain traceability, tokenization platforms, and smart contract automation for enterprises.</p>
      </div>
    </div>
  </div>
</section>

'''

recognition_marker = b'<!-- Recognition -->'
c = c.replace(recognition_marker, industries_html + recognition_marker)

with open('portfolio/index.html', 'wb') as f:
    f.write(c)
print('portfolio done')

# ── blog/index.html ──────────────────────────────────────────────────────────
with open('blog/index.html', 'rb') as f:
    c = f.read()

old_grid_end = b'<div class="blog-card"><div class="blog-thumb"><img src="https://images.pexels.com/photos/6802042/pexels-photo-6802042.jpeg?auto=compress&cs=tinysrgb&w=600" alt="Grid Trading" loading="lazy"></div><div class="blog-body"><span class="blog-tag">Trading Bots</span><h3>Grid Trading Bots: How to Profit in Sideways Markets</h3><p>A practical guide to grid trading strategy, parameter optimization, and risk management for volatile crypto markets.</p><div class="blog-meta"><span>Oct 25, 2024</span><span>8 min read</span></div></div></div>'

new_grid_end = old_grid_end + b'''
      <div class="blog-card"><div class="blog-thumb"><img src="https://images.pexels.com/photos/3184291/pexels-photo-3184291.jpeg?auto=compress&cs=tinysrgb&w=700" alt="White-Label Crypto Exchange" loading="lazy"></div><div class="blog-body"><span class="blog-tag">Crypto Exchange</span><h3>How to Launch a White-Label Crypto Exchange in 30 Days</h3><p>A step-by-step breakdown of how modern white-label solutions let you go from idea to live exchange in under a month &#8212; without sacrificing security or compliance.</p><div class="blog-meta"><span>Oct 18, 2024</span><span>10 min read</span></div></div></div>
      <div class="blog-card"><div class="blog-thumb"><img src="https://images.pexels.com/photos/3943716/pexels-photo-3943716.jpeg?auto=compress&cs=tinysrgb&w=700" alt="KYC AML Guide" loading="lazy"></div><div class="blog-body"><span class="blog-tag">Fintech</span><h3>The Complete Guide to KYC/AML for Fintech Startups</h3><p>Everything founders need to know about Know Your Customer and Anti-Money Laundering requirements &#8212; from choosing a provider to building compliant onboarding flows.</p><div class="blog-meta"><span>Oct 10, 2024</span><span>9 min read</span></div></div></div>
      <div class="blog-card"><div class="blog-thumb"><img src="https://images.pexels.com/photos/546819/pexels-photo-546819.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Smart Contract Security" loading="lazy"></div><div class="blog-body"><span class="blog-tag">Blockchain</span><h3>Smart Contract Security: Top 10 Vulnerabilities to Avoid</h3><p>From reentrancy attacks to integer overflows &#8212; a deep dive into the most common smart contract vulnerabilities and how to protect your protocol before launch.</p><div class="blog-meta"><span>Oct 3, 2024</span><span>11 min read</span></div></div></div>'''

if old_grid_end in c:
    c = c.replace(old_grid_end, new_grid_end)
    with open('blog/index.html', 'wb') as f:
        f.write(c)
    print('blog done')
else:
    print('blog: old_grid_end NOT FOUND')
    idx = c.find(b'Grid Trading')
    print(repr(c[idx:idx+200]))
