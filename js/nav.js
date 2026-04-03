/* PumaPulse — Shared nav/footer injector v4 */
(function() {
  var path = window.location.pathname;
  var depth = (path.match(/\//g) || []).length - 1;
  // services/blockchain/ or solutions/defi/ = depth 2 → ../../
  // about/ blog/ careers/ etc = depth 1 → ../
  // root = depth 0 → ''
  var base = depth >= 2 ? '../../' : depth === 1 ? '../' : '';
  var home = depth >= 2 ? '../../' : depth === 1 ? '../' : '/';

  /* ── NAVBAR ── */
  var navHTML = '<nav class="navbar" id="navbar"><div class="navbar-inner">'
    + '<a href="' + home + '" class="nav-logo"><img src="' + base + 'img/logo.png" alt="PumaPulse"></a>'
    + '<ul class="nav-links" id="navLinks">'

    /* Services mega menu */
    + '<li class="dropdown"><a href="#">Services</a>'
    + '<div class="mega-menu" style="width:760px">'
    + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:6px">'
    + '<a href="' + base + 'services/blockchain/" class="mega-item"><div class="mega-icon" style="background:rgba(98,126,234,0.12)"><img src="https://cdn.simpleicons.org/ethereum/627EEA" alt="Blockchain"></div><div><span class="mega-text-label">Blockchain Development</span><span class="mega-text-desc">Smart contracts, DeFi protocols, NFT platforms &amp; enterprise blockchain</span></div></a>'
    + '<a href="' + base + 'services/crypto-exchange/" class="mega-item"><div class="mega-icon" style="background:rgba(247,147,26,0.12)"><img src="https://cdn.simpleicons.org/bitcoin/F7931A" alt="Exchange"></div><div><span class="mega-text-label">Crypto Exchange</span><span class="mega-text-desc">CEX, DEX, P2P, hybrid &amp; white-label exchange platforms</span></div></a>'
    + '<a href="' + base + 'services/trading-bots/" class="mega-item"><div class="mega-icon" style="background:rgba(16,185,129,0.12)"><img src="https://cdn.simpleicons.org/python/3776AB" alt="Bots"></div><div><span class="mega-text-label">Trading Bots</span><span class="mega-text-desc">Arbitrage, DCA, grid, sniper, signal &amp; AI/ML trading bots</span></div></a>'
    + '<a href="' + base + 'services/fintech/" class="mega-item"><div class="mega-icon" style="background:rgba(99,91,255,0.12)"><img src="https://cdn.simpleicons.org/stripe/635BFF" alt="Fintech"></div><div><span class="mega-text-label">Fintech Solutions</span><span class="mega-text-desc">Neobank apps, digital banking, KYC/AML &amp; lending platforms</span></div></a>'
    + '<a href="' + base + 'services/wallets/" class="mega-item"><div class="mega-icon" style="background:rgba(20,241,149,0.12)"><img src="https://cdn.simpleicons.org/solana/9945FF" alt="Wallets"></div><div><span class="mega-text-label">Wallet Development</span><span class="mega-text-desc">MPC, DeFi, custodial, non-custodial &amp; multi-currency wallets</span></div></a>'
    + '<a href="' + base + 'services/forex/" class="mega-item"><div class="mega-icon" style="background:rgba(0,174,239,0.12)"><svg viewBox="0 0 24 24" fill="none" stroke="#00AEEF" stroke-width="2" stroke-linecap="round"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg></div><div><span class="mega-text-label">Forex Solutions</span><span class="mega-text-desc">Forex CRM, back office, MT4/MT5 integration &amp; traders room</span></div></a>'
    + '</div>'
    + '<div class="mega-menu-footer"><a href="' + base + 'portfolio/">View all case studies →</a></div>'
    + '</div></li>'

    /* Solutions mega menu */
    + '<li class="dropdown"><a href="#">Solutions</a>'
    + '<div class="mega-menu" style="width:680px">'
    + '<div class="mega-menu-header">Financial Technology Solutions</div>'
    + '<div class="mega-menu-grid">'
    + '<a href="' + base + 'solutions/defi/" class="mega-item"><div class="mega-icon" style="background:rgba(99,102,241,0.12)"><img src="https://cdn.simpleicons.org/ethereum/627EEA" alt="DeFi"></div><div><span class="mega-text-label">DeFi Platforms</span><span class="mega-text-desc">AMMs, lending protocols, yield aggregators &amp; cross-chain bridges</span></div></a>'
    + '<a href="' + base + 'solutions/neobank/" class="mega-item"><div class="mega-icon" style="background:rgba(16,185,129,0.12)"><svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round"><rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/></svg></div><div><span class="mega-text-label">Neobank</span><span class="mega-text-desc">Full-stack digital banking with cards, lending &amp; investments</span></div></a>'
    + '<a href="' + base + 'solutions/payment-gateway/" class="mega-item"><div class="mega-icon" style="background:rgba(59,130,246,0.12)"><img src="https://cdn.simpleicons.org/bitcoin/F7931A" alt="Payments"></div><div><span class="mega-text-label">Payment Gateway</span><span class="mega-text-desc">Accept 100+ cryptocurrencies with instant settlement</span></div></a>'
    + '<a href="' + base + 'solutions/ai-trading/" class="mega-item"><div class="mega-icon" style="background:rgba(167,139,250,0.12)"><img src="https://cdn.simpleicons.org/tensorflow/FF6F00" alt="AI Trading"></div><div><span class="mega-text-label">AI Trading</span><span class="mega-text-desc">ML price prediction, sentiment analysis &amp; smart order routing</span></div></a>'
    + '</div>'
    + '<div class="mega-menu-footer"><a href="' + base + 'portfolio/">View all case studies →</a><a href="' + base + 'contact/" class="mega-cta"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81a19.79 19.79 0 01-3.07-8.67A2 2 0 012 .18h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92z"/></svg>Free Consultation</a></div>'
    + '</div></li>'

    + '<li><a href="' + base + 'about/">About</a></li>'
    + '<li><a href="' + base + 'portfolio/">Portfolio</a></li>'
    + '<li><a href="' + base + 'blog/">Blog</a></li>'
    + '<li><a href="' + base + 'careers/">Careers</a></li>'
    + '<li><a href="' + base + 'contact/">Contact</a></li>'
    + '</ul>'
    + '<div class="nav-cta" id="navCta"><a href="' + base + 'contact/" class="btn btn-accent btn-sm">Get a Free Quote</a></div>'
    + '<div class="hamburger" id="hamburger"><span></span><span></span><span></span></div>'
    + '</div></nav>';

  /* ── FOOTER ── */
  var footerHTML = '<footer>'
    + '<div class="footer-top"><div class="container"><div class="footer-top-inner">'
    + '<div class="footer-brand-new">'
    + '<a href="' + home + '" class="nav-logo"><img src="' + base + 'img/logo.png" alt="PumaPulse"></a>'
    + '<p class="tagline">PumaPulse offers digital transformation solutions that help your business grow and adapt. We simplify complex tech and help startups and entrepreneurs succeed with smart, customized solutions.</p>'
    + '</div>'
    + '<div class="footer-col-new"><h5>Services</h5><ul>'
    + '<li><a href="' + base + 'services/blockchain/">Blockchain Dev</a></li>'
    + '<li><a href="' + base + 'services/crypto-exchange/">Crypto Exchange</a></li>'
    + '<li><a href="' + base + 'services/trading-bots/">Trading Bots</a></li>'
    + '<li><a href="' + base + 'services/wallets/">Wallet Dev</a></li>'
    + '<li><a href="' + base + 'services/fintech/">Fintech Apps</a></li>'
    + '<li><a href="' + base + 'services/forex/">Forex Solutions</a></li>'
    + '</ul></div>'
    + '<div class="footer-col-new"><h5>Solutions</h5><ul>'
    + '<li><a href="' + base + 'solutions/defi/">DeFi Platforms</a></li>'
    + '<li><a href="' + base + 'solutions/neobank/">Neobank</a></li>'
    + '<li><a href="' + base + 'solutions/payment-gateway/">Payment Gateway</a></li>'
    + '<li><a href="' + base + 'solutions/ai-trading/">AI Trading</a></li>'
    + '<li><a href="' + base + 'portfolio/">Portfolio</a></li>'
    + '</ul></div>'
    + '<div class="footer-col-new"><h5>Company</h5><ul>'
    + '<li><a href="' + base + 'about/">About Us</a></li>'
    + '<li><a href="' + base + 'blog/">Blog</a></li>'
    + '<li><a href="' + base + 'careers/">Careers</a></li>'
    + '<li><a href="' + base + 'contact/">Contact</a></li>'
    + '<li><a href="' + base + 'privacy/">Privacy Policy</a></li>'
    + '<li><a href="' + base + 'terms/">Terms of Service</a></li>'
    + '</ul></div>'
    + '<div class="footer-col-new"><h5>Resources</h5><ul>'
    + '<li><a href="' + base + 'blog/">Insights &amp; Trends</a></li>'
    + '<li><a href="' + base + 'portfolio/">Case Studies</a></li>'
    + '<li><a href="' + base + 'contact/">Free Consultation</a></li>'
    + '<li><a href="' + base + 'careers/">Open Positions</a></li>'
    + '</ul></div>'
    + '</div></div></div>'
    + '<div class="container"><div class="footer-bottom-bar">'
    + '<p>© 2025 PumaPulse Infoservices Private Limited. All Rights Reserved.</p>'
    + '<div class="footer-contact-mini">'
    + '<a href="mailto:sales@pumapulse.org"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>sales@pumapulse.org</a>'
    + '<a href="tel:+16815534010"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81a19.79 19.79 0 01-3.07-8.67A2 2 0 012 .18h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92z"/></svg>+1 (681) 553-4010</a>'
    + '<a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>43 King St W, Toronto, Canada</a>'
    + '</div>'
    + '</div></div>'
    + '</footer>';

  /* ── Inject ── */
  var navEl = document.getElementById('nav-placeholder');
  if (navEl) navEl.outerHTML = navHTML;
  var footerEl = document.getElementById('footer-placeholder');
  if (footerEl) footerEl.outerHTML = footerHTML;

  /* ── Wire navbar scroll + hamburger ── */
  setTimeout(function() {
    var nb = document.querySelector('.navbar');
    if (nb) {
      window.addEventListener('scroll', function() {
        nb.classList.toggle('scrolled', window.scrollY > 30);
      }, { passive: true });
      if (window.scrollY > 30) nb.classList.add('scrolled');
    }
    var hb = document.querySelector('.hamburger');
    if (hb && !hb.dataset.wired) {
      hb.dataset.wired = '1';
      hb.addEventListener('click', function() {
        document.body.classList.toggle('nav-mobile-open');
        hb.classList.toggle('open');
      });
    }
  }, 0);
})();
