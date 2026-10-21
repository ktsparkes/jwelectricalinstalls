# HTML components (blueprint section 7). Written with bp- prefix; build converts to jw-.
import json
from config import *

IMAGES = {}  # filename -> description (collected for IMAGES-NEEDED.md)


def img(name, desc):
    IMAGES.setdefault(name, desc)
    return UPLOADS + name


def U(slug=""):
    return f"{BASE}/{slug}/" if slug else f"{BASE}/"


ICONS = {
    "home": '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
    "bungalow": '<path d="M2 12l10-7 10 7"/><path d="M4 11v9h16v-9"/><path d="M10 20v-5h4v5"/>',
    "period": '<path d="M3 21V10l9-7 9 7v11z"/><path d="M16 6V3h2v4.5"/><path d="M9 21v-6h6v6"/>',
    "flats": '<rect x="4" y="2" width="16" height="20" rx="1"/><path d="M8 6h2M14 6h2M8 10h2M14 10h2M8 14h2M14 14h2M10 22v-4h4v4"/>',
    "garage": '<path d="M3 21V9l9-5 9 5v12"/><path d="M6 21v-8h12v8M6 16h12"/>',
    "gardenroom": '<rect x="3" y="8" width="18" height="12" rx="1"/><path d="M2 8h20"/><path d="M7 12h4v4H7zM14 12h3v8"/>',
    "building": '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M12 6h.01M16 6h.01M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M16 14h.01"/>',
    "shop": '<path d="M3 9l1.5-5h15L21 9"/><path d="M4 9v11h16V9"/><path d="M3 9h18"/><path d="M9 20v-6h6v6"/>',
    "factory": '<path d="M2 20V9l6 4V9l6 4V4h8v16z"/><path d="M2 20h20"/>',
    "barn": '<path d="M3 21V10l9-7 9 7v11z"/><path d="M8 21v-7h8v7"/><path d="M8 14l8 7M16 14l-8 7"/>',
    "stable": '<path d="M3 21V9l9-6 9 6v12"/><path d="M7 21v-8h10v8"/><path d="M7 16h10"/>',
    "coffee": '<path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><path d="M6 1v3M10 1v3M14 1v3"/>',
    "tool": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    "tree": '<circle cx="12" cy="9" r="6"/><path d="M12 15v7M9 22h6"/>',
    "drop": '<path d="M12 2.7l5.7 5.7a8 8 0 1 1-11.3 0z"/>',
    "monitor": '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/>',
    "check": '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    "pin": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    "message": '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>',
    "user": '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "tag": '<path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/>',
    "bulb": '<path d="M9 18h6M10 22h4M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.2 1 2V18h6v-1.3c0-.8.4-1.5 1-2A7 7 0 0 0 12 2z"/>',
    "socket": '<rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="12" cy="12" r="5"/><path d="M10 11v1.5M14 11v1.5"/>',
    "thermo": '<path d="M14 14.76V3.5a2.5 2.5 0 0 0-5 0v11.26a4.5 4.5 0 1 0 5 0z"/>',
    "zap": '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
    "search": '<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>',
    "layers": '<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>',
    "cable": '<path d="M3 6h5a4 4 0 0 1 4 4v4a4 4 0 0 0 4 4h5"/><circle cx="3" cy="6" r="1.5"/><circle cx="21" cy="18" r="1.5"/>',
    "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
    "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
}


def icon(name, size=32, sw=1.8, color="var(--bp-primary)"):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'style="color:{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{ICONS[name]}</svg>')


ARROW = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'


def btn(href, label, kind="primary", arrow=False):
    return f'<a href="{href}" class="bp-btn-{kind}">{label}{" " + ARROW if arrow else ""}</a>'


QUOTE_BTN = lambda: btn(U("contact-us"), "Get a Free Quote", "primary", True)
CALL_BTN = lambda: btn(f"tel:{PHONE_RAW}", f"Call {PHONE_DISPLAY}", "secondary")


def sticky(form_href=None):
    form_href = form_href or U("contact-us")
    return f'''<div class="bp-sticky-btns" aria-label="Quick contact options">
  <a href="tel:{PHONE_RAW}" class="bp-sticky-btn bp-sticky-phone" data-label="Call Us" aria-label="Call {BUSINESS}"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg></a>
  <a href="mailto:{EMAIL}" class="bp-sticky-btn bp-sticky-email" data-label="Email Us" aria-label="Email {BUSINESS}"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg></a>
  <a href="{form_href}" class="bp-sticky-btn bp-sticky-form" data-label="Contact Form" aria-label="Go to contact form"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></a>
</div>'''


