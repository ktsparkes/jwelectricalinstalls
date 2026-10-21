# Design system. Written with the blueprint's bp- prefix; build.py converts it to jw-.
GLOBAL = r"""
:root{
  --bp-primary:#8C6420; --bp-primary-rgb:140,100,32;
  --bp-primary-dark:#6F4F18;
  --bp-primary-deep:#171717; --bp-primary-deep-rgb:23,23,23;
  --bp-primary-light:#C9973F; --bp-primary-light-rgb:201,151,63;
  --bp-pale:#F4ECDD; --bp-wash:#FAF7F2;
  --bp-ink:#111111; --bp-text:#1C1C1C; --bp-muted:#5E5A52;
  --bp-call:#25D366; --bp-star:#C9973F;
  --bp-font-head:'Outfit',sans-serif; --bp-font-body:'DM Sans',sans-serif;
  --bp-border:rgba(var(--bp-primary-rgb),.14);
  --bp-shadow-md:0 8px 30px rgba(var(--bp-primary-deep-rgb),.10);
  --bp-shadow-lg:0 20px 60px rgba(var(--bp-primary-deep-rgb),.14);
  --bp-ease:cubic-bezier(.16,1,.3,1);
}
html,body{overflow-x:hidden!important}
.bp-page{width:100vw!important;max-width:100vw!important;margin-left:calc(50% - 50vw)!important;margin-right:calc(50% - 50vw)!important;font-family:var(--bp-font-body);color:var(--bp-text)}
.bp-page,.bp-page *{box-sizing:border-box}
.bp-page section{position:relative}
.bp-page h1,.bp-page h2,.bp-page h3,.bp-page h4{font-family:var(--bp-font-head);color:inherit}
.bp-page img{max-width:100%;height:auto}
.bp-section-label{font-family:var(--bp-font-head);font-weight:700;font-size:.78rem;letter-spacing:.15em;text-transform:uppercase;color:var(--bp-primary);margin:0 0 16px;display:block}
.bp-btn-primary,.bp-btn-secondary,.bp-btn-solid{display:inline-flex;align-items:center;justify-content:center;gap:10px;font-family:var(--bp-font-head);font-size:1rem;padding:16px 36px;border-radius:50px;text-decoration:none!important;transition:all .3s ease;cursor:pointer}
.bp-btn-primary{font-weight:700;color:var(--bp-primary-deep)!important;background:#fff;border:none}
.bp-btn-primary:hover{transform:translateY(-2px);box-shadow:0 10px 35px rgba(255,255,255,.25)}
.bp-btn-secondary{font-weight:600;color:#fff!important;background:transparent;border:2px solid rgba(255,255,255,.35)}
.bp-btn-secondary:hover{border-color:#fff;background:rgba(255,255,255,.1)}
.bp-btn-solid{font-weight:700;color:#fff!important;background:var(--bp-primary);border:none}
.bp-btn-solid:hover{background:var(--bp-primary-dark);transform:translateY(-2px)}
.fade-up,.fade-left,.fade-right,.scale-in{opacity:0;transition:opacity .8s var(--bp-ease),transform .8s var(--bp-ease)}
.fade-up{transform:translateY(50px)}
.fade-left{transform:translateX(-60px)}
.fade-right{transform:translateX(60px)}
.scale-in{transform:scale(.85);transition-duration:.7s}
.fade-up.visible,.fade-left.visible,.fade-right.visible,.scale-in.visible{opacity:1;transform:none}
.delay-1{transition-delay:.1s}.delay-2{transition-delay:.2s}.delay-3{transition-delay:.3s}.delay-4{transition-delay:.4s}
.delay-5{transition-delay:.5s}.delay-6{transition-delay:.6s}.delay-7{transition-delay:.7s}.delay-8{transition-delay:.8s}
@keyframes bpSlideUp{to{opacity:1;transform:translateY(0)}}
@keyframes bpFadeIn{to{opacity:1}}
@keyframes bpPulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.5;transform:scale(1.3)}}
@media(max-width:768px){.fade-left,.fade-right{transform:translateY(35px)}}
@media(prefers-reduced-motion:reduce){.fade-up,.fade-left,.fade-right,.scale-in{opacity:1;transform:none;transition:none}}
.bp-sticky-btns{position:fixed;bottom:24px;right:24px;z-index:9999;display:flex;flex-direction:column;gap:12px;align-items:flex-end}
.bp-sticky-btn{width:52px;height:52px;border-radius:50%;display:flex;align-items:center;justify-content:center;text-decoration:none;transition:all .3s var(--bp-ease);box-shadow:0 4px 20px rgba(var(--bp-primary-deep-rgb),.25);position:relative}
.bp-sticky-btn:hover{transform:scale(1.12);box-shadow:0 6px 28px rgba(var(--bp-primary-deep-rgb),.35)}
.bp-sticky-btn::before{content:attr(data-label);position:absolute;right:calc(100% + 10px);top:50%;transform:translateY(-50%);background:var(--bp-ink);color:#fff;font:600 .75rem var(--bp-font-head);padding:6px 12px;border-radius:6px;white-space:nowrap;opacity:0;pointer-events:none;transition:opacity .25s ease}
.bp-sticky-btn:hover::before{opacity:1}
.bp-sticky-phone{background:var(--bp-call)}
.bp-sticky-email{background:var(--bp-primary)}
.bp-sticky-form{background:var(--bp-primary-deep)}
@media(max-width:500px){.bp-sticky-btns{bottom:16px;right:16px;gap:10px}.bp-sticky-btn{width:46px;height:46px}.bp-sticky-btn::before{display:none}}
"""

C = {}

