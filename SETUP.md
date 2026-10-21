# J.W Electrical - WordPress Setup Checklist

Built exactly like KJM Roof & Build (BeTheme + one Custom HTML block per page).
Tick each step as you go.

## 1. Hostinger
- [ ] hPanel > Websites > Add website > WordPress
- [ ] Domain: jwelectricalinstalls.com (build on the temporary domain first, then point DNS from Wix/registrar when ready)
- [ ] SSL on, LiteSpeed Cache on

## 2. WordPress settings
- [ ] General: Site Title `J.W Electrical Installations`, Tagline `Electrician in Poole, Bournemouth & Dorset`
- [ ] Language English (UK), Timezone London, date `jS F Y`, week starts Monday
- [ ] WordPress Address + Site Address: `https://www.jwelectricalinstalls.com` (once the domain is live)
- [ ] Discussion: comments off
- [ ] Permalinks: Post name

## 3. Plugins
- [ ] Rank Math SEO, Site Kit by Google, LiteSpeed Cache, All-in-One WP Migration
- [ ] Delete Hello Dolly and any demo plugins

## 4. Theme
- [ ] Install BeTheme (needs its own licence)
- [ ] Upload + activate `wordpress/jw-child-theme.zip`
- [ ] Skip demo import (or delete its menus/pages after)

## 5. Theme Options (BeTheme)
- [ ] Layout: full width
- [ ] Header: Classic, full width, minimalist, sticky white, action button hidden
- [ ] Logo + sticky logo: `jw-electrical-logo.png`
- [ ] Colors > Menu highlight: **#8C6420**
- [ ] Footer: 2 columns (one-second / one-second), background **#1C1C1C**, back-to-top on, copyright bar hidden
- [ ] Custom CSS: paste `wordpress/theme-options-custom-css.css`
- [ ] Appearance > Customize > Additional CSS: paste `wordpress/customizer-additional-css.css`
- [ ] Site icon (favicon 512x512)

## 6. Images
- [ ] Upload everything in `IMAGES-NEEDED.md` with the exact filenames (in October, or update the path)

## 7. Pages
For each file in `pages/`: Add New Page > title > + block > **Custom HTML** > paste the whole file > set slug > Publish.

| File | Page title | Slug |
|---|---|---|
| 01-home | Home | home |
| 02-about | About | about |
| 03-services | Services | services |
| 04 to 12 | each service | as in filename (e.g. `house-rewiring`) |
| 13 to 19 | Electrician Poole etc. | as in filename (e.g. `electrician-poole`) |
| 20-projects | Projects | projects |
| 21-project-TEMPLATE | copy for each case study | child of Projects |
| 22-contact-us | Contact Us | contact-us |
| 23-privacy-policy | Privacy Policy | privacy-policy |
| 24-cookie-policy | Cookie Policy | cookie-policy |

- [ ] Settings > Reading > static front page = Home

## 8. Menu "Mainnav" (Main Menu location)
Home `/` - About `/about/` - Services `/services/` - Projects `/projects/` - Contact Us `/contact-us/` - `07742 924814` (custom link `tel:+447742924814`)
- Tip: leave Projects out of the menu until the first real case study is published

## 9. Footer widgets
- [ ] Footer Area 1 (title "Contact Form"): paste `wordpress/footer-area-1-contact-form.html`
- [ ] Footer Area 2 (no title): paste `wordpress/footer-area-2-get-in-touch.html`

## 10. Forms (Web3Forms)
- [ ] Free account at web3forms.com with James's enquiry email
- [ ] Replace `YOUR_WEB3FORMS_ACCESS_KEY` in Contact Us page + Footer Area 1
- [ ] Send a test from both forms (check spam first time)

## 11. SEO + analytics
- [ ] Rank Math wizard: Advanced, Local business, sitemap on, breadcrumbs off
- [ ] Each page: SEO title, description, focus keyword from `SEO.md`
- [ ] Site Kit: GA4 + Search Console, Consent Mode on
- [ ] Submit `sitemap_index.xml`, request indexing for every page
- [ ] Rank Math Redirections for old Wix URLs (see `SEO.md`)
- [ ] Update Google Business Profile website link

## 12. Check
- [ ] Test at desktop, tablet and phone: no white side gaps, sticky buttons, menu, phone/email links, forms
- [ ] Cookie banner: Accept/Reject both work
- [ ] LiteSpeed: purge all
- [ ] Backup with All-in-One WP Migration

## Editing later
Business details (phone, email, image folder) live in `src/config.py`. Change once, run `python3 src/build.py`, re-paste the changed pages.