# ---------- HEROES ----------
def hero(h1, sub, image, alt, badge=None, ctas=None, crumb=None, loc=False, use_img=False):
    ctas = ctas or [QUOTE_BTN(), btn(U("services"), "All Services", "secondary")]
    bg = (f'<img class="bp-hero-bg" src="{image}" alt="{alt}" fetchpriority="high">' if use_img else
          f'<div class="bp-hero-bg" role="img" aria-label="{alt}" style="background-image:url(\'{image}\')"></div>')
    b = f'\n    <div class="bp-hero-badge">{badge}</div>' if badge else ""
    c = f'\n    <p class="bp-hero-crumb"><a href="{U()}">Home</a> &nbsp;/&nbsp; {crumb}</p>' if crumb else ""
    return f'''<section class="bp-hero{' bp-hero--loc' if loc else ''}" aria-labelledby="hero-heading">
  {bg}
  <div class="bp-hero-overlay"></div>
  <div class="bp-hero-content">{c}{b}
    <h1 id="hero-heading">{h1}</h1>
    <p class="bp-hero-sub">{sub}</p>
    <div class="bp-hero-ctas">
      {"".join(ctas)}
    </div>
  </div>
</section>'''


def hero_proj(h1, sub, tag, crumb_last, image=None, alt=""):
    im = f'\n    <img class="bp-hero-proj-img" src="{image}" alt="{alt}">' if image else ""
    mid = f'<a href="{U("projects")}">Projects</a> &nbsp;/&nbsp; {crumb_last}' if crumb_last != "Projects" else "Projects"
    return f'''<section class="bp-hero-proj" aria-labelledby="hero-heading">
  <div class="bp-hero-proj-bg">{im}
  </div>
  <div class="bp-hero-proj-overlay"></div>
  <div class="bp-hero-proj-content">
    <p class="bp-hero-crumb"><a href="{U()}">Home</a> &nbsp;/&nbsp; {mid}</p>
    <span class="bp-hero-proj-tag">{tag}</span>
    <h1 id="hero-heading">{h1}</h1>
    <p class="bp-hero-sub">{sub}</p>
  </div>
</section>'''


# ---------- SECTIONS ----------
def circles(items):  # items: list of service dicts
    cards = "\n    ".join(
        f'<a href="{U(s["slug"])}" class="bp-circle-card scale-in{" delay-"+str(i) if i else ""}"><div class="bp-circle-img"><img src="{s["card_img"]}" alt="{s["card_alt"]}" loading="lazy"></div><h3>{s["short"]}</h3></a>'
        for i, s in enumerate(items))
    return f'''<section class="bp-circles" aria-label="Our specialist services">
  <div class="bp-circles-grid">
    {cards}
  </div>
</section>'''


def intro(paras, label=None, h2=None, hid="intro-heading", extra="", narrow=False):
    lab = f'\n    <p class="bp-section-label fade-up">{label}</p>' if label else ""
    h = f'\n    <h2 class="fade-up delay-1" id="{hid}">{h2}</h2>' if h2 else ""
    ps = "\n    ".join(f'<p class="fade-up delay-{min(i+2,4)}">{p}</p>' for i, p in enumerate(paras))
    aria = f' aria-labelledby="{hid}"' if h2 else ' aria-label="Introduction"'
    return f'''<section class="bp-intro{' bp-intro--narrow' if narrow else ''}"{aria}>
  <div class="bp-intro-inner">{lab}{h}
    {ps}{extra}
  </div>
</section>'''


def credential(strong, text):
    return f'\n    <div class="bp-credential fade-up delay-3"><strong>{strong}</strong>{text}</div>'


def about_split(label, h2, paras, stats, image, alt, accent_big, accent_small):
    ps = "\n      ".join(f"<p>{p}</p>" for p in paras)
    st = "\n        ".join(f'<div class="bp-stat-box"><div class="bp-stat-number">{n}</div><div class="bp-stat-label">{l}</div></div>' for n, l in stats)
    return f'''<section class="bp-about" aria-labelledby="about-heading">
  <div class="bp-about-inner">
    <div class="bp-about-text fade-left">
      <p class="bp-section-label">{label}</p>
      <h2 id="about-heading">{h2}</h2>
      {ps}
      <div class="bp-about-stats">
        {st}
      </div>
    </div>
    <div class="bp-about-image fade-right">
      <div class="bp-about-image-main"><img src="{image}" alt="{alt}" loading="lazy"></div>
      <div class="bp-about-accent"><div><strong>{accent_big}</strong><small>{accent_small}</small></div></div>
    </div>
  </div>
</section>'''