C["hero"] = r"""
.bp-hero{min-height:82vh;display:flex;align-items:center;overflow:hidden;padding:0!important}
.bp-hero-bg{position:absolute;inset:0;background-size:cover;background-position:center;background-color:var(--bp-primary-deep)}
img.bp-hero-bg{width:100%;height:100%;object-fit:cover;max-width:none}
.bp-hero-overlay{position:absolute;inset:0;background:linear-gradient(135deg,rgba(var(--bp-primary-deep-rgb),.72) 0%,rgba(var(--bp-primary-deep-rgb),.45) 50%,rgba(var(--bp-primary-rgb),.22) 100%)}
.bp-hero-content{position:relative;z-index:2;width:100%;max-width:1280px;margin:0 auto;padding:90px 40px}
.bp-hero-badge{display:inline-flex;align-items:center;gap:9px;padding:9px 20px;border-radius:50px;background:rgba(255,255,255,.12);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.25);color:#fff;font:700 15px var(--bp-font-head);letter-spacing:.08em;text-transform:uppercase;margin-bottom:28px;opacity:0;animation:bpFadeIn .8s .3s forwards}
.bp-hero-badge::before{content:"";width:9px;height:9px;border-radius:50%;background:var(--bp-primary-light);animation:bpPulse 2s infinite}
.bp-hero h1{color:#fff;font-size:clamp(48px,7vw,96px);font-weight:900;line-height:1.05;letter-spacing:-.04em;max-width:1100px;margin:0 0 22px;opacity:0;transform:translateY(30px);animation:bpSlideUp .9s .5s forwards}
.bp-hero h1 em{font-style:normal;color:var(--bp-primary-light)}
.bp-hero-sub{color:rgba(255,255,255,.9);font-size:20px;line-height:1.7;max-width:640px;margin:0 0 40px;opacity:0;transform:translateY(30px);animation:bpSlideUp .9s .7s forwards}
.bp-hero-ctas{display:flex;gap:16px;flex-wrap:wrap;opacity:0;transform:translateY(30px);animation:bpSlideUp .9s 1s forwards}
.bp-hero-crumb{font:600 .85rem var(--bp-font-head);color:rgba(255,255,255,.7);margin:0 0 18px;display:flex;align-items:center;gap:8px;opacity:0;animation:bpFadeIn .8s .15s forwards}
.bp-hero-crumb a{color:rgba(255,255,255,.7);text-decoration:none}
.bp-hero-crumb a:hover{color:#fff}
.bp-hero--loc{min-height:76vh}
.bp-hero--loc h1{font-size:clamp(2.8rem,6.4vw,5.2rem);letter-spacing:-.03em}
@media(min-width:769px) and (max-width:1180px){.bp-hero{min-height:680px}.bp-hero h1{font-size:clamp(58px,7vw,82px)}.bp-hero--loc h1{font-size:clamp(2.8rem,6.4vw,5.2rem)}}
@media(max-width:768px){
  .bp-hero{min-height:auto;padding:135px 0 110px!important}
  .bp-hero-content{padding:0 22px}
  .bp-hero-badge{font-size:12px;padding:8px 14px;margin-bottom:20px}
  .bp-hero h1{font-size:clamp(42px,12vw,56px);line-height:1.03}
  .bp-hero-sub{font-size:17px;line-height:1.65}
  .bp-hero-ctas .bp-btn-primary,.bp-hero-ctas .bp-btn-secondary{width:100%;max-width:340px}
}
@media(max-width:500px){.bp-hero--loc h1{font-size:clamp(2.4rem,12vw,3.6rem)}.bp-hero-ctas{flex-direction:column;align-items:stretch}}
"""

C["heroproj"] = r"""
.bp-hero-proj{position:relative;min-height:62vh;display:flex;align-items:flex-end;overflow:hidden}
.bp-hero-proj-bg{position:absolute;inset:0;background:linear-gradient(135deg,var(--bp-primary-deep) 0%,#2a241a 60%,var(--bp-primary) 100%)}
.bp-hero-proj-img{position:absolute;inset:0;width:100%!important;height:100%!important;max-width:none!important;object-fit:cover;display:block}
.bp-hero-proj-overlay{position:absolute;inset:0;background:linear-gradient(0deg,rgba(17,17,17,.8) 0%,rgba(var(--bp-primary-deep-rgb),.4) 55%,rgba(var(--bp-primary-rgb),.1) 100%)}
.bp-hero-proj-content{position:relative;z-index:2;max-width:1280px;margin:0 auto;padding:0 40px 56px;width:100%}
.bp-hero-crumb{font:600 .85rem var(--bp-font-head);color:rgba(255,255,255,.7);margin:0 0 18px;display:flex;align-items:center;gap:8px;opacity:0;animation:bpFadeIn .8s .15s forwards}
.bp-hero-crumb a{color:rgba(255,255,255,.7);text-decoration:none}
.bp-hero-proj-tag{display:inline-block;font:700 .78rem var(--bp-font-head);letter-spacing:.1em;text-transform:uppercase;color:#fff;background:var(--bp-primary);padding:6px 16px;border-radius:30px;margin-bottom:20px;opacity:0;animation:bpFadeIn .8s .25s forwards}
.bp-hero-proj h1{font-weight:900;font-size:clamp(2.2rem,5vw,3.8rem);line-height:1.08;color:#fff;margin:0 0 16px;letter-spacing:-.03em;max-width:16ch;opacity:0;transform:translateY(30px);animation:bpSlideUp .9s .35s forwards}
.bp-hero-proj .bp-hero-sub{color:rgba(255,255,255,.9);font-size:1.05rem;line-height:1.7;max-width:560px;margin:0;opacity:0;transform:translateY(30px);animation:bpSlideUp .9s .5s forwards}
@media(max-width:768px){.bp-hero-proj{min-height:54vh}.bp-hero-proj-content{padding:0 24px 40px}}
@media(max-width:480px){.bp-hero-proj h1{font-size:clamp(2rem,10vw,2.8rem)}}
"""

C["circles"] = r"""
.bp-circles{z-index:3;margin-top:-90px;padding:0 40px 45px}
.bp-circles-grid{max-width:1100px;margin:auto;display:grid;grid-template-columns:repeat(4,1fr);gap:36px}
.bp-circle-card{display:flex;flex-direction:column;align-items:center;text-align:center;color:var(--bp-text)!important;text-decoration:none!important}
.bp-circle-img{width:180px;height:180px;border-radius:50%;overflow:hidden;border:5px solid #fff;box-shadow:0 10px 40px rgba(var(--bp-primary-deep-rgb),.16);margin-bottom:20px;transition:.35s;background:var(--bp-pale)}
.bp-circle-img img{width:100%!important;height:100%!important;object-fit:cover!important;display:block}
.bp-circle-card:hover .bp-circle-img{transform:translateY(-7px) scale(1.03)}
.bp-circle-card h3{font-size:17px;font-weight:700;margin:0}
@media(max-width:1024px){.bp-circles-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:768px){.bp-circles{margin-top:-55px;padding:0 24px 50px;background:#fff}.bp-circles-grid{gap:35px 20px}.bp-circle-img{width:132px;height:132px}.bp-circle-card h3{font-size:15px}}
@media(max-width:420px){.bp-circle-img{width:min(118px,34vw);height:min(118px,34vw)}}
"""

C["intro"] = r"""
.bp-intro{background:#fff;padding:70px 48px 78px}
.bp-intro-inner{max-width:950px;margin:auto;text-align:center}
.bp-intro--narrow .bp-intro-inner{max-width:800px}
.bp-intro h2{font-size:clamp(38px,4.8vw,64px);font-weight:800;line-height:1.12;letter-spacing:-.035em;margin:0 0 30px;color:var(--bp-text)}
.bp-intro p:not(.bp-section-label){font-size:1.1rem;line-height:1.85;color:var(--bp-muted);margin:0 0 18px}
.bp-intro a{color:var(--bp-primary);text-decoration:underline;text-underline-offset:3px}
.bp-intro a:hover{color:var(--bp-primary-dark)}
.bp-credential{display:inline-block;text-align:left;margin-top:28px;padding:22px 28px;background:var(--bp-wash);border-left:4px solid var(--bp-primary);border-radius:4px;font-size:.98rem;line-height:1.75;color:var(--bp-text)}
.bp-credential strong{display:block;font:700 1rem var(--bp-font-head);color:var(--bp-primary);margin-bottom:6px}
@media(max-width:768px){.bp-intro{padding:52px 24px 60px}.bp-intro h2{font-size:35px}.bp-intro p:not(.bp-section-label){font-size:17px;line-height:1.75}}
"""

