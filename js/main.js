/* PumaPulse — main.js */

// ── Navbar scroll ──
const navbar = document.querySelector('.navbar');
if (navbar) {
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 30);
  }, { passive: true });
  // Trigger once on load
  if (window.scrollY > 30) navbar.classList.add('scrolled');
}

// ── Mobile menu (only for pages with inline navbar, not nav.js pages) ──
const hamburger = document.querySelector('.hamburger');
if (hamburger && !hamburger.dataset.wired) {
  hamburger.dataset.wired = '1';
  hamburger.addEventListener('click', () => {
    document.body.classList.toggle('nav-mobile-open');
    hamburger.classList.toggle('open');
  });
}

// ── Scroll reveal ──
const revealEls = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-stagger');
if (revealEls.length) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('revealed');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.07, rootMargin: '0px 0px -36px 0px' });
  revealEls.forEach(el => io.observe(el));
}

// ── Solutions tabs ──
window.switchSol = function(id, btn) {
  document.querySelectorAll('.sol-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.sol-tab').forEach(b => b.classList.remove('active'));
  const panel = document.getElementById('sol-' + id);
  if (panel) panel.classList.add('active');
  if (btn) btn.classList.add('active');
};

// ── Contact form ──
const contactForm = document.querySelector('.contact-form form');
if (contactForm) {
  contactForm.addEventListener('submit', e => {
    e.preventDefault();
    const btn = e.target.querySelector('button[type="submit"]');
    const orig = btn.textContent;
    btn.textContent = 'Message Sent ✓';
    btn.style.background = 'rgba(16,185,129,0.15)';
    btn.style.color = 'var(--accent)';
    btn.disabled = true;
    setTimeout(() => {
      btn.textContent = orig;
      btn.style.background = '';
      btn.style.color = '';
      btn.disabled = false;
      e.target.reset();
    }, 3500);
  });
}

// ── Apply form ──
const applyForm = document.querySelector('.apply-form form');
if (applyForm) {
  applyForm.addEventListener('submit', e => {
    e.preventDefault();
    const btn = e.target.querySelector('button[type="submit"]');
    btn.textContent = 'Application Submitted ✓';
    btn.style.background = 'rgba(16,185,129,0.15)';
    btn.style.color = 'var(--accent)';
    btn.disabled = true;
    setTimeout(() => {
      btn.textContent = 'Submit Application';
      btn.style.background = '';
      btn.style.color = '';
      btn.disabled = false;
      e.target.reset();
    }, 4000);
  });
}

// ── Newsletter ──
document.querySelectorAll('.newsletter-form').forEach(f => {
  f.addEventListener('submit', e => {
    e.preventDefault();
    const btn = f.querySelector('button');
    btn.textContent = 'Subscribed!';
    btn.disabled = true;
    setTimeout(() => { btn.textContent = 'Subscribe'; btn.disabled = false; f.reset(); }, 3000);
  });
});

// ── Culture video ──
const vid = document.getElementById('cultureVid');
const wrap = document.getElementById('cultureVideo');
document.getElementById('playBtn')?.addEventListener('click', () => {
  vid?.play();
  wrap?.classList.add('playing');
});
vid?.addEventListener('click', () => {
  if (vid.paused) { vid.play(); wrap?.classList.add('playing'); }
  else { vid.pause(); wrap?.classList.remove('playing'); }
});
