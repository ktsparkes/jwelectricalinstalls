"""Builds a clickable preview for GitHub Pages: index.html + preview/*.html (placeholder images)."""
import os, re, glob
from PIL import Image, ImageDraw
from config import BASE, UPLOADS
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "preview"); os.makedirs(os.path.join(P, "img"), exist_ok=True)
files = sorted(glob.glob(os.path.join(ROOT, "pages", "*.html")))
slug2file = {}
for f in files:
    n = os.path.basename(f)[3:-5]
    slug2file["" if n == "home" else n] = os.path.basename(f)
NAV = [("Home", ""), ("About", "about"), ("Services", "services"), ("Projects", "projects"), ("Contact Us", "contact-us")]
def link(slug):
    slug = slug.strip("/")
    return slug2file.get(slug, slug2file.get(slug.split("/")[-1], "01-home.html"))
names = set()
for f in files:
    h = open(f).read()
    names |= set(re.findall(re.escape(UPLOADS) + r"([\w\-\.]+)", h))
    h = h.replace(UPLOADS, "img/")
    h = re.sub(re.escape(BASE) + r"/([\w\-/]*)", lambda m: link(m.group(1)), h)
    h = re.sub(r'href="/([\w\-]+)/"', lambda m: f'href="{link(m.group(1))}"', h)
    nav = "".join(f'<a href="{link(s)}">{t}</a>' for t, s in NAV)
    head = f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PREVIEW - J.W Electrical</title>
<style>body{{margin:0;font-family:'DM Sans',sans-serif}}.pv{{position:sticky;top:0;z-index:999;background:#fff;border-bottom:1px solid #eee;display:flex;align-items:center;justify-content:space-between;padding:14px 24px;flex-wrap:wrap;gap:10px}}.pv b{{font-family:Outfit,sans-serif;font-size:20px}}.pv nav{{display:flex;gap:18px;flex-wrap:wrap}}.pv a{{color:#1c1c1c;text-decoration:none;font-weight:600}}.pv .tel{{background:#8C6420;color:#fff;padding:8px 14px;border-radius:6px}}.pvnote{{background:#fff7e0;font-size:13px;padding:6px 24px;text-align:center}}</style></head><body>
<div class="pvnote">PREVIEW ONLY - placeholder images, header/footer stand-ins. The real header and footer come from BeTheme on WordPress.</div>
<div class="pv"><b>J.W Electrical</b><nav>{nav}<a class="tel" href="tel:07742924814">07742 924814</a></nav></div>'''
    foot = '<div style="background:#1C1C1C;color:#ccc;padding:40px 24px;text-align:center;font-size:14px">Footer (contact form + Get In Touch widgets go here on WordPress) | <a style="color:#C9973F" href="23-privacy-policy.html">Privacy</a> | <a style="color:#C9973F" href="24-cookie-policy.html">Cookies</a></div></body></html>'
    open(os.path.join(P, os.path.basename(f)), "w").write(head + h + foot)
for i, n in enumerate(sorted(names)):
    im = Image.new("RGB", (800, 600), (60 + i * 9 % 50, 52 + i * 7 % 40, 40 + i * 5 % 30))
    d = ImageDraw.Draw(im); d.text((24, 24), "PHOTO: " + n, fill=(220, 200, 160))
    im.save(os.path.join(P, "img", n), "PNG" if n.endswith(".png") else "JPEG", quality=60)
rows = "".join(f'<li><a href="preview/{os.path.basename(f)}">{os.path.basename(f)[3:-5].replace("-", " ").title()}</a></li>' for f in files)
open(os.path.join(ROOT, "index.html"), "w").write(f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>J.W Electrical - Site Preview</title>
<style>body{{font-family:system-ui,sans-serif;max-width:720px;margin:40px auto;padding:0 20px;color:#1c1c1c}}h1{{font-size:28px}}li{{margin:8px 0}}a{{color:#8C6420;font-weight:600}}</style></head><body>
<h1>J.W Electrical - Site Preview</h1><p>Click any page. Images are placeholders until the real photos are uploaded.</p><ol>{rows}</ol></body></html>''')
print("preview built:", len(files), "pages,", len(names), "placeholder images")