C["about"] = r"""
.bp-about{padding:95px 40px;background:var(--bp-primary-deep);overflow:hidden}
.bp-about::before{content:'';position:absolute;top:-200px;right:-200px;width:600px;height:600px;border-radius:50%;background:radial-gradient(circle,rgba(var(--bp-primary-light-rgb),.12) 0%,transparent 70%)}
.bp-about-inner{max-width:1280px;margin:auto;display:grid;grid-template-columns:1fr 1fr;gap:70px;align-items:center;position:relative}
.bp-about .bp-section-label{color:var(--bp-primary-light)}
.bp-about h2{font-size:clamp(42px,4.8vw,74px);font-weight:800;line-height:1.05;letter-spacing:-.04em;color:#fff;margin:0 0 28px}
.bp-about-text p:not(.bp-section-label){font-size:18px;line-height:1.85;color:rgba(255,255,255,.82);margin:0 0 22px}
.bp-about-text a{color:var(--bp-primary-light);text-decoration:underline}
.bp-about-stats{display:grid;grid-template-columns:repeat(2,1fr);gap:22px;margin-top:38px}
.bp-stat-box{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);border-radius:24px;padding:30px 16px;text-align:center}
.bp-stat-number{font:900 46px var(--bp-font-head);color:#fff}
.bp-stat-label{font-size:15px;color:rgba(255,255,255,.7);margin-top:8px}
.bp-about-image{position:relative}
.bp-about-image-main{border-radius:30px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.3);background:#2a2a2a}
.bp-about-image-main img{width:100%;height:620px;object-fit:cover;display:block}
.bp-about-accent{position:absolute;left:-25px;bottom:35px;width:120px;height:120px;border-radius:25px;background:var(--bp-primary);display:flex;align-items:center;justify-content:center;text-align:center;color:#fff}
.bp-about-accent strong{display:block;font:900 34px var(--bp-font-head)}
.bp-about-accent small{font:700 12px var(--bp-font-head);text-transform:uppercase;letter-spacing:.1em}
@media(max-width:768px){
  .bp-about{padding:75px 24px}
  .bp-about-inner{display:flex;flex-direction:column;align-items:stretch;gap:38px}
  .bp-about-text{width:100%;min-width:0}.bp-stat-box{min-width:0;overflow-wrap:anywhere}
  .bp-about h2{font-size:42px}.bp-about-image{width:100%}.bp-about-image-main img{height:auto;aspect-ratio:4/5}
  .bp-about-accent{left:18px;bottom:18px;width:95px;height:95px}.bp-about-accent strong{font-size:28px}
  .bp-about-stats{gap:14px}.bp-stat-box{padding:24px 10px}.bp-stat-number{font-size:36px}.bp-stat-label{font-size:13px}
}
"""

C["overview"] = r"""
.bp-overview{padding:88px 48px;background:var(--bp-primary-deep);overflow:hidden}
.bp-overview::before{content:'';position:absolute;top:-200px;right:-200px;width:600px;height:600px;border-radius:50%;background:radial-gradient(circle,rgba(var(--bp-primary-light-rgb),.12) 0%,transparent 70%)}
.bp-overview-inner{max-width:1320px;margin:0 auto;display:grid;grid-template-columns:1fr 1.1fr;gap:84px;align-items:center;position:relative}
.bp-split-img{border-radius:20px;overflow:hidden;box-shadow:var(--bp-shadow-lg);background:var(--bp-pale)}
.bp-split-img img{width:100%;height:100%;object-fit:cover;display:block;aspect-ratio:4/3}
.bp-overview .bp-split-img{background:#2a2a2a}
.bp-overview .bp-section-label{color:var(--bp-primary-light)}
.bp-overview h2{font-weight:800;font-size:clamp(2.2rem,4vw,3.4rem);color:#fff;line-height:1.12;margin:0 0 24px;letter-spacing:-.03em}
.bp-overview p:not(.bp-section-label){font-size:1.05rem;line-height:1.85;color:rgba(255,255,255,.75);margin:0 0 14px}
.bp-overview a{color:var(--bp-primary-light);text-decoration:underline;text-underline-offset:3px}
@media(max-width:1024px){.bp-overview-inner{grid-template-columns:1fr;gap:44px}}
@media(max-width:768px){.bp-overview{padding:60px 22px}.bp-split-img{border-radius:18px}}
"""

C["systems"] = r"""
.bp-systems{padding:88px 48px;background:#fff}
.bp-systems-inner{max-width:1320px;margin:0 auto;display:grid;grid-template-columns:1.1fr 1fr;gap:84px;align-items:center}
.bp-split-img{border-radius:20px;overflow:hidden;background:var(--bp-pale)}
.bp-split-img img{width:100%;height:100%;object-fit:cover;display:block;aspect-ratio:4/3}
.bp-systems .bp-split-img{box-shadow:var(--bp-shadow-md)}
.bp-systems h2{font-weight:800;font-size:clamp(2.2rem,4vw,3.4rem);color:var(--bp-text);line-height:1.12;margin:0 0 24px;letter-spacing:-.03em}
.bp-systems p{font-size:1.05rem;line-height:1.85;color:var(--bp-muted);margin:0 0 20px}
.bp-systems a{color:var(--bp-primary)}
.bp-system-list{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:20px}
.bp-system-list h3{font-weight:700;font-size:1.05rem;color:var(--bp-primary);margin:0 0 6px}
.bp-system-list p{font-size:.95rem;line-height:1.7;margin:0}
@media(max-width:1024px){.bp-systems-inner{grid-template-columns:1fr;gap:44px}.bp-systems .bp-split-img{order:-1}}
@media(max-width:768px){.bp-systems{padding:60px 22px}}
"""

C["why"] = r"""
.bp-why{padding:88px 48px;background:var(--bp-wash)}
.bp-why-inner{max-width:1100px;margin:0 auto}
.bp-why-header{text-align:center;margin-bottom:50px}
.bp-why h2{font-weight:800;font-size:clamp(2.4rem,4.8vw,4rem);color:var(--bp-text);letter-spacing:-.03em;line-height:1.12;margin:0}
.bp-why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:28px}
.bp-why-card{position:relative;background:#fff;border-radius:20px;padding:44px 36px;text-align:center;border:1px solid var(--bp-border);transition:all .4s var(--bp-ease);overflow:hidden}
.bp-why-card::before{content:'';position:absolute;top:0;left:0;right:0;height:4px;background:var(--bp-primary);transform:scaleX(0);transition:transform .4s ease}
.bp-why-card:hover::before{transform:scaleX(1)}
.bp-why-card:hover{transform:translateY(-6px);box-shadow:var(--bp-shadow-lg);border-color:transparent}
.bp-why-icon{width:72px;height:72px;margin:0 auto 24px;background:var(--bp-pale);border-radius:50%;display:flex;align-items:center;justify-content:center;transition:all .3s ease}
.bp-why-card:hover .bp-why-icon{background:var(--bp-primary)}
.bp-why-card:hover .bp-why-icon svg{stroke:#fff}
.bp-why-card h3{font-weight:700;font-size:1.15rem;color:var(--bp-text);margin:0 0 12px}
.bp-why-card p{font-size:.95rem;line-height:1.7;color:var(--bp-muted);margin:0}
@media(max-width:1024px){.bp-why-grid{grid-template-columns:1fr;max-width:560px;margin:0 auto}}
@media(max-width:768px){.bp-why{padding:60px 22px}.bp-why-card{padding:32px 24px}}
"""

