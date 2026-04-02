import re

with open('index.html', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8', errors='replace')

# 1. Replace video background with deep space image
content = re.sub(
    r'<div class="hero-video-wrap">[\s\S]*?</div>\s*</div>',
    '''<div class="hero-video-wrap">
    <img src="https://images.pexels.com/photos/1169754/pexels-photo-1169754.jpeg?auto=compress&cs=tinysrgb&w=1920" alt="Deep Space" style="width:100%;height:100%;object-fit:cover;position:absolute;inset:0">
  </div>''',
    content, count=1
)

# 2. Replace hero-right (dashboard mockup) with solar system canvas
new_hero_right = '''      <div class="hero-right" style="padding:60px 0;position:relative;display:flex;align-items:center;justify-content:center">
        <canvas id="solarCanvas" style="width:100%;max-width:520px;height:520px;display:block"></canvas>
      </div>'''

content = re.sub(
    r'<div class="hero-right"[\s\S]*?(?=\s*</div>\s*</div>\s*</div>\s*</section>)',
    new_hero_right,
    content, count=1
)

# 3. Remove old galaxy JS and replace with solar system JS
content = re.sub(r'<script>\s*\(function\(\)\{[\s\S]*?galaxyCanvas[\s\S]*?\}\)\(\);\s*</script>', '', content)

solar_js = '''
<script>
(function(){
  var c = document.getElementById('solarCanvas');
  if(!c) return;
  var W = c.offsetWidth || 520, H = 520;
  c.width = W; c.height = H;
  var ctx = c.getContext('2d');
  var cx = W/2, cy = H/2;

  var planets = [
    { name:'Mercury', r:4,  dist:52,  speed:0.047, color:'#b5b5b5', angle:0 },
    { name:'Venus',   r:7,  dist:80,  speed:0.035, color:'#e8cda0', angle:1 },
    { name:'Earth',   r:8,  dist:112, speed:0.029, color:'#4fa3e0', angle:2,
      moon:{ r:3, dist:18, speed:0.12, color:'#ccc', angle:0 } },
    { name:'Mars',    r:6,  dist:148, speed:0.024, color:'#c1440e', angle:3 },
    { name:'Jupiter', r:18, dist:200, speed:0.013, color:'#c88b3a', angle:1,
      bands:['#c88b3a','#d4a96a','#b87333','#e8c49a'] },
    { name:'Saturn',  r:14, dist:252, speed:0.009, color:'#e4d191', angle:4, ring:true },
  ];

  var stars = [];
  for(var i=0;i<220;i++){
    stars.push({
      x: Math.random()*W, y: Math.random()*H,
      r: Math.random()*1.4+0.2,
      o: Math.random()*0.8+0.2,
      t: Math.random()*Math.PI*2
    });
  }

  function drawStar(x,y,r,o){ ctx.beginPath(); ctx.arc(x,y,r,0,Math.PI*2); ctx.fillStyle='rgba(255,255,255,'+o+')'; ctx.fill(); }

  function drawPlanet(p){
    var x = cx + Math.cos(p.angle)*p.dist;
    var y = cy + Math.sin(p.angle)*p.dist;

    // Saturn ring
    if(p.ring){
      ctx.save();
      ctx.translate(x,y);
      ctx.scale(1,0.35);
      ctx.beginPath();
      ctx.arc(0,0,p.r+10,0,Math.PI*2);
      ctx.strokeStyle='rgba(228,209,145,0.5)';
      ctx.lineWidth=5;
      ctx.stroke();
      ctx.restore();
    }

    // Jupiter bands
    if(p.bands){
      var grd = ctx.createRadialGradient(x-p.r*0.3,y-p.r*0.3,p.r*0.1,x,y,p.r);
      grd.addColorStop(0,'#f0d090');
      grd.addColorStop(0.4,'#c88b3a');
      grd.addColorStop(0.7,'#b87333');
      grd.addColorStop(1,'#8b5e1a');
      ctx.beginPath(); ctx.arc(x,y,p.r,0,Math.PI*2);
      ctx.fillStyle=grd; ctx.fill();
    } else {
      var grd = ctx.createRadialGradient(x-p.r*0.35,y-p.r*0.35,p.r*0.05,x,y,p.r);
      grd.addColorStop(0,'rgba(255,255,255,0.6)');
      grd.addColorStop(0.4,p.color);
      grd.addColorStop(1,'rgba(0,0,0,0.5)');
      ctx.beginPath(); ctx.arc(x,y,p.r,0,Math.PI*2);
      ctx.fillStyle=grd; ctx.fill();
    }

    // Moon
    if(p.moon){
      var mx = x + Math.cos(p.moon.angle)*p.moon.dist;
      var my = y + Math.sin(p.moon.angle)*p.moon.dist;
      ctx.beginPath(); ctx.arc(mx,my,p.moon.r,0,Math.PI*2);
      ctx.fillStyle=p.moon.color; ctx.fill();
      p.moon.angle += p.moon.speed * 0.016;
    }

    p.angle += p.speed * 0.016;
  }

  var last = 0;
  function draw(ts){
    var dt = Math.min((ts-last)/16, 3); last=ts;
    ctx.clearRect(0,0,W,H);

    // Stars twinkle
    stars.forEach(function(s){
      s.t += 0.02;
      var o = s.o*(0.7+0.3*Math.sin(s.t));
      drawStar(s.x,s.y,s.r,o);
    });

    // Nebula glow
    [[cx,cy-60,80,'59,130,246'],[cx+80,cy+60,60,'167,139,250'],[cx-70,cy+40,70,'16,185,129']].forEach(function(n){
      var g=ctx.createRadialGradient(n[0],n[1],0,n[0],n[1],n[2]);
      g.addColorStop(0,'rgba('+n[3]+',0.07)'); g.addColorStop(1,'rgba('+n[3]+',0)');
      ctx.fillStyle=g; ctx.beginPath(); ctx.arc(n[0],n[1],n[2],0,Math.PI*2); ctx.fill();
    });

    // Orbit rings
    planets.forEach(function(p){
      ctx.beginPath(); ctx.arc(cx,cy,p.dist,0,Math.PI*2);
      ctx.strokeStyle='rgba(255,255,255,0.06)'; ctx.lineWidth=1; ctx.stroke();
    });

    // Sun
    var sunGrd = ctx.createRadialGradient(cx,cy,0,cx,cy,22);
    sunGrd.addColorStop(0,'#fff7a0'); sunGrd.addColorStop(0.4,'#ffcc00'); sunGrd.addColorStop(1,'#ff6600');
    ctx.beginPath(); ctx.arc(cx,cy,22,0,Math.PI*2); ctx.fillStyle=sunGrd; ctx.fill();
    // Sun glow
    var glowGrd = ctx.createRadialGradient(cx,cy,10,cx,cy,50);
    glowGrd.addColorStop(0,'rgba(255,200,0,0.25)'); glowGrd.addColorStop(1,'rgba(255,100,0,0)');
    ctx.beginPath(); ctx.arc(cx,cy,50,0,Math.PI*2); ctx.fillStyle=glowGrd; ctx.fill();

    planets.forEach(drawPlanet);
    requestAnimationFrame(draw);
  }
  requestAnimationFrame(draw);
})();
</script>
'''

content = content.replace('</body>', solar_js + '\n</body>', 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
