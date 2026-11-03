# Single source of truth for business details. Change here, re-run build.py.
DOMAIN = "www.jwelectricalinstalls.com"
BASE = "https://" + DOMAIN
BUSINESS = "J.W Electrical Installations"
SHORT = "J.W Electrical"
LEGAL = "James Watton trading as J.W Electrical Installations"
OWNER = "James Watton"
PHONE_DISPLAY = "07742 924814"
PHONE_RAW = "07742924814"
PHONE_E164 = "+447742924814"
EMAIL = "jwelectrical111@gmail.com"
ADDRESS = "Poole, Dorset BH15 3DE"
POSTCODE = "BH15 3DE"
GOOGLE = "https://share.google/38ttVE6QLstd7QR4P"
UPLOADS = "/wp-content/uploads/2026/10/"  # change if images are uploaded in a different month
WEB3FORMS_KEY = "YOUR_WEB3FORMS_ACCESS_KEY"
YEAR = "2026"
UPDATED = "October 2026"
JOB_TYPES = [
    "Additional sockets / power points", "Lighting (inside or outside)", "Full or partial rewire",
    "Fault finding / repairs", "Electric heating", "Conduit / containment",
    "Commercial / industrial work", "Agricultural / farm work", "Other",
]
AREAS = [  # (label, slug)
    ("Poole", "electrician-poole"), ("Bournemouth", "electrician-bournemouth"),
    ("Christchurch", "electrician-christchurch"), ("Broadstone", "electrician-broadstone"),
    ("Wimborne", "electrician-wimborne"), ("Ferndown", "electrician-ferndown"),
    ("Dorset", "electrician-dorset"),
]

# ---- Photos uploaded to WordPress (November 2026). Key = slot name used by the generator, value = real filename.
UPLOADED = "/wp-content/uploads/2026/11/"
SOCK = "Clutter-free-room-with-matte-black-sockets.png"
PHOTOS = {
    "jw-electrical-logo.png": "Transparent-JV-electrical-logo-cutout.png",
    "electrician-poole-dorset-hero.jpg": "james-outdoor-standing-hero.webp",
    "james-watton-jw-electrical.jpg": "james-arms-crossed-original-best.webp",
    "james-watton-about.jpg": "james-about-portrait-black-tshirt.webp",
    "about-jw-electrical-hero.jpg": "james-installing-ceiling-light.webp",
    "jw-electrical-at-work.jpg": "james-first-fix-rewiring.webp",
    "electrical-services-hero.jpg": "vaulted-ceiling-led-strip-pendant-lighting.webp",
    "contact-jw-electrical-hero.jpg": "james-installing-black-socket.webp",
    "domestic-electrician-hero.jpg": "kitchen-pendant-lighting-installation.webp",
    "domestic-electrician.jpg": "residential-renovation-project-exterior.webp",
    "domestic-electrician-detail.jpg": SOCK,
    "commercial-electrician-hero.jpg": "commercial-electrician-first-fix-cabling.webp",
    "commercial-electrician.jpg": "electrical-control-box-wiring-terminations.webp",
    "commercial-electrician-detail.jpg": "industrial-fused-isolator-power-sockets.webp",
    "house-rewiring-hero.jpg": "james-first-fix-rewiring.webp",
    "house-rewiring.jpg": "house-rewiring-first-fix-cables.webp",
    "house-rewiring-detail.jpg": "modern-consumer-unit-circuit-breakers.webp",
    "lighting-installation-hero.jpg": "james-installing-ceiling-light.webp",
    "lighting-installation.jpg": "vaulted-ceiling-recessed-spotlights.webp",
    "lighting-installation-detail.jpg": "vaulted-ceiling-led-strip-pendant-lighting.webp",
    "additional-sockets-hero.jpg": "james-installing-black-socket.webp",
    "additional-sockets.jpg": SOCK,
    "electrical-fault-finding-hero.jpg": "james-inspecting-consumer-unit.webp",
    "electrical-fault-finding.jpg": "led-lighting-driver-wiring-connections.webp",
    "electrical-fault-finding-detail.jpg": "modern-consumer-unit-circuit-breakers.webp",
    "conduit-containment-hero.jpg": "commercial-ceiling-cable-tray-installation.webp",
    "conduit-containment.jpg": "electrical-control-panel-cable-wiring.webp",
    "project-1.jpg": "vaulted-ceiling-led-strip-pendant-lighting.webp",
    "project-2.jpg": "electrical-control-box-wiring-terminations.webp",
    "project-3.jpg": "residential-renovation-project-exterior.webp",
    "project-4.jpg": "vaulted-ceiling-recessed-spotlights.webp",
    "project-5.jpg": "electrical-control-panel-cable-wiring.webp",
    "project-6.jpg": "commercial-ceiling-cable-tray-installation.webp",
}
# Stand-ins: real photos used in slots that still need a better, specific photo. (slot: filename)
STANDINS = {
    "agricultural-electrician-hero.jpg": "james-outdoor-standing-hero.webp",
    "agricultural-electrician.jpg": "industrial-fused-isolator-power-sockets.webp",
    "agricultural-electrician-detail.jpg": "electrical-control-panel-cable-wiring.webp",
    "electric-heating-hero.jpg": "james-inspecting-consumer-unit.webp",
    "electric-heating.jpg": "vaulted-ceiling-led-strip-pendant-lighting.webp",
    "electric-heating-detail.jpg": "modern-consumer-unit-circuit-breakers.webp",
    "additional-sockets-detail.jpg": "kitchen-pendant-lighting-installation.webp",
    "conduit-containment-detail.jpg": "industrial-fused-isolator-power-sockets.webp",
    "electrician-poole.jpg": "kitchen-pendant-lighting-installation.webp",
    "electrician-bournemouth.jpg": "vaulted-ceiling-recessed-spotlights.webp",
    "electrician-christchurch.jpg": "james-installing-ceiling-light.webp",
    "electrician-wimborne.jpg": "house-rewiring-first-fix-cables.webp",
    "electrician-ferndown.jpg": "commercial-ceiling-cable-tray-installation.webp",
    "electrician-broadstone.jpg": "james-installing-black-socket.webp",
    "electrician-dorset.jpg": "james-first-fix-rewiring.webp",
}