C["why4"] = r"""
.bp-why4{padding:75px 40px;background:#fff}
.bp-why4-inner{max-width:1320px;margin:0 auto}
.bp-why4 h2{font-weight:800;font-size:clamp(2.2rem,4.4vw,3.6rem);color:var(--bp-text);letter-spacing:-.03em;line-height:1.12;text-align:center;margin:0 0 50px}
.bp-why4-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:24px}
.bp-why4-card{background:var(--bp-wash);border-radius:20px;padding:36px 28px;text-align:center;transition:all .4s var(--bp-ease)}
.bp-why4-card:hover{transform:translateY(-6px);box-shadow:var(--bp-shadow-lg)}
.bp-why4-icon{width:60px;height:60px;margin:0 auto 20px;background:var(--bp-pale);border-radius:50%;display:flex;align-items:center;justify-content:center}
.bp-why4-card h3{font-weight:700;font-size:1.05rem;color:var(--bp-text);margin:0 0 10px}
.bp-why4-card p{font-size:.92rem;line-height:1.65;color:var(--bp-muted);margin:0}
@media(max-width:1024px){.bp-why4-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:600px){.bp-why4-grid{grid-template-columns:1fr}}
@media(max-width:768px){.bp-why4{padding:60px 18px}}
"""

C["services"] = r"""
.bp-services{padding:110px 40px;background:var(--bp-wash)}
.bp-services-inner{max-width:1320px;margin:auto}
.bp-services-header{text-align:center;max-width:820px;margin:0 auto 65px}
.bp-services-header h2{font-size:clamp(42px,5vw,70px);font-weight:800;letter-spacing:-.05em;line-height:.98;color:var(--bp-text);margin:0 0 22px}
.bp-services-sub{color:var(--bp-muted);font-size:18px;line-height:1.8;margin:0}
.bp-services-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:32px}
.bp-service-card{display:flex;flex-direction:column;background:#fff;border-radius:28px;overflow:hidden;box-shadow:0 12px 35px rgba(var(--bp-primary-deep-rgb),.07);color:var(--bp-text)!important;text-decoration:none!important;transition:.3s}
.bp-service-card:hover{transform:translateY(-5px);box-shadow:0 20px 45px rgba(var(--bp-primary-deep-rgb),.14)}
.bp-service-card-img{width:100%;height:300px;background-size:cover;background-position:center;background-color:var(--bp-pale);flex-shrink:0}
.bp-service-card-body{padding:34px;flex:1;display:flex;flex-direction:column}
.bp-service-card h3{font-size:28px;font-weight:700;line-height:1.1;margin:0 0 18px}
.bp-service-card p{font-size:17px;line-height:1.8;color:var(--bp-muted);margin:0 0 22px}
.bp-service-card span{margin-top:auto;color:var(--bp-primary);font:700 16px var(--bp-font-head)}
@media(max-width:1024px){.bp-services-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.bp-services-grid .bp-service-card:last-child:nth-child(odd){grid-column:1/-1;width:calc(50% - 16px);margin:auto}}
@media(max-width:768px){.bp-services{padding:70px 18px}.bp-services-header{margin-bottom:40px}.bp-services-header h2{font-size:42px}.bp-services-grid{grid-template-columns:1fr;gap:28px}.bp-services-grid .bp-service-card:last-child:nth-child(odd){grid-column:auto;width:100%}.bp-service-card-img{height:230px}.bp-service-card-body{padding:30px 26px}.bp-service-card h3{font-size:26px}}
"""

C["locservices"] = r"""
.bp-locservices{padding:100px 40px;background:var(--bp-wash)}
.bp-locservices-inner{max-width:1320px;margin:auto}
.bp-locservices-header{text-align:center;max-width:820px;margin:0 auto 60px}
.bp-locservices-header h2{font-size:clamp(38px,3.6vw,60px);font-weight:800;line-height:.98;letter-spacing:-.04em;color:var(--bp-text);margin:0 0 24px}
.bp-locservices-header .bp-sub{font-size:18px;line-height:1.8;color:var(--bp-muted);margin:0}
.bp-locservices-grid{display:flex;flex-wrap:wrap;justify-content:center;gap:32px}
.bp-locservice-card{background:#fff;border-radius:28px;overflow:hidden;display:flex;flex-direction:column;box-shadow:0 12px 35px rgba(var(--bp-primary-deep-rgb),.07);flex:0 1 calc(25% - 24px);min-width:250px;text-decoration:none!important;color:inherit!important;transition:.3s}
.bp-locservice-card:hover{transform:translateY(-5px)}
.bp-locservice-card-icon{height:150px;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,var(--bp-pale) 0%,var(--bp-wash) 100%)}
.bp-locservice-card-body{padding:28px;flex:1;display:flex;flex-direction:column}
.bp-tag{display:inline-block;font:700 11px var(--bp-font-head);letter-spacing:.08em;text-transform:uppercase;color:var(--bp-primary);background:var(--bp-pale);padding:4px 10px;border-radius:20px;margin-bottom:12px;width:fit-content}
.bp-locservice-card h3{font-size:21px;line-height:1.1;font-weight:700;color:var(--bp-text);margin:0 0 10px}
.bp-locservice-card p{font-size:15px;line-height:1.7;color:var(--bp-muted);margin:0}
@media(max-width:1024px){.bp-locservice-card{flex:0 1 calc(50% - 16px)}}
@media(max-width:768px){.bp-locservices{padding:60px 18px}.bp-locservices-header h2{font-size:36px}.bp-locservices-grid{gap:24px}.bp-locservice-card{flex:0 1 100%;border-radius:24px}}
"""

C["projects"] = r"""
.bp-projects{padding:75px 40px;background:#fff}
.bp-projects-inner{max-width:1320px;margin:0 auto}
.bp-projects-header{text-align:center;margin-bottom:50px}
.bp-projects h2{font-weight:800;font-size:clamp(2.4rem,4.8vw,4rem);color:var(--bp-text);letter-spacing:-.03em;line-height:1.12;margin:0}
.bp-projects-sub{max-width:650px;margin:16px auto 0;font-size:1.05rem;line-height:1.85;color:var(--bp-muted)}
.bp-projects-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));grid-template-rows:360px 360px;gap:18px}
.bp-proj{border-radius:20px;overflow:hidden;position:relative;display:block;text-decoration:none;background:var(--bp-pale)}
.bp-proj img{width:100%!important;height:100%!important;object-fit:cover;display:block;transition:transform .7s var(--bp-ease)}
.bp-proj:hover img{transform:scale(1.08)}
.bp-proj--wide{grid-column:span 2}
.bp-proj-overlay{position:absolute;inset:0;background:linear-gradient(to top,rgba(17,17,17,.85) 0%,rgba(17,17,17,.1) 50%,transparent 100%);display:flex;flex-direction:column;justify-content:flex-end;padding:28px;opacity:0;transition:opacity .4s ease}
.bp-proj:hover .bp-proj-overlay{opacity:1}
.bp-proj-overlay h3{font-weight:700;font-size:1.15rem;color:#fff;margin:0 0 4px}
.bp-proj-overlay span{font-size:.85rem;color:rgba(255,255,255,.75)}
@media(max-width:1024px){.bp-projects-grid{grid-template-columns:repeat(2,1fr);grid-template-rows:none}.bp-proj,.bp-proj--wide{grid-column:auto;height:320px}}
@media(max-width:768px){.bp-projects{padding:60px 18px}.bp-projects-grid{grid-template-columns:1fr;gap:22px}.bp-proj,.bp-proj--wide{height:285px}.bp-proj-overlay{opacity:1}}
"""

