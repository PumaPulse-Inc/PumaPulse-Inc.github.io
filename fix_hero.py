import re

with open('index.html', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8', errors='replace')

# New hero-right: dashboard mockup + galaxy canvas
new_hero_right = '''      <div class="hero-right" style="padding:80px 0 60px;position:relative">
        <!-- Galaxy canvas -->
        <canvas id="galaxyCanvas" style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:0;border-radius:24px;opacity:0.7"></canvas>
        <!-- Dashboard mockup -->
        <div class="dashboard-mockup" style="position:relative;z-index:1">
          <!-- Top bar -->
          <div style="background:rgba(15,23,42,0.92);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.1);border-radius:20px;padding:20px 24px;margin-bottom:14px">
            <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px">
              <div style="display:flex;align-items:center;gap:10px">
                <div style="width:10px;height:10px;border-radius:50%;background:#10b981;box-shadow:0 0 8px #10b981"></div>
                <span style="font-size:0.78rem;font-weight:600;color:rgba(240,244,255,0.7)">PumaPulse Exchange</span>
              </div>
              <span style="font-size:0.72rem;color:rgba(240,244,255,0.4)">Live Dashboard</span>
            </div>
            <!-- Chart bars -->
            <div style="display:flex;align-items:flex-end;gap:5px;height:70px;margin-bottom:12px">
              <div style="flex:1;background:linear-gradient(to top,#10b981,rgba(16,185,129,0.3));border-radius:4px 4px 0 0;height:40%;animation:barGrow 1s 0.1s both"></div>
              <div style="flex:1;background:linear-gradient(to top,#10b981,rgba(16,185,129,0.3));border-radius:4px 4px 0 0;height:65%;animation:barGrow 1s 0.2s both"></div>
              <div style="flex:1;background:linear-gradient(to top,#10b981,rgba(16,185,129,0.3));border-radius:4px 4px 0 0;height:45%;animation:barGrow 1s 0.3s both"></div>
              <div style="flex:1;background:linear-gradient(to top,#3b82f6,rgba(59,130,246,0.3));border-radius:4px 4px 0 0;height:80%;animation:barGrow 1s 0.4s both"></div>
              <div style="flex:1;background:linear-gradient(to top,#3b82f6,rgba(59,130,246,0.3));border-radius:4px 4px 0 0;height:55%;animation:barGrow 1s 0.5s both"></div>
              <div style="flex:1;background:linear-gradient(to top,#a78bfa,rgba(167,139,250,0.3));border-radius:4px 4px 0 0;height:90%;animation:barGrow 1s 0.6s both"></div>
              <div style="flex:1;background:linear-gradient(to top,#a78bfa,rgba(167,139,250,0.3));border-radius:4px 4px 0 0;height:70%;animation:barGrow 1s 0.7s both"></div>
              <div style="flex:1;background:linear-gradient(to top,#10b981,rgba(16,185,129,0.3));border-radius:4px 4px 0 0;height:100%;animation:barGrow 1s 0.8s both;box-shadow:0 0 12px rgba(16,185,129,0.5)"></div>
            </div>
            <div style="display:flex;justify-content:space-between">
              <div><div style="font-size:1.4rem;font-weight:800;color:#fff">$2.4M</div><div style="font-size:0.72rem;color:rgba(240,244,255,0.45)">24h Volume</div></div>
              <div style="text-align:right"><div style="font-size:1.4rem;font-weight:800;color:#10b981">+18.4%</div><div style="font-size:0.72rem;color:rgba(240,244,255,0.45)">ROI This Month</div></div>
            </div>
          </div>
          <!-- Metric cards row -->
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:14px">
            <div style="background:rgba(59,130,246,0.12);border:1px solid rgba(59,130,246,0.25);border-radius:14px;padding:16px">
              <div style="font-size:0.72rem;color:rgba(240,244,255,0.5);margin-bottom:6px">Active Bots</div>
              <div style="font-size:1.5rem;font-weight:800;color:#fff">247</div>
              <div style="font-size:0.72rem;color:#3b82f6;margin-top:4px">&#9650; 12 new today</div>
            </div>
            <div style="background:rgba(167,139,250,0.12);border:1px solid rgba(167,139,250,0.25);border-radius:14px;padding:16px">
              <div style="font-size:0.72rem;color:rgba(240,244,255,0.5);margin-bottom:6px">Neobank Users</div>
              <div style="font-size:1.5rem;font-weight:800;color:#fff">12K</div>
              <div style="font-size:0.72rem;color:#a78bfa;margin-top:4px">&#9650; 340 this week</div>
            </div>
          </div>
          <!-- Bottom status bar -->
          <div style="background:rgba(15,23,42,0.92);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.08);border-radius:14px;padding:14px 18px;display:flex;align-items:center;justify-content:space-between">
            <div style="display:flex;align-items:center;gap:8px">
              <div style="width:8px;height:8px;border-radius:50%;background:#10b981;animation:glowPulse 2s infinite"></div>
              <span style="font-size:0.78rem;color:rgba(240,244,255,0.6)">All systems operational</span>
            </div>
            <div style="display:flex;gap:16px">
              <span style="font-size:0.72rem;color:rgba(240,244,255,0.4)">Latency: <span style="color:#10b981">0.8ms</span></span>
              <span style="font-size:0.72rem;color:rgba(240,244,255,0.4)">Uptime: <span style="color:#10b981">99.9%</span></span>
            </div>
          </div>
        </div>
      </div>'''

# Replace the hero-right div (from opening to closing </div> after last live-card)
fixed = re.sub(
    r'<div class="hero-right"[^>]*>[\s\S]*?</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>',
    new_hero_right + '\n      </div>\n    </div>\n  </div>\n</section>',
    content, count=1
)

# Add CSS for bar animation and galaxy in the <style> block
bar_css = '''
    @keyframes barGrow{from{transform:scaleY(0);transform-origin:bottom}to{transform:scaleY(1);transform-origin:bottom}}
    .dashboard-mockup{animation:fadeInUp 0.8s 0.3s both}
'''

fixed = fixed.replace('    /* -- Hero extras -- */', '    /* -- Hero extras -- */\n' + bar_css, 1)

# Add galaxy JS before </body>
galaxy_js = '''
<script>
(function(){
  var c = document.getElementById('galaxyCanvas');
  if(!c) return;
  var ctx = c.getContext('2d');
  var stars = [];
  function resize(){
    c.width = c.offsetWidth;
    c.height = c.offsetHeight;
  }
  resize();
  window.addEventListener('resize', resize);
  for(var i=0;i<180;i++){
    stars.push({
      x: Math.random(),
      y: Math.random(),
      r: Math.random()*1.8+0.3,
      o: Math.random()*0.7+0.2,
      s: Math.random()*0.0003+0.0001,
      hue: Math.random()<0.5 ? 160 : (Math.random()<0.5 ? 220 : 270)
    });
  }
  var nebula = [];
  for(var j=0;j<6;j++){
    nebula.push({
      x: Math.random(), y: Math.random(),
      r: Math.random()*120+60,
      hue: [160,220,270,200][Math.floor(Math.random()*4)],
      o: Math.random()*0.08+0.03
    });
  }
  var t=0;
  function draw(){
    ctx.clearRect(0,0,c.width,c.height);
    // nebula blobs
    nebula.forEach(function(n){
      var grd = ctx.createRadialGradient(n.x*c.width,n.y*c.height,0,n.x*c.width,n.y*c.height,n.r);
      grd.addColorStop(0,'hsla('+n.hue+',80%,60%,'+n.o+')');
      grd.addColorStop(1,'hsla('+n.hue+',80%,60%,0)');
      ctx.fillStyle=grd;
      ctx.beginPath();
      ctx.arc(n.x*c.width,n.y*c.height,n.r,0,Math.PI*2);
      ctx.fill();
    });
    // stars
    stars.forEach(function(s){
      var flicker = Math.sin(t*s.s*1000+s.x*100)*0.3+0.7;
      ctx.beginPath();
      ctx.arc(s.x*c.width,s.y*c.height,s.r,0,Math.PI*2);
      ctx.fillStyle='hsla('+s.hue+',70%,90%,'+(s.o*flicker)+')';
      ctx.fill();
    });
    t++;
    requestAnimationFrame(draw);
  }
  draw();
})();
</script>
'''

fixed = fixed.replace('</body>', galaxy_js + '</body>', 1)

if fixed != content:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(fixed)
    print('Done!')
else:
    print('Pattern not matched')
