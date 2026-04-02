with open('index.html', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8', errors='replace')

# Find where hero ends (</section> before <!-- Testimonials -->)
testi_idx = content.find('<!-- Testimonials -->')
if testi_idx == -1:
    print('Cannot find Testimonials marker')
    exit()

# Find the </section> just before Testimonials
insert_at = content.rfind('</section>', 0, testi_idx) + len('</section>')
print(f'Inserting at position {insert_at}')
print('Context:', repr(content[insert_at:insert_at+50]))

missing_sections = '''

<!-- Stats -->
<div class="stats-row counter-section">
  <div class="stat-cell"><div class="stat-num" data-target="120" data-suffix="+">120+</div><p>Projects Delivered</p></div>
  <div class="stat-cell"><div class="stat-num" data-target="40" data-suffix="+">40+</div><p>Countries Served</p></div>
  <div class="stat-cell"><div class="stat-num" data-target="8" data-suffix="+">8+</div><p>Years in Fintech</p></div>
  <div class="stat-cell"><div class="stat-num" data-target="98" data-suffix="%">98%</div><p>Client Satisfaction</p></div>
</div>

<!-- Services -->
<section class="section" id="services">
  <div class="container">
    <div class="text-center reveal">
      <span class="eyebrow">What We Build</span>
      <h2>Full-Spectrum <span class="grad-text">Fintech & Blockchain</span></h2>
      <div class="section-divider"></div>
      <p class="section-desc" style="margin-top:16px">From crypto exchanges to AI trading bots, neobanks to DeFi protocols — we engineer the financial infrastructure of tomorrow.</p>
    </div>
    <div class="svc-grid reveal-stagger">
      <div class="svc-card tilt-card glow-card">
        <div class="svc-img"><img src="https://images.pexels.com/photos/8358141/pexels-photo-8358141.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Blockchain" loading="lazy"><div class="svc-img-overlay"></div></div>
        <div class="svc-body"><h3>Blockchain Development</h3><p>Smart contracts, DeFi protocols, NFT platforms, cross-chain bridges, and enterprise blockchain networks — audited and production-ready.</p><a href="services/blockchain/" class="svc-link hover-underline">Explore <svg viewBox="0 0 14 14" fill="none"><path d="M1 7h12M7 1l6 6-6 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div>
      </div>
      <div class="svc-card tilt-card glow-card">
        <div class="svc-img"><img src="https://images.pexels.com/photos/844124/pexels-photo-844124.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Crypto Exchange" loading="lazy"><div class="svc-img-overlay"></div></div>
        <div class="svc-body"><h3>Crypto Exchange Platforms</h3><p>CEX, DEX, P2P, hybrid, and white-label exchange platforms — built for performance, compliance, and scale from day one.</p><a href="services/crypto-exchange/" class="svc-link hover-underline">Explore <svg viewBox="0 0 14 14" fill="none"><path d="M1 7h12M7 1l6 6-6 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div>
      </div>
      <div class="svc-card tilt-card glow-card">
        <div class="svc-img"><img src="https://images.pexels.com/photos/6801648/pexels-photo-6801648.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Trading Bots" loading="lazy"><div class="svc-img-overlay"></div></div>
        <div class="svc-body"><h3>Trading Bot Development</h3><p>Arbitrage, DCA, grid, sniper, and AI/ML bots — intelligent automated trading systems that optimize tactics and reduce risk.</p><a href="services/trading-bots/" class="svc-link hover-underline">Explore <svg viewBox="0 0 14 14" fill="none"><path d="M1 7h12M7 1l6 6-6 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div>
      </div>
      <div class="svc-card tilt-card glow-card">
        <div class="svc-img"><img src="https://images.pexels.com/photos/3943716/pexels-photo-3943716.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Fintech" loading="lazy"><div class="svc-img-overlay"></div></div>
        <div class="svc-body"><h3>Digital Banking &amp; Neobanking</h3><p>Full-stack neobank apps with accounts, cards, lending, savings, and investment features — compliant and beautifully designed.</p><a href="services/fintech/" class="svc-link hover-underline">Explore <svg viewBox="0 0 14 14" fill="none"><path d="M1 7h12M7 1l6 6-6 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div>
      </div>
      <div class="svc-card tilt-card glow-card">
        <div class="svc-img"><img src="https://images.pexels.com/photos/5698696/pexels-photo-5698696.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Wallets" loading="lazy"><div class="svc-img-overlay"></div></div>
        <div class="svc-body"><h3>Crypto Wallet Development</h3><p>MPC, custodial, non-custodial, and DeFi wallets — secure digital wallets that facilitate quick and safe transactions globally.</p><a href="services/wallets/" class="svc-link hover-underline">Explore <svg viewBox="0 0 14 14" fill="none"><path d="M1 7h12M7 1l6 6-6 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div>
      </div>
      <div class="svc-card tilt-card glow-card">
        <div class="svc-img"><img src="https://images.pexels.com/photos/6770610/pexels-photo-6770610.jpeg?auto=compress&cs=tinysrgb&w=700" alt="Forex" loading="lazy"><div class="svc-img-overlay"></div></div>
        <div class="svc-body"><h3>Forex CRM &amp; Trading Solutions</h3><p>CRM, back-office, traders room, MT4/MT5 integration, and MAM/PAMM systems — everything a modern broker needs to compete.</p><a href="services/forex/" class="svc-link hover-underline">Explore <svg viewBox="0 0 14 14" fill="none"><path d="M1 7h12M7 1l6 6-6 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div>
      </div>
    </div>
  </div>
</section>

<!-- Solutions -->
<section class="section" style="background:var(--bg2)" id="solutions">
  <div class="container">
    <div class="text-center reveal">
      <span class="eyebrow">Solutions</span>
      <h2>Explore Our <span class="grad-text2">Solution Suite</span></h2>
      <div class="section-divider"></div>
    </div>
    <div class="sol-tabs reveal">
      <button class="sol-tab active" onclick="showSol('exchange',this)">Exchange</button>
      <button class="sol-tab" onclick="showSol('trading',this)">Trading</button>
      <button class="sol-tab" onclick="showSol('payments',this)">Payments</button>
      <button class="sol-tab" onclick="showSol('banking',this)">Banking</button>
      <button class="sol-tab" onclick="showSol('forex',this)">Forex</button>
    </div>
    <div id="sol-exchange" class="sol-panel active">
      <div class="sol-card"><div class="sol-card-img"><img src="https://images.pexels.com/photos/844124/pexels-photo-844124.jpeg?auto=compress&cs=tinysrgb&w=500" alt="CEX" loading="lazy"></div><div class="sol-card-body"><h4>Centralized Exchange (CEX)</h4><p>High-performance order matching, KYC/AML, admin panel, and institutional-grade liquidity management.</p><a href="services/crypto-exchange/">Learn more</a></div></div>
      <div class="sol-card"><div class="sol-card-img"><img src="https://images.pexels.com/photos/7567443/pexels-photo-7567443.jpeg?auto=compress&cs=tinysrgb&w=500" alt="DEX" loading="lazy"></div><div class="sol-card-body"><h4>Decentralized Exchange (DEX)</h4><p>AMM-based DEX with smart contract liquidity pools, yield farming, and governance token integration.</p><a href="services/crypto-exchange/">Learn more</a></div></div>
      <div class="sol-card"><div class="sol-card-img"><img src="https://images.pexels.com/photos/6802042/pexels-photo-6802042.jpeg?auto=compress&cs=tinysrgb&w=500" alt="P2P" loading="lazy"></div><div class="sol-card-body"><h4>P2P Exchange</h4><p>Peer-to-peer trading with escrow, dispute resolution, reputation system, and 100+ payment methods.</p><a href="services/crypto-exchange/">Learn more</a></div></div>
    </div>
    <div id="sol-trading" class="sol-panel">
      <div class="sol-card"><div class="sol-card-img"><img src="https://images.pexels.com/photos/6801648/pexels-photo-6801648.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Algo" loading="lazy"></div><div class="sol-card-body"><h4>Algo Trading Software</h4><p>Rule-based and AI-driven algorithmic trading systems for crypto, forex, and equity markets.</p><a href="services/trading-bots/">Learn more</a></div></div>
      <div class="sol-card"><div class="sol-card-img"><img src="https://images.pexels.com/photos/8185624/pexels-photo-8185624.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Arbitrage" loading="lazy"></div><div class="sol-card-body"><h4>Arbitrage Bots</h4><p>Cross-exchange and triangular arbitrage bots that capture price inefficiencies in milliseconds.</p><a href="services/trading-bots/">Learn more</a></div></div>
      <div class="sol-card"><div class="sol-card-img"><img src="https://images.pexels.com/photos/6777571/pexels-photo-6777571.jpeg?auto=compress&cs=tinysrgb&w=500" alt="DCA" loading="lazy"></div><div class="sol-card-body"><h4>DCA &amp; Grid Bots</h4><p>Dollar-cost averaging and grid trading bots with smart entry/exit logic and portfolio rebalancing.</p><a href="services/trading-bots/">Learn more</a></div></div>
    </div>
    <div id="sol-payments" class="sol-panel">
      <div class="sol-card"><div class="sol-card-img"><img src="https://images.pexels.com/photos/4386370/pexels-photo-4386370.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Gateway" loading="lazy"></div><div class="sol-card-body"><h4>Crypto Payment Gateway</h4><p>Accept 100+ cryptocurrencies with instant settlement, fiat conversion, and zero chargebacks.</p><a href="solutions/payment-gateway/">Learn more</a></div></div>
      <div class="sol-card"><div class="sol-card-img"><img src="https://images.pexels.com/photos/6770520/pexels-photo-6770520.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Ecommerce" loading="lazy"></div><div class="sol-card-body"><h4>E-Commerce Integration</h4><p>Plug-and-play crypto payments for Shopify, WooCommerce, Magento, and custom platforms.</p><a href="solutions/payment-gateway/">Learn more</a></div></div>
      <div class="sol-card"><div class="sol-card-img"><img src="https://images.pexels.com/photos/3943723/pexels-photo-3943723.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Cross Border" loading="lazy"></div><div class="sol-card-body"><h4>Cross-Border Payments</h4><p>Instant, low-cost international transfers powered by blockchain rails across 180+ countries.</p><a href="solutions/payment-gateway/">Learn more</a></div></div>
    </div>
    <div id="sol-banking" class="sol-panel">
      <div class="sol-card"><div class="sol-card-img"><img src="https://images.pexels.com/photos/3943716/pexels-photo-3943716.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Neobank" loading="lazy"></div><div class="sol-card-body"><h4>Neobank Platform</h4><p>Full-stack digital banking with accounts, virtual cards, lending, savings, and investment features.</p><a href="solutions/neobank/">Learn more</a></div></div>
      <div class="sol-card"><div class="sol-card-img"><img src="https://images.pexels.com/photos/4386431/pexels-photo-4386431.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Digital Banking" loading="lazy"></div><div class="sol-card-body"><h4>Digital Banking App</h4><p>Mobile-first banking apps with biometric auth, real-time notifications, and open banking APIs.</p><a href="solutions/neobank/">Learn more</a></div></div>
      <div class="sol-card"><div class="sol-card-img"><img src="https://images.pexels.com/photos/3184291/pexels-photo-3184291.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Fintech" loading="lazy"></div><div class="sol-card-body"><h4>Fintech Software</h4><p>Compliance-ready fintech platforms with KYC, AML, and regulatory reporting built in from day one.</p><a href="services/fintech/">Learn more</a></div></div>
    </div>
    <div id="sol-forex" class="sol-panel">
      <div class="sol-card"><div class="sol-card-img"><img src="https://images.pexels.com/photos/6770610/pexels-photo-6770610.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Forex CRM" loading="lazy"></div><div class="sol-card-body"><h4>Forex CRM</h4><p>Complete broker CRM with IB management, lead tracking, KYC, and compliance tools.</p><a href="services/forex/">Learn more</a></div></div>
      <div class="sol-card"><div class="sol-card-img"><img src="https://images.pexels.com/photos/6802042/pexels-photo-6802042.jpeg?auto=compress&cs=tinysrgb&w=500" alt="Back Office" loading="lazy"></div><div class="sol-card-body"><h4>Back Office &amp; Traders Room</h4><p>Full back-office suite with reporting, and client management for forex brokerages.</p><a href="services/forex/">Learn more</a></div></div>
      <div class="sol-card"><div class="sol-card-img"><img src="https://images.pexels.com/photos/8358141/pexels-photo-8358141.jpeg?auto=compress&cs=tinysrgb&w=500" alt="MT4 MT5" loading="lazy"></div><div class="sol-card-body"><h4>MT4/MT5 Integration</h4><p>Custom plugins, liquidity bridges, and CRM connectors for MetaTrader platforms.</p><a href="services/forex/">Learn more</a></div></div>
    </div>
  </div>
</section>

<!-- Why PumaPulse -->
<section class="section">
  <div class="container">
    <div class="text-center reveal">
      <span class="eyebrow">Why Choose Us</span>
      <h2>We Don't Just Build Software <span class="grad-text">We Build Businesses</span></h2>
      <div class="section-divider"></div>
    </div>
    <div class="why-grid reveal-stagger" style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:48px">
      <div class="why-item" style="padding:28px;border-radius:16px;border:1px solid var(--border)">
        <div style="width:48px;height:48px;border-radius:12px;background:var(--ad);display:flex;align-items:center;justify-content:center;margin-bottom:16px"><svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" style="width:22px;height:22px"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
        <h4 style="margin-bottom:8px">Security First</h4><p style="font-size:0.87rem">Every product ships with multi-layer security, HSM key management, and third-party audits.</p>
      </div>
      <div class="why-item" style="padding:28px;border-radius:16px;border:1px solid var(--border)">
        <div style="width:48px;height:48px;border-radius:12px;background:var(--pd);display:flex;align-items:center;justify-content:center;margin-bottom:16px"><svg viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="2" style="width:22px;height:22px"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg></div>
        <h4 style="margin-bottom:8px">Fast Delivery</h4><p style="font-size:0.87rem">Pre-built modules and agile process let us ship production-ready products in weeks, not months.</p>
      </div>
      <div class="why-item" style="padding:28px;border-radius:16px;border:1px solid var(--border)">
        <div style="width:48px;height:48px;border-radius:12px;background:var(--vd);display:flex;align-items:center;justify-content:center;margin-bottom:16px"><svg viewBox="0 0 24 24" fill="none" stroke="#7c3aed" stroke-width="2" style="width:22px;height:22px"><path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg></div>
        <h4 style="margin-bottom:8px">Compliance Built-In</h4><p style="font-size:0.87rem">KYC, AML, and regulatory requirements built into every product from the ground up.</p>
      </div>
      <div class="why-item" style="padding:28px;border-radius:16px;border:1px solid var(--border)">
        <div style="width:48px;height:48px;border-radius:12px;background:rgba(245,158,11,0.12);display:flex;align-items:center;justify-content:center;margin-bottom:16px"><svg viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2" style="width:22px;height:22px"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/></svg></div>
        <h4 style="margin-bottom:8px">On-Time Delivery</h4><p style="font-size:0.87rem">We respect your timeline. Milestones are hit, scope is controlled, no surprises.</p>
      </div>
      <div class="why-item" style="padding:28px;border-radius:16px;border:1px solid var(--border)">
        <div style="width:48px;height:48px;border-radius:12px;background:var(--ad);display:flex;align-items:center;justify-content:center;margin-bottom:16px"><svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" style="width:22px;height:22px"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg></div>
        <h4 style="margin-bottom:8px">Performance Obsessed</h4><p style="font-size:0.87rem">We benchmark everything — from matching engine TPS to API response times.</p>
      </div>
      <div class="why-item" style="padding:28px;border-radius:16px;border:1px solid var(--border)">
        <div style="width:48px;height:48px;border-radius:12px;background:var(--pd);display:flex;align-items:center;justify-content:center;margin-bottom:16px"><svg viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="2" style="width:22px;height:22px"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <h4 style="margin-bottom:8px">Dedicated Support</h4><p style="font-size:0.87rem">Post-launch SLA-backed support, monitoring, and continuous improvement — we don't disappear.</p>
      </div>
    </div>
  </div>
</section>

<!-- How We Work -->
<section class="section" style="background:var(--bg2)">
  <div class="container">
    <div class="text-center reveal">
      <span class="eyebrow">Our Process</span>
      <h2>How We Turn Ideas Into <span class="grad-text3">Shipped Products</span></h2>
      <div class="section-divider"></div>
    </div>
    <div class="process-row reveal-stagger" style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:48px;position:relative">
      <div style="text-align:center;padding:28px 20px;background:var(--card);border:1px solid var(--border);border-radius:16px">
        <div style="width:52px;height:52px;border-radius:50%;background:var(--grad);display:flex;align-items:center;justify-content:center;margin:0 auto 16px;font-size:1.1rem;font-weight:800;color:#fff">1</div>
        <h4 style="margin-bottom:8px">Discovery</h4><p style="font-size:0.85rem">We deep-dive into your requirements, market, and technical constraints to define the right architecture.</p>
      </div>
      <div style="text-align:center;padding:28px 20px;background:var(--card);border:1px solid var(--border);border-radius:16px">
        <div style="width:52px;height:52px;border-radius:50%;background:var(--grad2);display:flex;align-items:center;justify-content:center;margin:0 auto 16px;font-size:1.1rem;font-weight:800;color:#fff">2</div>
        <h4 style="margin-bottom:8px">Design &amp; Plan</h4><p style="font-size:0.85rem">UI/UX design, technical specs, and project roadmap — all reviewed and approved before a line of code is written.</p>
      </div>
      <div style="text-align:center;padding:28px 20px;background:var(--card);border:1px solid var(--border);border-radius:16px">
        <div style="width:52px;height:52px;border-radius:50%;background:var(--grad3);display:flex;align-items:center;justify-content:center;margin:0 auto 16px;font-size:1.1rem;font-weight:800;color:#fff">3</div>
        <h4 style="margin-bottom:8px">Build &amp; Test</h4><p style="font-size:0.85rem">Agile sprints with weekly demos, continuous integration, automated testing, and security audits throughout.</p>
      </div>
      <div style="text-align:center;padding:28px 20px;background:var(--card);border:1px solid var(--border);border-radius:16px">
        <div style="width:52px;height:52px;border-radius:50%;background:var(--grad);display:flex;align-items:center;justify-content:center;margin:0 auto 16px;font-size:1.1rem;font-weight:800;color:#fff">4</div>
        <h4 style="margin-bottom:8px">Launch &amp; Scale</h4><p style="font-size:0.85rem">Production deployment, performance tuning, and ongoing support — we stay with you after go-live.</p>
      </div>
    </div>
  </div>
</section>

'''

fixed = content[:insert_at] + missing_sections + content[insert_at:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(fixed)
print('Done! Added', len(missing_sections), 'chars of missing sections')