C["process"] = r"""
.bp-process{padding:75px 40px;background:var(--bp-primary-deep);overflow:hidden}
.bp-process::before{content:'';position:absolute;top:-200px;right:-200px;width:600px;height:600px;border-radius:50%;background:radial-gradient(circle,rgba(var(--bp-primary-light-rgb),.12) 0%,transparent 70%)}
.bp-process-inner{max-width:1320px;margin:0 auto;position:relative;z-index:1}
.bp-process-header{text-align:center;margin-bottom:60px}
.bp-process .bp-section-label{color:var(--bp-primary-light)}
.bp-process h2{font-weight:800;font-size:clamp(2.4rem,4.8vw,4rem);color:#fff;letter-spacing:-.03em;line-height:1.12;margin:0}
.bp-process-sub{max-width:700px;margin:16px auto 0;font-size:1.05rem;line-height:1.85;color:rgba(255,255,255,.7)}
.bp-process-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:32px}
.bp-process-step{text-align:center}
.bp-process-num{width:64px;height:64px;margin:0 auto 20px;background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.15);border-radius:50%;display:flex;align-items:center;justify-content:center;font:800 1.4rem var(--bp-font-head);color:var(--bp-primary-light);transition:all .3s ease}
.bp-process-step:hover .bp-process-num{background:var(--bp-primary);border-color:var(--bp-primary);color:#fff;transform:translateY(-4px)}
.bp-process-step h3{font-weight:700;font-size:1.15rem;color:#fff;margin:0 0 10px}
.bp-process-step p{font-size:.95rem;line-height:1.7;color:rgba(255,255,255,.65);margin:0}
.bp-process-step a{color:var(--bp-primary-light)}
@media(max-width:1024px){.bp-process-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:600px){.bp-process-grid{grid-template-columns:1fr}}
@media(max-width:768px){.bp-process{padding:60px 18px}}
"""

C["included"] = r"""
.bp-included{padding:88px 48px;background:var(--bp-wash)}
.bp-included-inner{max-width:1040px;margin:0 auto;text-align:center}
.bp-included h2{font-weight:800;font-size:clamp(2rem,4vw,3rem);color:var(--bp-text);line-height:1.12;margin:0 0 48px;letter-spacing:-.03em}
.bp-checklist{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:16px 32px;text-align:left}
.bp-checklist li{font-size:1rem;line-height:1.6;color:var(--bp-text);display:flex;align-items:flex-start;gap:12px}
.bp-checklist li::before{content:'';width:20px;height:20px;min-width:20px;border-radius:50%;margin-top:3px;background:var(--bp-primary) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'/%3E%3C/svg%3E") center/12px no-repeat}
@media(max-width:600px){.bp-checklist{grid-template-columns:1fr}.bp-included{padding:60px 22px}}
"""

C["icongrid"] = r"""
.bp-icongrid{padding:88px 48px;background:#fff}
.bp-icongrid-inner{max-width:1320px;margin:0 auto}
.bp-icongrid-header{text-align:center;margin-bottom:52px}
.bp-icongrid-header h2{font-weight:800;font-size:clamp(2rem,4vw,3rem);color:var(--bp-text);line-height:1.12;margin:0;letter-spacing:-.03em}
.bp-icongrid-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.bp-icon-card{border:1.5px solid var(--bp-border);border-radius:16px;padding:36px 24px;text-align:center;transition:all .35s var(--bp-ease);background:#fff}
.bp-icon-card:hover{border-color:var(--bp-primary);box-shadow:var(--bp-shadow-md);transform:translateY(-4px)}
.bp-icon-card svg{width:60px;height:60px;margin:0 auto 18px;display:block}
.bp-icon-card h3{font-weight:700;font-size:1rem;color:var(--bp-text);margin:0}
@media(max-width:1024px){.bp-icongrid-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:480px){.bp-icongrid-grid{grid-template-columns:1fr}}
@media(max-width:768px){.bp-icongrid{padding:60px 22px}}
"""

C["reviews"] = r"""
.bp-reviews{background:var(--bp-wash);padding:88px 48px}
.bp-reviews-inner{max-width:1320px;margin:0 auto}
.bp-reviews-header{text-align:center;max-width:760px;margin:0 auto 40px}
.bp-reviews-header h2{font-size:clamp(34px,5vw,64px);font-weight:800;color:var(--bp-text);line-height:1.12;margin:0 0 12px}
.bp-reviews-header p:not(.bp-section-label){color:var(--bp-muted);font-size:1.05rem;line-height:1.7}
.bp-reviews-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.bp-review-card{background:#fff;border-radius:16px;padding:36px;box-shadow:0 4px 18px rgba(0,0,0,.06);border-top:4px solid var(--bp-primary);display:flex;flex-direction:column}
.bp-review-text{font-size:1rem;line-height:1.7;margin:0 0 18px;flex:1;color:var(--bp-text);font-style:italic}
.bp-review-meta{font-size:14px;color:var(--bp-muted)}
.bp-review-meta strong{color:var(--bp-text);display:block}
.bp-reviews-link{text-align:center;margin-top:32px}
.bp-reviews-link a{color:var(--bp-primary);font-weight:700}
@media(max-width:900px){.bp-reviews-grid{grid-template-columns:1fr;max-width:600px;margin:0 auto}.bp-reviews{padding:56px 20px}.bp-review-card{padding:28px}}
"""

C["faq"] = r"""
.bp-faq{padding:90px 48px;background:#fff}
.bp-faq-inner{max-width:950px;margin:auto}
.bp-faq-header{text-align:center;margin-bottom:42px}
.bp-faq-header h2{font-size:clamp(2rem,4vw,3rem);font-weight:800;color:var(--bp-text);margin:0}
.bp-faq-item{border:1px solid #ece4d6;border-radius:14px;margin-bottom:14px;background:#fff;overflow:hidden}
.bp-faq--wash .bp-faq-item{background:var(--bp-wash);border:none;border-radius:16px}
.bp-faq-item summary{padding:22px 25px;font:700 1.1rem var(--bp-font-head);color:var(--bp-text);cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:20px}
.bp-faq-item summary::-webkit-details-marker{display:none}
.bp-faq-item summary::after{content:'+';color:var(--bp-primary);font-size:1.3rem;transition:transform .25s ease}
.bp-faq-item[open] summary::after{transform:rotate(45deg)}
.bp-faq-item summary:hover{color:var(--bp-primary)}
.bp-faq-item p{padding:0 25px 24px;margin:0;color:var(--bp-muted);font-size:1rem;line-height:1.75}
.bp-faq-item a{color:var(--bp-primary)}
@media(max-width:768px){.bp-faq{padding:60px 20px}.bp-faq-item summary{padding:18px 20px;font-size:.98rem}.bp-faq-item p{padding:0 20px 20px}}
"""

