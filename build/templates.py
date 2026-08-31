# -*- coding: utf-8 -*-
import json
from common import SITE, ICONS, icon, NAV_ITEMS, SERVICES

def render_head(title, description, path, og_image="/assets/img/og-image.jpg", extra_schema=None, noindex=False):
    canonical = SITE["domain"] + path
    robots = "noindex, nofollow" if noindex else "index, follow"
    schema_blocks = [organization_schema()]
    if extra_schema:
        if isinstance(extra_schema, list):
            schema_blocks.extend(extra_schema)
        else:
            schema_blocks.append(extra_schema)
    schema_tags = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schema_blocks
    )
    return f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">

<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#0F2A47">

<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE['domain']}{og_image}">
<meta property="og:locale" content="en_CA">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{SITE['domain']}{og_image}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/styles.css">
{schema_tags}"""


def organization_schema():
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": SITE["domain"] + "/#organization",
        "name": SITE["name"],
        "url": SITE["domain"],
        "logo": SITE["domain"] + "/assets/img/logo-stacked@2x.png",
        "image": SITE["domain"] + "/assets/img/og-image.jpg",
        "description": "Masmot Logistics Ltd is a freight forwarder providing ocean and air freight forwarding, customs brokerage support, ship husbandry, temperature-controlled warehousing, project cargo, and cargo insurance services.",
        "email": SITE["email"],
        "telephone": SITE["phone_display"],
        "faxNumber": SITE["fax_display"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": SITE["address_line1"],
            "addressLocality": "Oakville",
            "addressRegion": "ON",
            "postalCode": "L6H 5V1",
            "addressCountry": "CA",
        },
    }


def local_business_schema():
    d = organization_schema()
    d["@type"] = "LocalBusiness"
    d["@id"] = SITE["domain"] + "/#localbusiness"
    d["priceRange"] = "$$"
    d["openingHoursSpecification"] = {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "opens": "08:30",
        "closes": "17:30",
    }
    return d


def breadcrumb_schema(items):
    """items: list of (name, url_path)"""
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": name,
                "item": SITE["domain"] + path,
            }
            for i, (name, path) in enumerate(items)
        ],
    }


def service_schema(service):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": service["title"],
        "provider": {"@type": "Organization", "name": SITE["name"], "url": SITE["domain"]},
        "areaServed": "CA",
        "description": service["summary"],
        "url": SITE["domain"] + "/services/" + service["slug"] + ".html",
    }


def faq_schema(pairs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in pairs
        ],
    }


def render_topbar():
    return f"""<div class="topbar">
  <div class="container">
    <div class="topbar-links">
      <a href="tel:{SITE['phone_href'].replace('tel:', '')}">{icon('phone',14)} {SITE['phone_display']}</a>
      <a href="mailto:{SITE['email']}">{icon('mail',14)} {SITE['email']}</a>
      <span>{icon('pin',14)} Oakville, ON, Canada</span>
    </div>
    <div class="topbar-links">
      <span>{icon('clock',14)} {SITE['hours']}</span>
      <a href="/contact.html">Get a Quote</a>
    </div>
  </div>
</div>"""


def render_header(active=""):
    def nav_link(label, href):
        cls = ' class="active"' if href == active else ""
        return f'<li><a href="{href}"{cls}>{label}</a></li>'

    services_dropdown = "\n".join(
        f'<a href="/services/{s["slug"]}.html">{icon(s["icon"],18)} {s["title"]}</a>' for s in SERVICES
    )

    return f"""{render_topbar()}
<header class="site-header">
  <div class="container navbar">
    <a href="/" class="brand">
      <img src="/assets/img/icon-mark.svg" alt="" width="42" height="42">
      <span class="brand-text"><strong>MASMOT</strong><span>LOGISTICS LTD</span></span>
    </a>
    <nav aria-label="Primary">
      <ul class="nav-links">
        {nav_link('Home', '/')}
        {nav_link('About', '/about.html')}
        <li class="has-dropdown">
          <a href="/services/"{' class="active"' if active == '/services/' else ''}>Services {icon('chevron-down',14)}</a>
          <div class="dropdown">
            {services_dropdown}
          </div>
        </li>
        {nav_link('Contact', '/contact.html')}
      </ul>
    </nav>
    <div class="nav-cta">
      <a href="/contact.html" class="btn btn-secondary">Get a Quote</a>
      <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">{icon('menu',22)}</button>
    </div>
  </div>
</header>"""


def render_footer():
    services_links = "\n".join(f'<li><a href="/services/{s["slug"]}.html">{s["title"]}</a></li>' for s in SERVICES)
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="/assets/img/logo-horizontal-white.svg" alt="{SITE['name']}" width="220" height="66">
        <p>Freight forwarding and ancillary logistics services, built around cargo that has to move on time, every time.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          {services_links}
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="/about.html">About Us</a></li>
          <li><a href="/services/">All Services</a></li>
          <li><a href="/contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Head Office</h4>
        <ul>
          <li>{SITE['address_line1']}<br>{SITE['address_line2']}</li>
          <li><a href="tel:{SITE['phone_href'].replace('tel:','')}">{SITE['phone_display']}</a></li>
          <li><a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
          <li>Fax: {SITE['fax_display']}</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span id="year">2026</span> {SITE['name']}. All rights reserved.</span>
      <div class="footer-legal">
        <a href="/privacy-policy.html">Privacy Policy</a>
        <a href="/terms-of-service.html">Terms of Service</a>
      </div>
    </div>
  </div>
</footer>
<script src="/assets/js/main.js"></script>"""


def page(title, description, path, body, active="", og_image="/assets/img/og-image.jpg", extra_schema=None, noindex=False):
    return f"""<!DOCTYPE html>
<html lang="en-CA">
<head>
{render_head(title, description, path, og_image, extra_schema, noindex)}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
{render_header(active)}
<main id="main">
{body}
</main>
{render_footer()}
</body>
</html>
"""
