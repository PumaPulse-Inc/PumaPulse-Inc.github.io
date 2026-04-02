import re

# ── careers/index.html ───────────────────────────────────────────────────────
with open('careers/index.html', 'rb') as f:
    c = f.read()

# Add "Why Work Here" section before the open-roles section
why_work_here = b'''
<!-- Why Work Here -->
<section class="section">
  <div class="container">
    <div class="text-center reveal">
      <span class="eyebrow">Why PumaPulse</span>
      <h2>Four Reasons to <span class="grad-text">Join Our Team</span></h2>
      <div class="section-divider"></div>
    </div>
    <div class="svc-grid reveal-stagger" style="grid-template-columns:repeat(4,1fr);margin-top:48px">
      <div class="svc-card" style="padding:32px;text-align:center">
        <div style="width:56px;height:56px;border-radius:16px;background:var(--ad);display:flex;align-items:center;justify-content:center;margin:0 auto 20px">
          <svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" style="width:26px;height:26px"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
        </div>
        <h3 style="margin-bottom:10px">Remote-First</h3>
        <p>Work from anywhere in the world. We&#39;re a distributed team across 18+ countries and we&#39;ve built our culture around async-first collaboration.</p>
      </div>
      <div class="svc-card" style="padding:32px;text-align:center">
        <div style="width:56px;height:56px;border-radius:16px;background:var(--pd);display:flex;align-items:center;justify-content:center;margin:0 auto 20px">
          <svg viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="2" stroke-linecap="round" style="width:26px;height:26px"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
        </div>
        <h3 style="margin-bottom:10px">Competitive Pay</h3>
        <p>Salaries benchmarked to the top 10% of market, plus equity participation, performance bonuses, and a $1,500 home office setup budget.</p>
      </div>
      <div class="svc-card" style="padding:32px;text-align:center">
        <div style="width:56px;height:56px;border-radius:16px;background:var(--vd);display:flex;align-items:center;justify-content:center;margin:0 auto 20px">
          <svg viewBox="0 0 24 24" fill="none" stroke="#7c3aed" stroke-width="2" stroke-linecap="round" style="width:26px;height:26px"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
        </div>
        <h3 style="margin-bottom:10px">Learning Budget</h3>
        <p>$2,000 per year for courses, certifications, conferences, and books. We invest in your growth because your expertise makes us better.</p>
      </div>
      <div class="svc-card" style="padding:32px;text-align:center">
        <div style="width:56px;height:56px;border-radius:16px;background:rgba(245,158,11,0.12);display:flex;align-items:center;justify-content:center;margin:0 auto 20px">
          <svg viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2" stroke-linecap="round" style="width:26px;height:26px"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
        </div>
        <h3 style="margin-bottom:10px">Real Impact</h3>
        <p>Your code ships to real users processing millions in transactions. No bureaucracy, no busywork &#8212; just meaningful work that moves the needle.</p>
      </div>
    </div>
  </div>
</section>

'''

open_roles_marker = b'<!-- Open Roles -->'
c = c.replace(open_roles_marker, why_work_here + open_roles_marker)

# Add 3 more job listings to reach 8+ (currently has 9 but let's add Security Engineer, Mobile Engineer, Compliance)
# Find the last job card before the dept Business label and add after DevOps
old_devops = b'<div class="job-card"><div class="job-info"><h4>DevOps / Infrastructure Engineer</h4><div class="job-tags"><span class="jtag jtag-dept">Engineering</span><span class="jtag jtag-type">Full-time</span><span class="jtag jtag-loc">Remote</span></div></div><a href="#apply" class="btn btn-outline btn-sm">Apply Now</a></div>'
new_devops = old_devops + b'''
      <div class="job-card"><div class="job-info"><h4>Security Engineer &#8212; Blockchain &amp; Smart Contracts</h4><div class="job-tags"><span class="jtag jtag-dept">Engineering</span><span class="jtag jtag-type">Full-time</span><span class="jtag jtag-loc">Remote</span></div></div><a href="#apply" class="btn btn-outline btn-sm">Apply Now</a></div>
      <div class="job-card"><div class="job-info"><h4>Mobile Engineer (React Native / Flutter)</h4><div class="job-tags"><span class="jtag jtag-dept">Engineering</span><span class="jtag jtag-type">Full-time</span><span class="jtag jtag-loc">Remote</span></div></div><a href="#apply" class="btn btn-outline btn-sm">Apply Now</a></div>'''