C["areas"] = r"""
.bp-areas{background:var(--bp-wash);padding:88px 48px}
.bp-areas-card{max-width:1180px;margin:0 auto;background:#fff;border-radius:28px;padding:64px 48px;text-align:center;box-shadow:0 2px 14px rgba(23,23,23,.04)}
.bp-areas-card .bp-section-label{color:var(--bp-primary);letter-spacing:4px;font-size:14px}
.bp-areas-card h2{font-weight:800;font-size:clamp(32px,4.5vw,58px);line-height:1.1;color:var(--bp-text);letter-spacing:-1px;margin:0 0 18px}
.bp-areas-sub{font-size:18px;color:var(--bp-muted);margin:0 0 32px;line-height:1.7}
.bp-areas-chips{display:flex;flex-wrap:wrap;justify-content:center;gap:16px}
.bp-areas-chips a{font:600 17px var(--bp-font-head);color:var(--bp-text)!important;text-decoration:none!important;border:2px solid var(--bp-primary);border-radius:40px;padding:14px 28px;background:var(--bp-wash);transition:all .2s ease}
.bp-areas-chips a:hover,.bp-areas-chips a:focus{background:var(--bp-primary);color:#fff!important;transform:translateY(-2px)}
@media(max-width:768px){.bp-areas{padding:56px 16px}.bp-areas-card{padding:40px 20px;border-radius:20px}.bp-areas-chips{gap:10px}.bp-areas-chips a{font-size:15px;padding:11px 20px}}
"""

C["locareas"] = r"""
.bp-locareas{padding:75px 40px;background:var(--bp-wash)}
.bp-locareas-panel{max-width:1000px;margin:0 auto;background:#fff;border:1px solid var(--bp-border);border-radius:24px;padding:48px 52px;text-align:center}
.bp-locareas-panel h2{font-weight:800;font-size:clamp(1.9rem,3.4vw,2.6rem);color:var(--bp-text);letter-spacing:-.03em;margin:0 0 12px}
.bp-locareas-panel > p:not(.bp-section-label){font-size:1.02rem;color:var(--bp-muted);max-width:55ch;margin:0 auto 28px}
.bp-locareas-list{display:flex;flex-wrap:wrap;justify-content:center;gap:12px}
.bp-chip{font:600 .92rem var(--bp-font-head);padding:10px 20px;border-radius:30px;background:var(--bp-wash);color:var(--bp-text);border:1.5px solid var(--bp-primary-light)}
.bp-chip--hq{background:var(--bp-primary);color:#fff;border-color:var(--bp-primary)}
@media(max-width:768px){.bp-locareas{padding:60px 18px}.bp-locareas-panel{padding:32px 22px}}
"""

C["cta"] = r"""
.bp-cta{padding:84px 48px;background:var(--bp-primary-deep);text-align:center;overflow:hidden}
.bp-cta::before{content:'';position:absolute;top:-150px;left:50%;transform:translateX(-50%);width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,rgba(var(--bp-primary-light-rgb),.12) 0%,transparent 70%)}
.bp-cta-inner{max-width:700px;margin:0 auto;position:relative;z-index:1}
.bp-cta h2{font-weight:800;font-size:clamp(2rem,4vw,3rem);color:#fff;margin:0 0 16px;letter-spacing:-.03em;line-height:1.15}
.bp-cta p{font-size:1.05rem;color:rgba(255,255,255,.75);margin:0 0 36px;line-height:1.7}
.bp-cta-btns{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}
@media(max-width:768px){.bp-cta{padding:60px 22px}.bp-cta-btns{flex-direction:column;align-items:center}.bp-cta-btns a{width:100%;max-width:320px}}
"""

C["ctacard"] = r"""
.bp-ctacard{padding:70px 40px 90px;background:var(--bp-wash)}
.bp-ctacard-inner{max-width:1100px;margin:0 auto;background:linear-gradient(135deg,#2a2218 0%,var(--bp-primary-deep) 100%);border-radius:28px;padding:56px 60px;display:flex;align-items:center;justify-content:space-between;gap:32px;flex-wrap:wrap;border:1px solid rgba(var(--bp-primary-light-rgb),.3)}
.bp-ctacard h2{font-weight:800;font-size:clamp(1.5rem,2.8vw,2.1rem);color:#fff;max-width:34ch;letter-spacing:-.02em;line-height:1.2;margin:0}
.bp-ctacard-ctas{display:flex;gap:14px;flex-wrap:wrap}
@media(max-width:768px){.bp-ctacard{padding:60px 18px 70px}.bp-ctacard-inner{padding:40px 32px;flex-direction:column;align-items:flex-start}.bp-ctacard-ctas{width:100%;flex-direction:column}.bp-ctacard-ctas a{width:100%}}
"""

C["ratingstrip"] = r"""
.bp-ratingstrip{padding:75px 40px;background:#fff;text-align:center}
.bp-ratingstrip h2{font-size:clamp(26px,3vw,34px);font-weight:800;margin:0 0 22px;color:var(--bp-text)}
.bp-ratingstrip blockquote{max-width:720px;margin:0 auto 28px;font-size:1.2rem;line-height:1.7;font-style:italic;color:var(--bp-text)}
.bp-ratingstrip cite{display:block;margin-top:12px;font:700 .85rem var(--bp-font-head);font-style:normal;letter-spacing:.08em;text-transform:uppercase;color:var(--bp-primary)}
.bp-ratingstrip-link{display:inline-block;border:2px solid var(--bp-primary);border-radius:50px;padding:14px 28px;color:var(--bp-primary)!important;font:700 16px var(--bp-font-head);text-decoration:none!important;transition:.3s}
.bp-ratingstrip-link:hover{background:var(--bp-primary);color:#fff!important}
@media(max-width:768px){.bp-ratingstrip{padding:65px 24px 90px}}
"""

