/* PumaPulse — Advanced Animations */

// ── Counter animation ──
function animateCounter(el) {
  const target = parseFloat(el.dataset.target);
  const suffix = el.dataset.suffix || '';
  const prefix = el.dataset.prefix || '';
  const decimals = el.dataset.decimals || 0;
  const duration = 2000;
  const start = performance.now();
  function update(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    const ease = 1 - Math.pow(1 - progress, 4);
    const current = (target * ease).toFixed(decimals);
    el.textContent = prefix + current + suffix;
    if (progress < 1) requestAnimationFrame(update);
  }
  requestAnimationFrame(update);
}

const counterIO = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.querySelectorAll('[data-target]').forEach(animateCounter);
      counterIO.unobserve(e.target);
    }
  });
}, { threshold: 0.3 });
document.querySelectorAll('.counter-section').forEach(el => counterIO.observe(el));

// ── Typewriter effect ──
function typewriter(el) {
  const words = JSON.parse(el.dataset.words || '[]');
  if (!words.length) return;
  let wi = 0, ci = 0, deleting = false;
  function tick() {
    const word = words[wi];
    if (!deleting) {
      el.textContent = word.slice(0, ++ci);
      if (ci === word.length) { deleting = true; setTimeout(tick, 1800); return; }
    } else {
      el.textContent = word.slice(0, --ci);
      if (ci === 0) { deleting = false; wi = (wi + 1) % words.length; }
    }
    setTimeout(tick, deleting ? 60 : 100);
  }
  tick();
}
document.querySelectorAll('[data-words]').forEach(typewriter);

// ── Parallax on scroll ──
function parallax() {
  const els = document.querySelectorAll('[data-parallax]');
  els.forEach(el => {
    const speed = parseFloat(el.dataset.parallax) || 0.3;
    const rect = el.getBoundingClientRect();
    const offset = (window.innerHeight / 2 - rect.top - rect.height / 2) * speed;
    el.style.transform = `translateY(${offset}px)`;
  });
}
window.addEventListener('scroll', parallax, { passive: true });
parallax();

// ── Magnetic buttons ──
document.querySelectorAll('.btn-magnetic').forEach(btn => {
  btn.addEventListener('mousemove', e => {
    const r = btn.getBoundingClientRect();
    const x = e.clientX - r.left - r.width / 2;
    const y = e.clientY - r.top - r.height / 2;
    btn.style.transform = `translate(${x * 0.25}px, ${y * 0.25}px)`;
  });
  btn.addEventListener('mouseleave', () => {
    btn.style.transform = '';
  });
});

// ── Tilt cards ──
document.querySelectorAll('.tilt-card').forEach(card => {
  card.addEventListener('mousemove', e => {
    const r = card.getBoundingClientRect();
    const x = (e.clientX - r.left) / r.width - 0.5;
    const y = (e.clientY - r.top) / r.height - 0.5;
    card.style.transform = `perspective(800px) rotateY(${x * 8}deg) rotateX(${-y * 8}deg) translateZ(8px)`;
  });
  card.addEventListener('mouseleave', () => {
    card.style.transform = 'perspective(800px) rotateY(0) rotateX(0) translateZ(0)';
    card.style.transition = 'transform 0.5s ease';
  });
  card.addEventListener('mouseenter', () => {
    card.style.transition = 'transform 0.1s ease';
  });
});

// ── Glowing cursor trail ──
const trail = document.createElement('div');
trail.style.cssText = 'position:fixed;width:300px;height:300px;border-radius:50%;pointer-events:none;z-index:0;transition:opacity 0.3s;opacity:0;background:radial-gradient(circle,rgba(192,32,42,0.06) 0%,transparent 70%);transform:translate(-50%,-50%);';
document.body.appendChild(trail);
let trailX = 0, trailY = 0, curX = 0, curY = 0;
document.addEventListener('mousemove', e => { curX = e.clientX; curY = e.clientY; trail.style.opacity = '1'; });
document.addEventListener('mouseleave', () => { trail.style.opacity = '0'; });
function animateTrail() {
  trailX += (curX - trailX) * 0.08;
  trailY += (curY - trailY) * 0.08;
  trail.style.left = trailX + 'px';
  trail.style.top = trailY + 'px';
  requestAnimationFrame(animateTrail);
}
animateTrail();

// ── Number ticker on hero stats ──
document.querySelectorAll('.hero-stat-num[data-target]').forEach(el => {
  const io = new IntersectionObserver(entries => {
    if (entries[0].isIntersecting) { animateCounter(el); io.disconnect(); }
  }, { threshold: 0.5 });
  io.observe(el);
});

// ── Scroll progress bar ──
const bar = document.createElement('div');
bar.style.cssText = 'position:fixed;top:0;left:0;height:2px;background:linear-gradient(90deg,#c0202a,#e0263a);z-index:99999;transition:width 0.1s linear;width:0%;';
document.body.appendChild(bar);
window.addEventListener('scroll', () => {
  const pct = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
  bar.style.width = pct + '%';
}, { passive: true });

// ── Stagger children on reveal ──
const staggerIO = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('revealed');
      staggerIO.unobserve(e.target);
    }
  });
}, { threshold: 0.07, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-stagger').forEach(el => staggerIO.observe(el));

// ── Floating particles background ──
(function() {
  const canvas = document.getElementById('particleCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let W = canvas.width = window.innerWidth;
  let H = canvas.height = window.innerHeight;
  window.addEventListener('resize', () => { W = canvas.width = window.innerWidth; H = canvas.height = window.innerHeight; });
  const particles = Array.from({length: 60}, () => ({
    x: Math.random() * W, y: Math.random() * H,
    r: Math.random() * 1.5 + 0.5,
    vx: (Math.random() - 0.5) * 0.3,
    vy: (Math.random() - 0.5) * 0.3,
    o: Math.random() * 0.4 + 0.1
  }));
  function draw() {
    ctx.clearRect(0, 0, W, H);
    particles.forEach(p => {
      p.x += p.vx; p.y += p.vy;
      if (p.x < 0) p.x = W; if (p.x > W) p.x = 0;
      if (p.y < 0) p.y = H; if (p.y > H) p.y = 0;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(16,185,129,${p.o})`;
      ctx.fill();
    });
    // Draw connections
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx*dx + dy*dy);
        if (dist < 120) {
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = `rgba(59,130,246,${0.08 * (1 - dist/120)})`;
          ctx.lineWidth = 0.5;
          ctx.stroke();
        }
      }
    }
    requestAnimationFrame(draw);
  }
  draw();
})();
