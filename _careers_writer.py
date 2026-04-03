import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

html = ""
html += """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Careers at PumaPulse - Join Our Team</title>
<meta name="description" content="Join PumaPulse and help build the financial infrastructure of tomorrow. We hire blockchain engineers, fintech developers, and product designers.">
<link rel="icon" href="../img/icon.png" type="image/png">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/style.css">
<link rel="stylesheet" href="../css/theme.css">
<link rel="stylesheet" href="../css/animations.css">
<link rel="stylesheet" href="../css/mobile.css">
<style>
body{font-family:'Inter',sans-serif;background:#f5f6fa;color:#1a1e2e;overflow-x:hidden}
.car-hero{min-height:90vh;position:relative;display:flex;align-items:center;overflow:hidden;background:#060a14}
.car-hero-bg{position:absolute;inset:0;background:url('https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1800&q=80') center/cover;opacity:.15}
.car-hero-grad{position:absolute;inset:0;background:linear-gradient(135deg,rgba(192,32,42,.18) 0%,transparent 55%),linear-gradient(to top,#060a14 0%,transparent 55%)}
.car-hero-grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.03) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.03) 1px,transparent 1px);background-size:60px 60px}
.car-hero-inner{position:relative;z-index:2;max-width:1200px;margin:0 auto;padding:120px 44px 80px}
.car-eyebrow{display:inline-flex;align-items:center;gap:10px;font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:rgba(192,32,42,.9);margin-bottom:24px}
.car-eyebrow::before{content:'';width:24px;height:2px;background:#c0202a;border-radius:2px}
.car-hero h1{font-size:clamp(44px,6vw,80px);font-weight:900;line-height:1.0;letter-spacing:-.03em;color:#fff;margin-bottom:24px}
.car-hero h1 em{color:#e0263a;font-style:normal}
.car-hero-sub{font-size:17px;line-height:1.8;color:rgba(200,215,235,.7);max-width:520px;font-weight:300;margin-bottom:40px}
.car-btns{display:flex;gap:14px;flex-wrap:wrap}
.car-btn-r{display:inline-flex;align-items:center;gap:8px;background:#c0202a;color:#fff;padding:14px 30px;border-radius:50px;font-weight:700;font-size:14px;text-decoration:none;transition:background .2s,box-shadow .2s}
.car-btn-r:hover{background:#e0263a;box-shadow:0 0 28px rgba(192,32,42,.5)}
.car-btn-g{display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,.08);color:#fff;padding:14px 30px;border-radius:50px;font-weight:600;font-size:14px;text-decoration:none;border:1.5px solid rgba(255,255,255,.2);transition:all .2s}
.car-btn-g:hover{background:rgba(255,255,255,.14);border-color:rgba(255,255,255,.5)}
.car-stats{display:flex;gap:0;margin-top:64px;padding-top:40px;border-top:1px solid rgba(255,255,255,.1)}
.car-stat{padding-right:40px;border-right:1px solid rgba(255,255,255,.1)}
.car-stat:last-child{border-right:none;padding-left:40px;padding-right:0}
.car-stat:not(:first-child){padding-left:40px}
.car-stat-v{font-size:36px;font-weight:900;color:#fff;line-height:1;letter-spacing:-.02em}
.car-stat-v em{color:#e0263a;font-style:normal}
.car-stat-l{font-size:10px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:rgba(200,215,235,.5);margin-top:5px}
.car-sec{padding:100px 0}
.car-con{max-width:1200px;margin:0 auto;padding:0 44px}
.car-lbl{display:inline-flex;align-items:center;gap:8px;font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:#c0202a;margin-bottom:16px}
.car-lbl::before{content:'';width:20px;height:2px;background:#c0202a;border-radius:2px;flex-shrink:0}
.car-h2{font-size:clamp(30px,4vw,50px);font-weight:900;line-height:1.05;letter-spacing:-.03em;color:#1a1e2e;margin-bottom:16px}
.car-h2 em{color:#e0263a;font-style:normal}
.car-h2w{color:#fff}
.car-p{font-size:16px;line-height:1.8;color:#4a5470;font-weight:300}
.car-pw{color:rgba(200,215,235,.75)}
.car-split{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center}
.car-img-wrap{position:relative;overflow:hidden}
.car-img-wrap img{width:100%;height:480px;object-fit:cover;display:block}
.car-img-badge{position:absolute;bottom:24px;left:24px;right:24px;background:rgba(0,0,0,.75);backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.1);padding:16px 20px;display:flex;align-items:center;gap:20px}
.car-badge-val{font-size:28px;font-weight:900;color:#fff;line-height:1}
.car-badge-val em{font-size:14px;color:rgba(200,215,235,.5);font-style:normal;font-weight:400}
.car-badge-lbl{font-size:9px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:rgba(200,215,235,.45);margin-top:3px}
.car-badge-div{width:1px;height:36px;background:rgba(255,255,255,.15);flex-shrink:0}
.car-values{display:grid;grid-template-columns:1fr 1fr;gap:0;margin-top:52px;border:1px solid #e0e4ef}
.car-val{padding:36px 32px;border-right:1px solid #e0e4ef;border-bottom:1px solid #e0e4ef;position:relative;overflow:hidden;transition:background .2s}
.car-val:hover{background:#fff}
.car-val:nth-child(2n){border-right:none}
.car-val:nth-last-child(-n+2){border-bottom:none}
.car-val-num{font-size:60px;font-weight:900;color:rgba(192,32,42,.06);line-height:1;position:absolute;top:12px;right:16px;letter-spacing:-.04em}
.car-val-icon{width:44px;height:44px;background:rgba(192,32,42,.08);border-radius:10px;display:flex;align-items:center;justify-content:center;margin-bottom:18px}
.car-val-icon svg{width:20px;height:20px;stroke:#c0202a;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.car-val-t{font-size:16px;font-weight:800;color:#1a1e2e;margin-bottom:8px;letter-spacing:-.01em}
.car-val-d{font-size:13px;line-height:1.75;color:#4a5470}
.car-perks{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:#e0e4ef;border:1px solid #e0e4ef;margin-top:52px}
.car-perk{background:#fff;padding:0;overflow:hidden;transition:background .2s}
.car-perk:hover{background:#f5f6fa}
.car-perk-img{height:150px;overflow:hidden}
.car-perk-img img{width:100%;height:100%;object-fit:cover;transition:transform .4s;filter:brightness(.9)}
.car-perk:hover .car-perk-img img{transform:scale(1.05);filter:brightness(1)}
.car-perk-body{padding:22px 24px 26px}
.car-perk-t{font-size:15px;font-weight:800;color:#1a1e2e;margin-bottom:8px;letter-spacing:-.01em}
.car-perk-d{font-size:13px;line-height:1.7;color:#4a5470}
.car-life{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:240px 240px;gap:10px;margin-top:52px}
.car-life-img{overflow:hidden;position:relative}
.car-life-img img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .5s}
.car-life-img:hover img{transform:scale(1.05)}
.car-life-img.tall{grid-row:span 2}
.car-jobs-wrap{margin-top:52px}
.car-dept-lbl{font-size:10px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:#e0263a;padding:24px 0 12px;border-bottom:2px solid #c0202a;margin-bottom:0}
.car-job{display:flex;align-items:center;justify-content:space-between;padding:20px 0;border-bottom:1px solid rgba(255,255,255,.08);gap:20px;transition:padding .15s}
.car-job:hover{padding-left:8px}
.car-job-t{font-size:15px;font-weight:700;color:#fff;margin-bottom:8px;letter-spacing:-.01em}
.car-job-tags{display:flex;gap:6px;flex-wrap:wrap}
.car-jtag{font-size:10px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;padding:3px 10px;border-radius:4px}
.car-jtag-d{background:rgba(192,32,42,.15);color:#ff3b4e}
.car-jtag-t{background:rgba(255,255,255,.08);color:rgba(200,215,235,.75)}
.car-jtag-l{background:rgba(255,255,255,.05);color:rgba(200,215,235,.5)}
.car-job-btn{display:inline-flex;align-items:center;gap:6px;background:transparent;color:#fff;border:1px solid rgba(255,255,255,.2);padding:9px 18px;border-radius:50px;font-size:11px;font-weight:700;text-decoration:none;white-space:nowrap;transition:all .15s;letter-spacing:.06em;text-transform:uppercase}
.car-job-btn:hover{background:#c0202a;border-color:#c0202a}
.car-apply-grid{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:start}
.car-process{margin-top:28px;border:1px solid #e0e4ef}
.car-step{display:flex;align-items:flex-start;gap:14px;padding:18px 20px;border-bottom:1px solid #e0e4ef}
.car-step:last-child{border-bottom:none}
.car-step-n{width:30px;height:30px;border-radius:50%;background:#c0202a;color:#fff;font-size:12px;font-weight:800;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px}
.car-step-t{font-size:13px;font-weight:700;color:#1a1e2e;margin-bottom:2px}
.car-step-d{font-size:12px;color:#8a93b0}
.car-form-box{background:#fff;border:1px solid #e0e4ef;padding:40px}
.car-form-box h3{font-size:22px;font-weight:900;color:#1a1e2e;margin-bottom:6px;letter-spacing:-.02em}
.car-form-sub{font-size:13px;color:#8a93b0;margin-bottom:28px}
.car-form-row{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.car-fg{margin-bottom:18px}
.car-fg label{display:block;font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#4a5470;margin-bottom:7px}
.car-fg input,.car-fg select,.car-fg textarea{width:100%;padding:12px 16px;border:1.5px solid #e0e4ef;background:#f5f6fa;font-family:'Inter',sans-serif;font-size:14px;color:#1a1e2e;outline:none;transition:border-color .2s,background .2s;border-radius:0}
.car-fg input:focus,.car-fg select:focus,.car-fg textarea:focus{border-color:#c0202a;background:#fff}
.car-fg textarea{height:110px;resize:vertical}
.car-upload{border:2px dashed #e0e4ef;padding:24px;text-align:center;cursor:pointer;transition:all .2s;background:#f5f6fa}
.car-upload:hover{border-color:#c0202a;background:rgba(192,32,42,.03)}
.car-upload-t{font-size:14px;font-weight:600;color:#1a1e2e;margin-bottom:4px}
.car-upload-s{font-size:12px;color:#8a93b0}
.car-submit{width:100%;padding:15px;background:#c0202a;color:#fff;border:none;font-family:'Inter',sans-serif;font-size:15px;font-weight:700;cursor:pointer;border-radius:50px;transition:background .2s,box-shadow .2s;margin-top:8px}
.car-submit:hover{background:#e0263a;box-shadow:0 0 28px rgba(192,32,42,.4)}
@media(max-width:1024px){.car-split{grid-template-columns:1fr;gap:40px}.car-values{grid-template-columns:1fr}.car-val:nth-child(2n){border-right:1px solid #e0e4ef}.car-val:nth-last-child(-n+2){border-bottom:1px solid #e0e4ef}.car-val:last-child{border-bottom:none}.car-perks{grid-template-columns:repeat(2,1fr)}.car-apply-grid{grid-template-columns:1fr;gap:40px}}
@media(max-width:768px){.car-hero-inner{padding:100px 20px 60px}.car-con{padding:0 20px}.car-sec{padding:64px 0}.car-stats{flex-wrap:wrap}.car-stat{flex:0 0 50%;padding:16px 0;border-right:none;border-bottom:1px solid rgba(255,255,255,.1)}.car-stat:nth-child(odd){border-right:1px solid rgba(255,255,255,.1)}.car-stat:last-child,.car-stat:nth-last-child(2):nth-child(odd){border-bottom:none}.car-perks{grid-template-columns:1fr}.car-life{grid-template-columns:1fr 1fr;grid-template-rows:auto}.car-life-img.tall{grid-row:span 1;height:200px}.car-life-img{height:200px}.car-form-row{grid-template-columns:1fr}.car-form-box{padding:24px}.car-btns{flex-direction:column}.car-btn-r,.car-btn-g{justify-content:center;text-align:center}}
@media(max-width:480px){.car-life{grid-template-columns:1fr}.car-values{grid-template-columns:1fr}}
</style>
</head>
<body>
<div id="nav-placeholder"></div>
"""
