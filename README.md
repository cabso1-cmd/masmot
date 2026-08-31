# Masmot Logistics Ltd — Website

This repository is the complete, ready-to-publish website for **Masmot Logistics Ltd**, built as a static site (plain HTML/CSS/JS — no build step required to run it). It's designed to be pushed straight to GitHub and served with **GitHub Pages**, on the domain **masmotlogistics.ca**, managed through **Cloudflare** DNS, alongside your existing **iCloud custom domain email**.

This README covers, in order: what's in the repo, how to publish it on GitHub Pages, how to point Cloudflare at it without breaking your email, and where the letterhead/signature files are.

---

## 1. What's in this repo

```
index.html, about.html, contact.html, 404.html                        → top-level pages
services/                                                              → services hub + 7 service pages
assets/css/styles.css                                                  → all site styling (one file)
assets/js/main.js                                                      → nav, FAQ accordion, tracker demo
assets/img/                                                             → logo files (SVG + PNG), social share image
favicon.ico, favicon-*.png, apple-touch-icon.png, android-chrome-*.png → favicons
site.webmanifest                                                       → PWA/icon manifest
sitemap.xml, robots.txt                                                → SEO
CNAME                                                                   → tells GitHub Pages the custom domain (masmotlogistics.ca)
build/                                                                  → OPTIONAL: the Python scripts used to generate the HTML pages from shared templates. You never need to run these — they're here so future content edits (e.g. adding an 8th service, changing the phone number sitewide) can be made once in build/common.py and regenerated, instead of hand-editing 15 HTML files. See "Editing content later" below.
deliverables/letterhead/                                                → the Word letterhead template
deliverables/email-signature/                                           → the Outlook email signature
```

Nothing in here needs Jekyll, npm, or a build step to go live — GitHub Pages will serve the HTML files exactly as they are.

---

## 2. Push this to GitHub

1. Create a new **empty** repository on GitHub (no README/gitignore/license — this folder already has everything). A private repo works fine; it doesn't need to be public for Pages to work on a paid GitHub plan, and public repos get Pages for free on any plan.
2. From inside this folder:
   ```bash
   git init
   git add .
   git commit -m "Initial Masmot Logistics website"
   git branch -M main
   git remote add origin https://github.com/cabso1-cmd/masmot.git
   git push -u origin main
   ```

## 3. Turn on GitHub Pages