c = c.replace(old_devops, new_devops)

# Add Compliance role after Technical Content Writer
old_content_writer = b'<div class="job-card"><div class="job-info"><h4>Technical Content Writer (Blockchain / DeFi)</h4><div class="job-tags"><span class="jtag jtag-dept">Marketing</span><span class="jtag jtag-type">Contract</span><span class="jtag jtag-loc">Remote</span></div></div><a href="#apply" class="btn btn-outline btn-sm">Apply Now</a></div>'
new_content_writer = old_content_writer + b'''
      <div class="job-card"><div class="job-info"><h4>Compliance &amp; Regulatory Specialist</h4><div class="job-tags"><span class="jtag jtag-dept">Legal</span><span class="jtag jtag-type">Full-time</span><span class="jtag jtag-loc">Remote / Toronto</span></div></div><a href="#apply" class="btn btn-outline btn-sm">Apply Now</a></div>'''

c = c.replace(old_content_writer, new_content_writer)

with open('careers/index.html', 'wb') as f:
    f.write(c)
print('careers done')

# ── contact/index.html ───────────────────────────────────────────────────────
with open('contact/index.html', 'rb') as f:
    c = f.read()

# Add office cards, response time guarantee, and FAQ before footer
new_sections = b'''
<!-- Office Locations -->
<section class="section" style="background:var(--bg2)">
  <div class="container">
    <div class="text-center reveal">
      <span class="eyebrow">Our Offices</span>
      <h2>Find Us <span class="grad-text">Around the Globe</span></h2>
      <div class="section-divider"></div>
    </div>
    <div class="svc-grid reveal-stagger" style="grid-template-columns:repeat(3,1fr);margin-top:48px">
      <div class="svc-card" style="padding:32px">
        <div style="font-size:2.2rem;margin-bottom:16px">&#127464;&#127462;</div>
        <h3 style="margin-bottom:6px">Toronto, Canada</h3>
        <span style="font-size:0.78rem;font-weight:600;color:var(--accent);text-transform:uppercase;letter-spacing:0.06em">Headquarters</span>
        <div class="section-divider" style="margin:14px 0"></div>
        <p style="font-size:0.87rem;margin-bottom:8px">43 King Street West<br>Toronto, ON M5H 1K1, Canada</p>
        <p style="font-size:0.84rem;color:var(--muted2)">Mon &#8211; Fri, 9am &#8211; 6pm EST</p>
        <p style="font-size:0.84rem;margin-top:8px">+1 (681) 553-4010</p>
      </div>
      <div class="svc-card" style="padding:32px">
        <div style="font-size:2.2rem;margin-bottom:16px">&#127462;&#127466;</div>
        <h3 style="margin-bottom:6px">Dubai, UAE</h3>
        <span style="font-size:0.78rem;font-weight:600;color:var(--accent);text-transform:uppercase;letter-spacing:0.06em">MENA Office</span>
        <div class="section-divider" style="margin:14px 0"></div>
        <p style="font-size:0.87rem;margin-bottom:8px">Dubai Internet City<br>Dubai, United Arab Emirates</p>
        <p style="font-size:0.84rem;color:var(--muted2)">Sun &#8211; Thu, 9am &#8211; 6pm GST</p>
        <p style="font-size:0.84rem;margin-top:8px">hello@pumapulse.org</p>
      </div>
      <div class="svc-card" style="padding:32px">
        <div style="font-size:2.2rem;margin-bottom:16px">&#127480;&#127468;</div>
        <h3 style="margin-bottom:6px">Singapore</h3>
        <span style="font-size:0.78rem;font-weight:600;color:var(--accent);text-transform:uppercase;letter-spacing:0.06em">APAC Office</span>
        <div class="section-divider" style="margin:14px 0"></div>
        <p style="font-size:0.87rem;margin-bottom:8px">One Raffles Place<br>Singapore 048616</p>
        <p style="font-size:0.84rem;color:var(--muted2)">Mon &#8211; Fri, 9am &#8211; 6pm SGT</p>
        <p style="font-size:0.84rem;margin-top:8px">sales@pumapulse.org</p>
      </div>
    </div>
  </div>
</section>

<!-- Response Time Guarantee -->
<section class="section-sm">
  <div class="container">
    <div class="cta-banner reveal" style="text-align:center">
      <div class="cta-bg"><img src="https://images.pexels.com/photos/3184291/pexels-photo-3184291.jpeg?auto=compress&cs=tinysrgb&w=1600" alt="Response Time"></div>
      <div class="cta-content">
        <div style="font-size:3.5rem;font-weight:900;background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1;margin-bottom:12px">24h</div>
        <h2>We Respond Within <span class="grad-text">24 Hours</span></h2>
        <p style="max-width:520px;margin:0 auto">Every inquiry gets a real, thoughtful response from our team &#8212; not a bot, not a template. Send us a message today and hear back by tomorrow.</p>
        <div style="display:flex;gap:24px;justify-content:center;flex-wrap:wrap;margin-top:28px">
          <div style="text-align:center"><div style="font-size:1.4rem;font-weight:800;color:#fff">Free</div><div style="font-size:0.82rem;color:rgba(255,255,255,0.6)">Strategy Call</div></div>
          <div style="text-align:center"><div style="font-size:1.4rem;font-weight:800;color:#fff">48h</div><div style="font-size:0.82rem;color:rgba(255,255,255,0.6)">Detailed Proposal</div></div>
          <div style="text-align:center"><div style="font-size:1.4rem;font-weight:800;color:#fff">NDA</div><div style="font-size:0.82rem;color:rgba(255,255,255,0.6)">Before Any Discussion</div></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="section" style="background:var(--bg2)">
  <div class="container">
    <div class="text-center reveal">
      <span class="eyebrow">Quick Answers</span>
      <h2>Common Questions About <span class="grad-text2">Working With Us</span></h2>
      <div class="section-divider"></div>
    </div>
    <div style="max-width:760px;margin:48px auto 0;display:flex;flex-direction:column;gap:16px" class="reveal-stagger">
      <div class="svc-card" style="padding:28px 32px">
        <h4 style="margin-bottom:10px;font-size:1rem">How long does it take to build a crypto exchange?</h4>
        <p style="font-size:0.88rem">A white-label exchange can be live in 4&#8211;6 weeks. A fully custom platform typically takes 3&#8211;5 months depending on features, compliance requirements, and integrations. We&#39;ll give you a precise timeline after our discovery call.</p>
      </div>
      <div class="svc-card" style="padding:28px 32px">
        <h4 style="margin-bottom:10px;font-size:1rem">Do you sign NDAs before discussing project details?</h4>
        <p style="font-size:0.88rem">Absolutely &#8212; we sign an NDA before any technical or business discussion. Your idea and IP are protected from the very first conversation. We take confidentiality seriously and have never had a breach.</p>
      </div>
      <div class="svc-card" style="padding:28px 32px">
        <h4 style="margin-bottom:10px;font-size:1rem">What happens after the project is delivered?</h4>
        <p style="font-size:0.88rem">We don&#39;t disappear after launch. Every project includes a 30-day post-launch support period, and we offer ongoing maintenance retainers with SLA-backed uptime guarantees. Most of our clients stay with us for years.</p>
      </div>
    </div>
  </div>
</section>

'''

footer_marker = b'<div id="footer-placeholder"></div>'
c = c.replace(footer_marker, new_sections + footer_marker, 1)

with open('contact/index.html', 'wb') as f:
    f.write(c)
print('contact done')