def overview(label, h2, paras, image, alt):
    ps = "\n      ".join(f'<p class="fade-right delay-{i+2}">{p}</p>' for i, p in enumerate(paras))
    return f'''<section class="bp-overview">
  <div class="bp-overview-inner">
    <div class="bp-split-img fade-left delay-1"><img src="{image}" alt="{alt}" loading="lazy"></div>
    <div>
      <p class="bp-section-label fade-right">{label}</p>
      <h2 class="fade-right delay-1">{h2}</h2>
      {ps}
    </div>
  </div>
</section>'''


def systems(label, h2, lead, items, cross, image, alt):
    li = "\n        ".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in items)
    return f'''<section class="bp-systems">
  <div class="bp-systems-inner">
    <div class="bp-split-img fade-left delay-1"><img src="{image}" alt="{alt}" loading="lazy"></div>
    <div>
      <p class="bp-section-label fade-right">{label}</p>
      <h2 class="fade-right delay-1">{h2}</h2>
      <p class="fade-right delay-2">{lead}</p>
      <ul class="bp-system-list fade-right delay-3">
        {li}
      </ul>
      <p class="fade-right delay-4" style="margin-top:20px">{cross}</p>
    </div>
  </div>
</section>'''


def why3(label, h2, cards):
    cs = "\n      ".join(
        f'<article class="bp-why-card fade-up delay-{i+1}">\n        <div class="bp-why-icon">{icon(ic,32)}</div>\n        <h3>{t}</h3><p>{d}</p>\n      </article>'
        for i, (ic, t, d) in enumerate(cards))
    return f'''<section class="bp-why">
  <div class="bp-why-inner">
    <div class="bp-why-header">
      <p class="bp-section-label fade-up">{label}</p>
      <h2 class="fade-up delay-1">{h2}</h2>
    </div>
    <div class="bp-why-grid">
      {cs}
    </div>
  </div>
</section>'''


def why4(label, h2, cards):
    cs = "\n      ".join(
        f'<article class="bp-why4-card fade-up delay-{i+1}"><div class="bp-why4-icon">{icon(ic,26)}</div><h3>{t}</h3><p>{d}</p></article>'
        for i, (ic, t, d) in enumerate(cards))
    return f'''<section class="bp-why4">
  <div class="bp-why4-inner">
    <p class="bp-section-label fade-up" style="text-align:center">{label}</p>
    <h2 class="fade-up delay-1">{h2}</h2>
    <div class="bp-why4-grid">
      {cs}
    </div>
  </div>
</section>'''


def services_grid(services, sub, label="What We Offer", h2="Our Services"):
    cards = "\n      ".join(
        f'''<a href="{U(s["slug"])}" class="bp-service-card scale-in delay-{i%3+1}">
        <div class="bp-service-card-img" role="img" aria-label="{s["card_alt"]}" style="background-image:url('{s["card_img"]}')"></div>
        <div class="bp-service-card-body"><h3>{s["name"]}</h3><p>{s["card"]}</p><span>Learn more &rarr;</span></div>
      </a>''' for i, s in enumerate(services))
    return f'''<section class="bp-services" id="all-services" aria-labelledby="services-heading">
  <div class="bp-services-inner">
    <div class="bp-services-header">
      <p class="bp-section-label fade-up">{label}</p>
      <h2 class="fade-up delay-1" id="services-heading">{h2}</h2>
      <p class="bp-services-sub fade-up delay-2">{sub}</p>
    </div>
    <div class="bp-services-grid">
      {cards}
    </div>
  </div>
</section>'''


def locservices(town, h2, sub, cards):  # cards: (icon, tag, title, slug, desc)
    cs = "\n    ".join(
        f'''<a href="{U(slug)}" class="bp-locservice-card scale-in delay-{i+1}">
      <div class="bp-locservice-card-icon" role="img" aria-label="{t} icon">{icon(ic,42,1.6)}</div>
      <div class="bp-locservice-card-body"><span class="bp-tag">{tag}</span><h3>{t}</h3><p>{d}</p></div>
    </a>''' for i, (ic, tag, t, slug, d) in enumerate(cards))
    return f'''<section class="bp-locservices"><div class="bp-locservices-inner">
  <div class="bp-locservices-header">
    <p class="bp-section-label fade-up">What We Offer In {town}</p>
    <h2 class="fade-up delay-1">{h2}</h2>
    <p class="bp-sub fade-up delay-2">{sub}</p>
  </div>
  <div class="bp-locservices-grid">
    {cs}
  </div>
</div></section>'''


