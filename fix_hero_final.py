import re

with open('index.html', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8', errors='replace')

# Find the hero section and replace it entirely
old_hero = re.search(r'<!-- Hero -->.*?</section>', content, re.DOTALL)
if not old_hero:
    print('Hero not found')
    exit()

new_hero = '''<!-- Hero -->
<section class="hero" style="min-height:100vh;padding-top:0">
  <div class="hero-video-wrap">
    <video autoplay muted loop playsinline poster="https://images.pexels.com/photos/8358141/pexels-photo-8358141.jpeg?auto=compress&cs=tinysrgb&w=1600">
      <source src="https://cdn.coverr.co/videos/coverr-a-digital-globe-with-network-connections-1584/1080p.mp4" type="video/mp4">
    </video>
  </div>
  <div class="container hero-split">
    <!-- Left: text -->
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
    <!-- Right: solar system -->
    <div class="hero-right" style="position:relative;z-index:3;display:flex;align-items:center;justify-content:center;padding:80px 0">
      <canvas id="solarCanvas" style="width:100%;max-width:480px;height:480px;display:block"></canvas>
    </div>
  </div>
</section>'''

content = content[:old_hero.start()] + new_hero + content[old_hero.end():]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