C["projpage"] = r"""
.bp-projfacts{padding:0 40px;margin-top:-44px;z-index:3}
.bp-projfacts-inner{max-width:1100px;margin:0 auto;background:#fff;border-radius:20px;box-shadow:var(--bp-shadow-lg);padding:32px 40px;display:grid;grid-template-columns:repeat(4,1fr);gap:24px}
.bp-projfact{display:flex;align-items:center;gap:14px}
.bp-projfact-icon{width:44px;height:44px;flex-shrink:0;border-radius:50%;background:var(--bp-pale);display:flex;align-items:center;justify-content:center}
.bp-projfact-label{font:700 .7rem var(--bp-font-head);letter-spacing:.08em;text-transform:uppercase;color:var(--bp-primary);margin:0 0 3px}
.bp-projfact-value{font-weight:500;font-size:.95rem;color:var(--bp-text);line-height:1.3;margin:0}
.bp-projstory{padding:80px 40px 20px;background:#fff}
.bp-projstory-inner{max-width:760px;margin:0 auto}
.bp-projstory h2{font-weight:800;font-size:clamp(1.9rem,3.6vw,2.8rem);color:var(--bp-text);line-height:1.15;margin:0 0 24px;letter-spacing:-.03em}
.bp-projstory p:not(.bp-section-label){font-size:1.08rem;line-height:1.85;color:var(--bp-muted);margin:0 0 20px}
.bp-projstory a{color:var(--bp-primary)}
.bp-projgallery{padding:40px 40px 90px;background:#fff}
.bp-projgallery-grid{max-width:1000px;margin:0 auto;display:grid;grid-template-columns:repeat(2,1fr);gap:24px}
.bp-projgallery-item{aspect-ratio:4/3;border-radius:18px;background:var(--bp-wash);overflow:hidden}
.bp-projgallery-item img{width:100%!important;height:100%!important;object-fit:cover;display:block}
.bp-projhighlight{padding:20px 40px 90px;background:var(--bp-wash)}
.bp-projhighlight-inner{max-width:1000px;margin:0 auto;background:#fff;border-radius:24px;padding:48px 52px;display:flex;align-items:center;gap:40px;flex-wrap:wrap}
.bp-projhighlight-icon{width:76px;height:76px;flex-shrink:0;border-radius:50%;background:var(--bp-pale);display:flex;align-items:center;justify-content:center}
.bp-projhighlight-body{flex:1;min-width:240px}
.bp-projhighlight-body h3{font-weight:800;font-size:1.5rem;color:var(--bp-text);margin:0 0 10px;letter-spacing:-.02em}
.bp-projhighlight-body p{font-size:1rem;line-height:1.75;color:var(--bp-muted);margin:0}
@media(max-width:1024px){.bp-projfacts-inner{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:768px){.bp-projfacts{padding:0 18px;margin-top:-32px}.bp-projfacts-inner{padding:26px;gap:22px}.bp-projstory{padding:56px 22px 10px}.bp-projhighlight{padding:10px 18px 60px}.bp-projhighlight-inner{padding:36px 28px;flex-direction:column;align-items:flex-start}}
@media(max-width:600px){.bp-projfacts-inner,.bp-projgallery-grid{grid-template-columns:1fr}.bp-projgallery{padding:20px 18px 60px}}
"""

C["projlist"] = r"""
.bp-projlist{padding:80px 20px;background:#fff}
.bp-projlist-inner{max-width:1200px;margin:0 auto}
.bp-projlist h2{font-weight:800;font-size:36px;color:var(--bp-ink);text-align:center;margin:0 0 40px}
.bp-projlist-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:28px}
.bp-projcard{display:block;background:#fff;border-radius:14px;overflow:hidden;box-shadow:0 6px 24px rgba(23,23,23,.08);text-decoration:none!important;color:inherit;transition:transform .25s,box-shadow .25s}
.bp-projcard:hover{transform:translateY(-4px);box-shadow:0 12px 32px rgba(23,23,23,.14)}
.bp-projcard img{width:100%!important;height:260px!important;object-fit:cover;display:block;margin:0!important;background:var(--bp-pale)}
.bp-projcard-body{padding:22px 24px 26px}
.bp-projcard-loc{font-size:13px;font-weight:600;color:var(--bp-primary);text-transform:uppercase;letter-spacing:1px;margin:0 0 6px}
.bp-projcard h3{font-weight:700;font-size:22px;color:var(--bp-ink);margin:0 0 10px}
.bp-projcard p{font-size:16px;line-height:1.6;color:#4a4740;margin:0 0 14px}
.bp-projcard-more{font-weight:600;color:var(--bp-primary)}
@media(max-width:768px){.bp-projlist{padding:56px 16px}.bp-projlist h2{font-size:28px}.bp-projlist-grid{grid-template-columns:1fr}.bp-projcard img{height:210px!important}}
"""

