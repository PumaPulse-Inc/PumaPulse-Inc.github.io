import re

with open('services/crypto-exchange/index.html', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8', errors='replace')

new_section = '''        <span class="eyebrow">Core Features</span>
        <h2>Exchange Infrastructure <span class="grad-text">Built to Win</span></h2>
        <div class="section-divider" style="margin:0 0 24px"></div>
        <p style="margin-bottom:28px">Every exchange we build ships with enterprise-grade infrastructure covering the full trading lifecycle — from order placement to settlement, compliance, and liquidity management.</p>
        <div class="service-feature-list">
          <div class="sfeat"><div class="sfeat-icon" style="background:rgba(16,185,129,0.12)"><svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg></div><div><h4>1M+ TPS Matching Engine</h4><p>In-memory order book with sub-millisecond execution, price-time priority, partial fills, stop-loss, take-profit, and iceberg orders.</p></div></div>
          <div class="sfeat"><div class="sfeat-icon" style="background:rgba(59,130,246,0.12)"><svg viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="2" stroke-linecap="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div><div><h4>HSM-Backed Cold Storage</h4><p>Multi-sig treasury, hot/warm/cold wallet tiering, automated sweeping, DDoS protection, and real-time anomaly detection.</p></div></div>
          <div class="sfeat"><div class="sfeat-icon" style="background:rgba(167,139,250,0.12)"><svg viewBox="0 0 24 24" fill="none" stroke="#a78bfa" stroke-width="2" stroke-linecap="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg></div><div><h4>Deep Liquidity Integration</h4><p>Built-in liquidity aggregation from top-tier providers, market maker APIs, and cross-exchange bridges for tight spreads from day one.</p></div></div>
          <div class="sfeat"><div class="sfeat-icon" style="background:rgba(16,185,129,0.12)"><svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round"><path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg></div><div><h4>Global Compliance Ready</h4><p>Automated KYC/AML, FATF Travel Rule, SAR reporting, and 30+ jurisdiction support — launch compliant from day one.</p></div></div>
        </div>'''

# Replace from eyebrow "Core Features" to end of service-feature-list
fixed = re.sub(
    r'<span class="eyebrow">Core Features</span>[\s\S]*?</div>\s*</div>\s*</div>',
    new_section + '\n        </div>\n      </div>',
    content, count=1
)

if fixed != content:
    with open('services/crypto-exchange/index.html', 'w', encoding='utf-8') as f:
        f.write(fixed)
    print('Fixed exchange section')
else:
    print('Pattern not matched')
