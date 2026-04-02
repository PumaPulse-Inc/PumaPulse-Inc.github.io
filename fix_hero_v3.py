import re

with open('index.html', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8', errors='replace')

# 1. Replace entire hero section
new_hero = '''<!-- Hero -->
<section class="hero" style="min-height:100vh;padding-top:0">
  <div class="hero-video-wrap">
    <img src="https://images.pexels.com/photos/3861969/pexels-photo-3861969.jpeg?auto=compress&cs=tinysrgb&w=1920" alt="Fintech Background" style="width:100%;height:100%;object-fit:cover;position:absolute;inset:0">
  </div>
  <div class="container hero-split">
    <div class="hero-left" style="position:relative;z-index:3">
      <div class="hero-badge anim-float">
        <span class="hero-badge-dot"></span>
        Trusted Digital Transformation Company
      </div>
      <h1 style="color:#fff">Your Business Deserves<br><span class="shimmer-text">More Revenue,</span><br>Not More Work</h1>
      <p class="hero-desc">What's stopping your business from growing faster? We remove the friction, automate what slows you down, and help you scale at 10X speed — effortlessly. From crypto exchanges to AI-powered trading bots, we engineer high-performance fintech products that last.</p>
      <div class="hero-actions">
        <a href="contact/" class="btn btn-accent btn-lg btn-magnetic ripple-btn">Start Your Project</a>
        <a href="portfolio/" class="btn btn-ghost btn-lg">View Our Work</a>
      </div>
      <div class="trusted-row">
        <span class="trusted-label">Trusted by</span>
        <div class="trusted-logos">
          <span class="trusted-logo">Dreamster</span>
          <span class="trusted-logo">Cryptinum</span>
          <span class="trusted-logo">Apzor</span>
          <span class="trusted-logo">MetaStation</span>
          <span class="trusted-logo">MarginFX</span>
        </div>
      </div>
    </div>
    <div class="hero-right" style="position:relative;z-index:3;display:flex;align-items:center;justify-content:center;padding:80px 0">
      <canvas id="particleCanvas" style="width:100%;max-width:480px;height:480px;display:block;border-radius:24px"></canvas>
    </div>
  </div>
</section>'''

content = re.sub(r'<!-- Hero -->.*?</section>', new_hero, content, count=1, flags=re.DOTALL)

# 2. Remove "View All Projects" button (standalone button between hero and stats)
content = re.sub(
    r'<div[^>]*style="[^"]*text-align:center[^"]*"[^>]*>\s*<a[^>]*>View All Projects</a>\s*</div>',
    '', content
)
# Also catch other variants
content = re.sub(r'<a[^>]*class="[^"]*btn[^"]*"[^>]*>\s*View All Projects\s*</a>', '', content)

# 3. Remove old solar system JS
content = re.sub(r'<script>\s*\(function\(\)\{[\s\S]*?solarCanvas[\s\S]*?\}\)\(\);\s*</script>', '', content)

# 4. Add particle/network animation JS
particle_js = '''
<script>
(function(){
  var c = document.getElementById('particleCanvas');
  if(!c) return;
  var W = c.offsetWidth || 480, H = 480;
  c.width = W; c.height = H;
  var ctx = c.getContext('2d');

  var nodes = [];
  for(var i = 0; i < 60; i++){
    nodes.push({
      x: Math.random() * W,
      y: Math.random() * H,
      vx: (Math.random() - 0.5) * 0.6,
      vy: (Math.random() - 0.5) * 0.6,
      r: Math.random() * 2.5 + 1,
      hue: [160, 220, 270, 200][Math.floor(Math.random() * 4)]
    });
  }

  function draw(){
    ctx.clearRect(0, 0, W, H);

    // Draw connections
    for(var i = 0; i < nodes.length; i++){
      for(var j = i + 1; j < nodes.length; j++){
        var dx = nodes[i].x - nodes[j].x;
        var dy = nodes[i].y - nodes[j].y;
        var dist = Math.sqrt(dx*dx + dy*dy);
        if(dist < 100){
          ctx.beginPath();
          ctx.moveTo(nodes[i].x, nodes[i].y);
          ctx.lineTo(nodes[j].x, nodes[j].y);
          ctx.strokeStyle = 'rgba(16,185,129,' + (1 - dist/100) * 0.35 + ')';
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }
      }
    }

    // Draw nodes
    nodes.forEach(function(n){
      var grd = ctx.createRadialGradient(n.x, n.y, 0, n.x, n.y, n.r * 2);
      grd.addColorStop(0, 'hsla(' + n.hue + ',80%,70%,0.9)');
      grd.addColorStop(1, 'hsla(' + n.hue + ',80%,70%,0)');
      ctx.beginPath();
      ctx.arc(n.x, n.y, n.r * 2, 0, Math.PI * 2);
      ctx.fillStyle = grd;
      ctx.fill();

      // Move
      n.x += n.vx;
      n.y += n.vy;
      if(n.x < 0 || n.x > W) n.vx *= -1;
      if(n.y < 0 || n.y > H) n.vy *= -1;
    });

    requestAnimationFrame(draw);
  }
  draw();
})();
</script>
'''

content = content.replace('</body>', particle_js + '\n</body>', 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