C["contact"] = r"""
.bp-contact{padding:75px 40px;background:#fff;scroll-margin-top:80px}
.bp-contact-inner{max-width:1140px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:start}
.bp-contact-info h2{font-weight:800;font-size:clamp(2.2rem,4vw,3.2rem);color:var(--bp-text);line-height:1.12;margin:0 0 20px;letter-spacing:-.03em}
.bp-contact-info h2 span{color:var(--bp-primary)}
.bp-contact-intro{font-size:1.05rem;line-height:1.85;color:var(--bp-muted);margin:0 0 36px}
.bp-info-cards{display:flex;flex-direction:column;gap:16px}
.bp-info-card{display:flex;align-items:center;gap:16px;background:var(--bp-wash);border:1px solid rgba(var(--bp-primary-rgb),.15);border-radius:14px;padding:18px 20px;transition:border-color .2s,box-shadow .2s;text-decoration:none!important;color:inherit}
.bp-info-card:hover{border-color:var(--bp-primary);box-shadow:0 4px 20px rgba(var(--bp-primary-rgb),.12)}
.bp-info-icon{width:46px;height:46px;background:var(--bp-primary);border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.bp-info-icon svg{width:20px;height:20px;fill:#fff}
.bp-info-label{font:700 .72rem var(--bp-font-head);letter-spacing:.12em;text-transform:uppercase;color:var(--bp-muted);margin-bottom:3px}
.bp-info-value{font:700 1.05rem var(--bp-font-head);color:var(--bp-text);overflow-wrap:anywhere}
.bp-coverage-box{margin-top:28px;background:var(--bp-pale);border-left:4px solid var(--bp-primary);border-radius:0 14px 14px 0;padding:18px 20px}
.bp-coverage-box p{font-size:.92rem;color:var(--bp-text);line-height:1.65;margin:0}
.bp-coverage-box a{color:var(--bp-primary);font-weight:600}
.bp-enquiry{margin-top:36px;padding-top:30px;border-top:1px solid rgba(var(--bp-primary-rgb),.15)}
.bp-enquiry h3{font-weight:800;font-size:clamp(1.45rem,2.5vw,1.8rem);line-height:1.3;color:var(--bp-text);margin:0 0 15px}
.bp-enquiry > p{font-size:.95rem;line-height:1.8;color:var(--bp-muted);margin:0 0 18px}
.bp-enquiry-list{display:flex;flex-direction:column;gap:16px}
.bp-enquiry-item{display:flex;gap:13px;align-items:flex-start}
.bp-enquiry-check{width:25px;height:25px;min-width:25px;border-radius:50%;background:var(--bp-pale);color:var(--bp-primary);display:flex;align-items:center;justify-content:center;font:800 .9rem var(--bp-font-head);margin-top:2px}
.bp-enquiry-item h4{font-weight:700;font-size:.96rem;color:var(--bp-text);margin:0 0 4px}
.bp-enquiry-item p{font-size:.9rem;line-height:1.65;color:var(--bp-muted);margin:0}
.bp-form-wrapper{background:var(--bp-wash);border:1px solid rgba(var(--bp-primary-rgb),.15);border-radius:20px;padding:40px 36px}
.bp-form-wrapper h2{font-weight:800;font-size:1.6rem;color:var(--bp-text);margin:0 0 22px}
.bp-form-field{margin-bottom:18px}
.bp-form-field label{display:block;font:700 .78rem var(--bp-font-head);letter-spacing:.08em;text-transform:uppercase;color:var(--bp-muted);margin-bottom:7px}
.bp-form-field input,.bp-form-field select,.bp-form-field textarea{display:block;width:100%;max-width:100%;padding:13px 14px;border:1.5px solid rgba(var(--bp-primary-rgb),.2);border-radius:10px;background:#fff;color:var(--bp-text);font:16px/1.4 var(--bp-font-body);outline:none;box-shadow:none;transition:border-color .2s ease,box-shadow .2s ease}
.bp-form-field select{cursor:pointer;min-height:50px}
.bp-form-field textarea{min-height:135px;resize:vertical}
.bp-form-field input:focus,.bp-form-field select:focus,.bp-form-field textarea:focus{border-color:var(--bp-primary);box-shadow:0 0 0 3px rgba(var(--bp-primary-rgb),.15)}
.bp-form-field ::placeholder{color:#9a9488}
.bp-submit-btn{width:100%;min-height:52px;border:none;border-radius:50px;background:var(--bp-primary);color:#fff;font:700 1rem var(--bp-font-head);letter-spacing:.03em;padding:15px 28px;cursor:pointer;transition:background .2s ease,transform .15s ease,opacity .2s ease}
.bp-submit-btn:hover{background:var(--bp-primary-dark);transform:translateY(-2px)}
.bp-submit-btn:disabled{opacity:.65;cursor:not-allowed;transform:none}
.bp-form-result{display:none;margin-top:18px;padding:14px 16px;border-radius:10px;font-size:.92rem;line-height:1.55}
.bp-form-result.success{display:block;background:#E8F7ED;border:1px solid #A9DFB8;color:#216B37}
.bp-form-result.error{display:block;background:#FFF0F0;border:1px solid #E9B0B0;color:#A12828}
.bp-botcheck{position:absolute!important;left:-9999px!important;width:1px!important;height:1px!important;opacity:0!important;pointer-events:none!important}
.bp-creviews{padding:75px 40px;background:var(--bp-wash)}
.bp-creviews-inner{max-width:1140px;margin:0 auto}
.bp-creviews h2{font-weight:800;font-size:clamp(2.2rem,4vw,3.4rem);color:var(--bp-text);letter-spacing:-.03em;text-align:center;margin:0 0 42px}
.bp-creview{max-width:720px;margin:0 auto;background:#fff;border:1px solid rgba(var(--bp-primary-rgb),.12);border-radius:20px;padding:36px 32px;text-align:center}
.bp-creview-text{font-size:1.1rem;line-height:1.75;color:var(--bp-text);font-style:italic;margin:0}
.bp-creview-author{margin:18px 0 0;font:700 .8rem var(--bp-font-head);color:var(--bp-primary);text-transform:uppercase;letter-spacing:.08em}
.bp-creviews-link{text-align:center;margin-top:28px}
.bp-creviews-link a{color:var(--bp-primary);font-weight:700}
.bp-guarantee{background:var(--bp-primary-deep);padding:56px 40px}
.bp-guarantee-inner{max-width:860px;margin:0 auto;display:flex;align-items:center;gap:36px;justify-content:center;flex-wrap:wrap}
.bp-guarantee-icon{width:80px;flex-shrink:0}
.bp-guarantee h2{font-weight:800;font-size:clamp(1.5rem,3vw,2rem);color:#fff;line-height:1.2;margin:0}
.bp-guarantee p{margin:10px 0 0;color:rgba(255,255,255,.75);font-size:.98rem}
.bp-guarantee a{color:var(--bp-primary-light);font-weight:700}
@media(max-width:1024px){.bp-contact-inner{grid-template-columns:1fr;gap:44px}}
@media(max-width:768px){.bp-contact,.bp-creviews,.bp-guarantee{padding-left:22px;padding-right:22px}.bp-contact{padding-top:60px;padding-bottom:60px}.bp-form-wrapper{padding:28px 20px}.bp-guarantee-inner{flex-direction:column;text-align:center}}
"""

C["legal"] = r"""
.bp-pp-hero{background:linear-gradient(135deg,var(--bp-primary-deep) 0%,#3a2f1d 60%,var(--bp-primary) 100%);padding:110px 48px 90px;text-align:center;color:#fff}
.bp-pp-label{font-size:13px;letter-spacing:3px;text-transform:uppercase;color:rgba(255,255,255,.75);margin:0 0 14px;font-weight:700}
.bp-pp-hero h1{font-weight:800;font-size:clamp(40px,6vw,72px);line-height:1.05;color:#fff;margin:0 0 18px}
.bp-pp-sub{font-size:18px;line-height:1.6;max-width:640px;margin:0 auto 22px;color:rgba(255,255,255,.9)}
.bp-pp-date{display:inline-block;font-size:14px;background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.3);border-radius:30px;padding:8px 18px;color:#fff}
.bp-pp-body{background:var(--bp-wash);padding:72px 48px 96px}
.bp-pp-wrap{max-width:860px;margin:0 auto}
.bp-pp-section{background:#fff;border-radius:14px;padding:36px 40px;margin-bottom:22px;box-shadow:0 4px 18px rgba(0,0,0,.05)}
.bp-pp-section h2{font-weight:700;font-size:26px;color:var(--bp-text);margin:0 0 16px;display:flex;align-items:center;gap:14px;line-height:1.2}
.bp-pp-num{font:700 14px var(--bp-font-head);color:#fff;background:var(--bp-primary);border-radius:8px;min-width:38px;height:38px;display:inline-flex;align-items:center;justify-content:center}
.bp-pp-section p,.bp-pp-section li{font-size:16px;line-height:1.7;color:#3f3b34}
.bp-pp-section p{margin:0 0 12px}
.bp-pp-section ul{list-style:none;margin:0 0 12px;padding:0}
.bp-pp-section li{position:relative;padding-left:26px;margin-bottom:10px}
.bp-pp-section li:before{content:'';position:absolute;left:4px;top:10px;width:9px;height:9px;border-radius:50%;background:var(--bp-primary)}
.bp-pp-section a{color:var(--bp-primary);font-weight:600;text-decoration:none}
.bp-pp-card{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:8px}
.bp-pp-card div{background:var(--bp-wash);border-left:4px solid var(--bp-primary);border-radius:8px;padding:14px 16px;font-size:15px;color:var(--bp-text);font-weight:500}
.bp-pp-card span{display:block;font-size:12px;letter-spacing:1.5px;text-transform:uppercase;color:#6e685d;margin-bottom:4px;font-weight:700}
.bp-pp-cta{text-align:center;background:var(--bp-primary-deep);border-radius:14px;padding:40px 32px;color:#fff;margin-top:34px}
.bp-pp-cta h2{font-weight:700;font-size:26px;color:#fff;margin:0 0 10px}
.bp-pp-cta p{color:rgba(255,255,255,.8);margin:0 0 20px;font-size:16px}
.bp-pp-cta a{display:inline-block;background:var(--bp-primary);color:#fff!important;font-weight:700;padding:14px 28px;border-radius:8px;text-decoration:none}
@media(max-width:768px){.bp-pp-hero{padding:80px 20px 64px}.bp-pp-body{padding:40px 16px 64px}.bp-pp-section{padding:26px 22px}.bp-pp-section h2{font-size:21px}.bp-pp-card{grid-template-columns:1fr}}
"""