def projects_mosaic(sub, items):  # items: (img, alt, title, detail)
    out = []
    for i, (im, alt, t, d) in enumerate(items):
        wide = " bp-proj--wide" if i in (0, 5) else ""
        lazy = "" if i == 0 else ' loading="lazy"'
        out.append(f'<a href="{U("projects")}" class="bp-proj{wide} scale-in delay-{i+1}"><img src="{im}" alt="{alt}"{lazy}><div class="bp-proj-overlay"><h3>{t}</h3><span>{d}</span></div></a>')
    cs = "\n    ".join(out)
    return f'''<section class="bp-projects"><div class="bp-projects-inner">
  <div class="bp-projects-header">
    <p class="bp-section-label fade-up">Our Work</p>
    <h2 class="fade-up delay-1">Projects We're Proud Of</h2>
    <p class="bp-projects-sub fade-up delay-2">{sub}</p>
  </div>
  <div class="bp-projects-grid">
    {cs}
  </div>
</div></section>'''


def process(sub, steps):
    cs = "\n    ".join(f'<div class="bp-process-step fade-up delay-{i+1}"><div class="bp-process-num">{i+1}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))
    return f'''<section class="bp-process"><div class="bp-process-inner">
  <div class="bp-process-header">
    <p class="bp-section-label fade-up">How It Works</p>
    <h2 class="fade-up delay-1">Our Process</h2>
    <p class="bp-process-sub fade-up delay-2">{sub}</p>
  </div>
  <div class="bp-process-grid">
    {cs}
  </div>
</div></section>'''


def included(h2, items):
    li = "".join(f"<li>{x}</li>" for x in items)
    return f'''<section class="bp-included"><div class="bp-included-inner">
  <p class="bp-section-label fade-up">What's Included</p>
  <h2 class="fade-up delay-1">{h2}</h2>
  <ul class="bp-checklist fade-up delay-2">
    {li}
  </ul>
</div></section>'''


def icongrid(label, h2, items):
    cs = "\n    ".join(f'<div class="bp-icon-card scale-in delay-{i%3+1}">{icon(ic,60,1.5)}<h3>{t}</h3></div>' for i, (ic, t) in enumerate(items))
    return f'''<section class="bp-icongrid"><div class="bp-icongrid-inner">
  <div class="bp-icongrid-header"><p class="bp-section-label fade-up">{label}</p><h2 class="fade-up delay-1">{h2}</h2></div>
  <div class="bp-icongrid-grid">
    {cs}
  </div>
</div></section>'''


REVIEW_TEXT = "J.W Electrical provided exceptional service, and their attention to detail was impressive. I highly recommend them for any electrical needs."
REVIEW_NAME = "Robert W"


def reviews(h2="What Our Customers Say", sub="Our clients' satisfaction is paramount. Here's what one customer had to say about working with J.W Electrical."):
    return f'''<section class="bp-reviews"><div class="bp-reviews-inner">
  <div class="bp-reviews-header">
    <p class="bp-section-label fade-up">Customer Reviews</p>
    <h2 class="fade-up delay-1">{h2}</h2>
    <p class="fade-up delay-2">{sub}</p>
  </div>
  <div class="bp-reviews-grid">
    <div class="bp-review-card fade-up delay-1"><p class="bp-review-text">"{REVIEW_TEXT}"</p><div class="bp-review-meta"><strong>{REVIEW_NAME}</strong>{SHORT} customer</div></div>
  </div>
  <p class="bp-reviews-link"><a href="{GOOGLE}" target="_blank" rel="noopener">Read our reviews on Google &rarr;</a></p>
</div></section>'''


def faq(h2, items, wash=False):
    qs = "\n  ".join(f'<details class="bp-faq-item fade-up"><summary>{q}</summary><p>{a}</p></details>' for q, a in items)
    return f'''<section class="bp-faq{' bp-faq--wash' if wash else ''}"><div class="bp-faq-inner">
  <div class="bp-faq-header"><p class="bp-section-label fade-up">Frequently Asked Questions</p><h2 class="fade-up delay-1">{h2}</h2></div>
  {qs}
</div></section>'''


def free_quote_faq():
    return ("Do you offer free quotes?",
            f'Yes. Every quote is free and with no obligation. Call James on <a href="tel:{PHONE_RAW}">{PHONE_DISPLAY}</a> or <a href="{U("contact-us")}">fill in our contact form</a> and we\'ll get back to you as soon as possible.')


def areas(sub="Domestic, commercial and agricultural electrical work across Poole, Bournemouth, Christchurch and Dorset. Choose your area:"):
    chips = "".join(f'<a href="/{slug}/">{label}</a>' for label, slug in AREAS)
    return f'''<section class="bp-areas"><div class="bp-areas-card">
  <p class="bp-section-label">Coverage</p>
  <h2>Areas We Cover</h2>
  <p class="bp-areas-sub">{sub}</p>
  <div class="bp-areas-chips">
    {chips}
  </div>
</div></section>'''


def locareas(town, chips):
    cs = "".join(f'<span class="bp-chip{" bp-chip--hq" if i == 0 else ""}">{c}</span>' for i, c in enumerate(chips))
    return f'''<section class="bp-locareas"><div class="bp-locareas-panel fade-up">
  <p class="bp-section-label">Coverage</p>
  <h2>Areas We Cover Across {town}</h2>
  <p>We regularly work throughout {town}, including:</p>
  <div class="bp-locareas-list">{cs}</div>
</div></section>'''


def cta_banner(h2, p=None):
    p = p or "Get in touch for a free, no-obligation quote. We cover Poole, Bournemouth, Christchurch and the surrounding Dorset area."
    return f'''<section class="bp-cta"><div class="bp-cta-inner fade-up">
  <h2>{h2}</h2>
  <p>{p}</p>
  <div class="bp-cta-btns">
    {btn(U("contact-us"), "Get a Free Quote &rarr;")}
    {btn(f"tel:{PHONE_RAW}", f"Call {PHONE_DISPLAY}", "secondary")}
  </div>
</div></section>'''


def ctacard(h2):
    return f'''<section class="bp-ctacard"><div class="bp-ctacard-inner fade-up">
  <h2>{h2}</h2>
  <div class="bp-ctacard-ctas">
    {btn(U("contact-us"), "Request a Quote")}
    {btn(f"tel:{PHONE_RAW}", "Call Today", "secondary")}
  </div>
</div></section>'''


def ratingstrip():
    return f'''<section class="bp-ratingstrip"><div class="fade-up">
  <h2>What Our Customers Say</h2>
  <blockquote>"{REVIEW_TEXT}"<cite>{REVIEW_NAME}</cite></blockquote>
  <a href="{GOOGLE}" class="bp-ratingstrip-link" target="_blank" rel="noopener noreferrer">Read Our Google Reviews</a>
</div></section>'''


def projlist(cards):  # (slug, img, alt, loc, title, line)
    cs = "\n    ".join(
        f'<a class="bp-projcard" href="{U("projects/"+slug)}"><img src="{im}" alt="{alt}" loading="lazy"><div class="bp-projcard-body"><p class="bp-projcard-loc">{loc}</p><h3>{t}</h3><p>{line}</p><span class="bp-projcard-more">View project &rarr;</span></div></a>'
        for slug, im, alt, loc, t, line in cards)
    return f'''<section class="bp-projlist"><div class="bp-projlist-inner">
  <p class="bp-section-label" style="text-align:center">Case Studies</p>
  <h2>Completed Projects</h2>
  <div class="bp-projlist-grid">
    {cs}
  </div>
</div></section>'''


def schema(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, indent=2, ensure_ascii=False) + '\n</script>'


def business_schema(extra=None):
    o = {
        "@type": "Electrician",
        "@id": f"{BASE}/#business",
        "name": BUSINESS,
        "alternateName": SHORT,
        "url": U(),
        "telephone": PHONE_E164,
        "email": EMAIL,
        "image": img("jw-electrical-logo.png", "Logo (also upload in BeTheme Theme Options > Header > Logo). PNG with transparent background, at least 600px wide."),
        "logo": UPLOADS + "jw-electrical-logo.png",
        "founder": {"@type": "Person", "name": OWNER},
        "foundingDate": "2022",
        "address": {"@type": "PostalAddress", "addressLocality": "Poole", "addressRegion": "Dorset", "postalCode": POSTCODE, "addressCountry": "GB"},
        "areaServed": [{"@type": "City", "name": n} for n, _ in AREAS if n != "Dorset"] + [{"@type": "AdministrativeArea", "name": "Dorset"}],
        "sameAs": [GOOGLE],
    }
    if extra:
        o.update(extra)
    return o