1. In the repo on GitHub: **Settings → Pages**.
2. Under **Build and deployment → Source**, choose **Deploy from a branch**.
3. Branch: **main**, folder: **/ (root)**. Save.
4. Under **Custom domain**, enter `masmotlogistics.ca` and save. (This repo already includes a `CNAME` file with that domain, so GitHub may pick it up automatically — entering it in the UI is still worth doing to trigger GitHub's DNS check and certificate issuance.)
5. Leave this tab open — you'll come back after the DNS step below to confirm "DNS check successful" and to tick **Enforce HTTPS**.

## 4. Point Cloudflare at GitHub Pages

In the Cloudflare dashboard, open the **masmotlogistics.ca** zone → **DNS → Records**, and add:

| Type | Name | Content | Proxy status |
|---|---|---|---|
| A | @ | `185.199.108.153` | DNS only (grey cloud) — see note below |
| A | @ | `185.199.109.153` | DNS only |
| A | @ | `185.199.110.153` | DNS only |
| A | @ | `185.199.111.153` | DNS only |
| AAAA | @ | `2606:50c0:8000::153` | DNS only |
| AAAA | @ | `2606:50c0:8001::153` | DNS only |
| AAAA | @ | `2606:50c0:8002::153` | DNS only |
| AAAA | @ | `2606:50c0:8003::153` | DNS only |
| CNAME | www | `cabso1-cmd.github.io` | DNS only |

**Important — do this in two stages:**

1. **First**, add the records above with the Cloudflare proxy **off** ("DNS only" / grey cloud icon). Go back to the GitHub Pages settings tab and wait for **"DNS check successful"** and for the **Enforce HTTPS** checkbox to become available (this can take a few minutes up to a couple of hours). Tick **Enforce HTTPS** once it appears. GitHub needs to see your DNS directly (not through Cloudflare's proxy) to issue the SSL certificate the first time.
2. **After** HTTPS is confirmed working on `https://masmotlogistics.ca`, you can optionally switch the records to **Proxied** (orange cloud) to get Cloudflare's CDN/caching/DDoS protection. If you do, also set Cloudflare **SSL/TLS mode** to **Full (strict)** under SSL/TLS → Overview, so Cloudflare talks to GitHub over HTTPS too.

(`cabso1-cmd.github.io` is your GitHub Pages hostname regardless of what you name the repo — GitHub Pages custom-domain CNAMEs always point to `<username>.github.io`, never `<username>.github.io/<repo-name>`.)

## 5. Do NOT touch your existing iCloud email DNS records

Your iCloud custom domain email is almost certainly using records that look like this (already in place from your MaxSafe-style setup) — **leave these exactly as they are**:

| Type | Name | Content |
|---|---|---|
| MX | @ | `mx01.mail.icloud.com` (priority 10) |
| MX | @ | `mx02.mail.icloud.com` (priority 10) |
| TXT | @ | `v=spf1 include:icloud.com ~all` (or your existing SPF line with `include:icloud.com` added) |
| TXT | @ | the personal verification TXT string Apple gave you when you first set up the domain |
| CNAME | `sig1._domainkey` | `sig1.dkim.masmotlogistics.ca.at.icloudmailadmin.com` |

These use different record types (MX, TXT) or a different hostname (`sig1._domainkey`) than the website's A/AAAA/CNAME-on-`www` records, so **the website and email records coexist without conflict** — you're only adding new records, not replacing anything. The one thing to double check: Cloudflare only allows **one TXT record's worth of SPF** at the root (`@`) — if you ever add another service that wants its own SPF `v=spf1...` line, merge it into the single existing SPF TXT record rather than creating a second one, or mail delivery can break.

## 6. Verify

- `https://masmotlogistics.ca` loads the site (allow up to 24 hours for full DNS propagation, though Cloudflare is usually fast).
- `https://www.masmotlogistics.ca` redirects/loads correctly too.
- Padlock/HTTPS is active (no certificate warning).
- Send a test email to `operations@masmotlogistics.ca` to confirm mail still delivers after the DNS changes.
- Run `dig masmotlogistics.ca` (Mac/Linux) or `Resolve-DnsName masmotlogistics.ca` (Windows PowerShell) to double check the A records resolve to GitHub's IPs.

---

## 7. Letterhead & email signature

- **`deliverables/letterhead/Masmot-Logistics-Letterhead-Template.docx`** — open in Word, replace the bracketed placeholder text (`[Date]`, `[Recipient Name]`, etc.) with your letter content. The logo header and contact-details footer repeat automatically on every page.
- **`deliverables/email-signature/`** — the Outlook signature plus an `INSTRUCTIONS.md` walking through installing it in Outlook (Windows, Mac, and Outlook on the web). The signature's logo links back to the live website, so once the site is deployed (step 2–4 above) the logo just works with nothing further to do.

---

## 8. Editing content later

**Small text tweaks** (a sentence, a phone number in one spot): just edit the relevant `.html` file directly and commit.

**Sitewide changes** (phone number everywhere, adding an 8th service, changing the address): edit `build/common.py` (contact info, service list) or `build/service_content.py` (per-service copy), then regenerate:

```bash
cd build
python3 pages.py
python3 pages2.py
python3 sitemap_robots.py
```

This rewrites the HTML pages from the templates — safe to run any time, and much less error-prone than hand-editing the header/footer on 15 pages individually. Requires Python 3 (no extra packages).

---

## 9. SEO next steps (outside this repo)

The site ships with on-page SEO already handled: unique title/meta description per page, canonical URLs, Open Graph + Twitter card tags, `sitemap.xml`, `robots.txt`, and JSON-LD structured data (Organization/LocalBusiness, Service, FAQ, and Breadcrumb schema) on every relevant page. A few things worth doing once the site is live, from your end:

1. **Google Search Console** (search.google.com/search-console) — verify `masmotlogistics.ca`, submit `sitemap.xml`.
2. **Bing Webmaster Tools** — same idea, for Bing/Copilot search.
3. **Google Business Profile** — create/claim a listing for Masmot Logistics at the Oakville address; this matters more for local "freight forwarder near me" searches than on-page SEO does.
4. **Backlinks** — getting the old masmotlogistics.com either redirected to the new domain, or at least updated to link to it, will help carry over any existing authority.

---

## Brand assets quick reference

| | |
|---|---|
| Navy (primary) | `#0F2A47` |
| Navy (dark/footer) | `#0A2440` |
| Amber (accent) | `#F2A93B` / `#E0932A` (hover) |
| Slate (body text) | `#5B6B7C` |
| Headings font | Poppins (600/700) |
| Body font | Inter |

Logo source files (SVG, editable) are in `assets/img/`: `logo-horizontal.svg` (light backgrounds), `logo-horizontal-white.svg` (dark backgrounds), `logo-stacked.svg` (square use — letterhead, social profile photo), `icon-mark.svg` (icon/favicon only).
