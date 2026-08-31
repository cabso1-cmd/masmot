# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import SITE, icon, SERVICES, service_by_slug
from templates import page, organization_schema, local_business_schema, breadcrumb_schema, service_schema, faq_schema
from service_content import SERVICE_CONTENT

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def write(path, html):
    full = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path)


# ---------------------------------------------------------------------------
# Shared building blocks
# ---------------------------------------------------------------------------

def hero_art():
    return """<svg viewBox="0 0 520 460" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <circle cx="260" cy="230" r="210" fill="#163A5F" fill-opacity="0.35"/>
  <circle cx="260" cy="230" r="150" stroke="#3C567A" stroke-width="1.5" stroke-dasharray="4 6" fill="none"/>
  <!-- simplified world dots -->
  <g fill="#7C93AC" fill-opacity="0.6">
    <circle cx="120" cy="150" r="3"/><circle cx="140" cy="140" r="3"/><circle cx="160" cy="155" r="3"/>
    <circle cx="180" cy="130" r="3"/><circle cx="200" cy="150" r="3"/><circle cx="150" cy="175" r="3"/>
    <circle cx="330" cy="120" r="3"/><circle cx="350" cy="135" r="3"/><circle cx="370" cy="120" r="3"/>
    <circle cx="390" cy="140" r="3"/><circle cx="360" cy="160" r="3"/><circle cx="340" cy="150" r="3"/>
    <circle cx="300" cy="300" r="3"/><circle cx="320" cy="320" r="3"/><circle cx="290" cy="330" r="3"/>
    <circle cx="150" cy="300" r="3"/><circle cx="170" cy="320" r="3"/><circle cx="130" cy="330" r="3"/>
    <circle cx="380" cy="260" r="3"/><circle cx="400" cy="280" r="3"/>
  </g>
  <!-- routes -->
  <path d="M150 175 Q 240 220 340 150" stroke="#F2A93B" stroke-width="2" stroke-dasharray="1 8" stroke-linecap="round"/>
  <path d="M150 175 Q 220 280 300 300" stroke="#F2A93B" stroke-width="2" stroke-dasharray="1 8" stroke-linecap="round"/>
  <path d="M340 150 Q 370 220 380 260" stroke="#F2A93B" stroke-width="2" stroke-dasharray="1 8" stroke-linecap="round"/>
  <circle cx="150" cy="175" r="6" fill="#F2A93B"/>
  <circle cx="340" cy="150" r="6" fill="#F2A93B"/>
  <circle cx="300" cy="300" r="6" fill="#F2A93B"/>
  <circle cx="380" cy="260" r="6" fill="#F2A93B"/>
  <!-- ship -->
  <g transform="translate(210,330)">
    <rect x="-46" y="6" width="92" height="10" rx="3" fill="#F7F8FA"/>
    <path d="M-38 6 -30 -10 30 -10 38 6Z" fill="#F7F8FA"/>
    <rect x="-6" y="-32" width="16" height="24" rx="2" fill="#0F2A47"/>
    <rect x="-2" y="-42" width="4" height="12" fill="#0F2A47"/>
    <rect x="-24" y="-16" width="12" height="8" fill="#F2A93B"/>
    <rect x="-8" y="-16" width="12" height="8" fill="#F2A93B"/>
    <rect x="8" y="-16" width="12" height="8" fill="#F2A93B"/>
  </g>
  <!-- plane -->
  <g transform="translate(345,110) rotate(18)">
    <path d="M0 0 L34 4 L18 12 L14 24 L8 22 L8 12 L-10 6Z" fill="#EAF1F8"/>
  </g>
</svg>"""


def service_icon_svg(name):
    return icon(name, 28)


def check_items(items):
    lis = "\n".join(f'<li>{icon("check",18)} <span>{i}</span></li>' for i in items)
    return f'<ul class="check-list">{lis}</ul>'


def services_grid(exclude_slug=None, cols=3):
    cards = []
    for s in SERVICES:
        if s["slug"] == exclude_slug:
            continue
        cards.append(f"""<div class="card service-card reveal">
          <div class="icon-tile amber">{service_icon_svg(s['icon'])}</div>
          <h3>{s['title']}</h3>
          <p>{s['summary']}</p>
          <a class="card-link" href="/services/{s['slug']}.html">Learn more {icon('arrow-right',16)}</a>
        </div>""")
    return f'<div class="grid grid-{cols}">' + "\n".join(cards) + "</div>"


def cta_band(heading="Ready to move your next shipment?", sub="Tell us what you're shipping and where — we'll come back with routing and a quote.", primary=("Request a Quote", "/contact.html"), secondary=("View Services", "/services/")):
    secondary_html = f'<a href="{secondary[1]}" class="btn btn-outline-light">{secondary[0]}</a>' if secondary else ""
    return f"""<div class="cta-band reveal">
      <div>
        <h2>{heading}</h2>
        <p>{sub}</p>
      </div>
      <div class="hero-cta" style="margin-top:0">
        <a href="{primary[1]}" class="btn btn-primary">{primary[0]} {icon('arrow-right',18)}</a>
        {secondary_html}
      </div>
    </div>"""


def faq_block(pairs):
    items = []
    for i, (q, a) in enumerate(pairs):
        items.append(f"""<div class="accordion-item{' open' if i == 0 else ''}">
          <button class="accordion-trigger">{q} {icon('plus',20)}</button>
          <div class="accordion-panel"{' style="max-height:400px"' if i == 0 else ''}>
            <div class="accordion-panel-inner"><p class="mb-0">{a}</p></div>
          </div>
        </div>""")
    return f'<div class="accordion">' + "\n".join(items) + "</div>"


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------

def build_home():
    body = f"""
<section class="hero">
  <div class="container">
    <div>
      <span class="badge">{icon('globe',14)} Freight Forwarding &amp; Logistics</span>
      <h1>Freight forwarding built around the shipment that can't be late.</h1>
      <p class="lead">Masmot Logistics arranges ocean and air freight, customs brokerage support, ship husbandry, temperature-controlled warehousing, project cargo, and cargo insurance — coordinated by people who answer the phone.</p>
      <div class="hero-cta">
        <a href="/contact.html" class="btn btn-primary">Request a Quote {icon('arrow-right',18)}</a>
        <a href="/services/" class="btn btn-outline-light">Explore Services</a>
      </div>
      <div class="hero-stats">
        <div><strong>7</strong><span>Core service lines</span></div>
        <div><strong>24/7</strong><span>Shipment monitoring</span></div>
        <div><strong>ON</strong><span>Canadian head office</span></div>
      </div>
    </div>
    <div class="hero-art">{hero_art()}</div>
  </div>
</section>

<section class="band-off">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">What We Do</span>
      <h2>One point of contact, the whole move covered</h2>
      <p class="lead">From booking through delivery, each service is handled by the same team — so nothing gets lost in a handoff between vendors.</p>
    </div>
    {services_grid()}
  </div>
</section>

<section>
  <div class="container">
    <div class="split reveal">
      <div>
        <span class="eyebrow">Why Masmot</span>
        <h2>Freight forwarding that treats your deadline like our own</h2>
        <p class="lead">We're a freight forwarder, not a booking portal. Every shipment is planned by someone who understands the lane, the paperwork, and what happens when a sailing gets rolled or a flight gets bumped.</p>
        {check_items([
            "Direct access to your coordinator — not a rotating call centre",
            "Proactive exception handling on delays, rollovers, and customs holds",
            "Documentation checked before it becomes a clearance problem",
            "Ancillary services (husbandry, cold storage, insurance) under one roof",
        ])}
        <a href="/about.html" class="btn btn-secondary" style="margin-top:8px">More About Us</a>
      </div>
      <div class="split-media">
        <svg viewBox="0 0 400 320" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <rect x="20" y="40" width="360" height="240" rx="16" fill="#FFFFFF" stroke="#D8DEE6"/>
          <rect x="46" y="70" width="140" height="14" rx="4" fill="#0F2A47"/>
          <rect x="46" y="96" width="200" height="8" rx="4" fill="#D8DEE6"/>
          <rect x="46" y="112" width="170" height="8" rx="4" fill="#D8DEE6"/>
          <rect x="46" y="140" width="308" height="1" fill="#EDEFF3"/>
          <g>
            <rect x="46" y="160" width="90" height="70" rx="8" fill="#F3F6FA"/>
            <rect x="60" y="174" width="30" height="30" rx="4" fill="#F2A93B"/>
            <rect x="150" y="160" width="90" height="70" rx="8" fill="#F3F6FA"/>
            <rect x="164" y="174" width="30" height="30" rx="4" fill="#163A5F"/>
            <rect x="254" y="160" width="90" height="70" rx="8" fill="#F3F6FA"/>
            <rect x="268" y="174" width="30" height="30" rx="4" fill="#F2A93B"/>
          </g>
          <circle cx="330" cy="60" r="18" fill="#1E8A5F" fill-opacity="0.15"/>
          <path d="M322 60 328 66 340 52" stroke="#1E8A5F" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
    </div>
  </div>
</section>

<section class="band-navy">
  <div class="container">
    <div class="stats-strip reveal">
      <div><strong>7</strong><span>Freight &amp; ancillary services</span></div>
      <div><strong>2</strong><span>Modes: ocean &amp; air</span></div>
      <div><strong>1</strong><span>Coordinator per account</span></div>
      <div><strong>ON, CA</strong><span>Head office, Oakville</span></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">How It Works</span>
      <h2>From quote to delivery in four steps</h2>
    </div>
    <div class="steps reveal">
      <div class="step"><h3>Tell us the shipment</h3><p>Commodity, dimensions, origin, destination, and timeline — the more detail, the sharper the quote.</p></div>
      <div class="step"><h3>Get routing &amp; pricing</h3><p>We return carrier options and an all-in quote, with the trade-offs between cost and transit time laid out.</p></div>
      <div class="step"><h3>We book &amp; document</h3><p>Booking confirmed, documentation prepared and checked, customs coordination lined up ahead of departure.</p></div>
      <div class="step"><h3>Track to delivery</h3><p>Status updates through transit, exceptions flagged as they happen, proof of delivery on file at the end.</p></div>
    </div>
  </div>
</section>

<section class="band-off">
  <div class="container">
    <div class="quote-card reveal" style="max-width:760px;margin:0 auto">
      <p>"Working with a forwarder who actually calls back when a sailing gets rolled is worth more than a marginally better rate. That's the difference with Masmot."</p>
      <div class="who">Operations Lead<span>Import/export shipper, Ontario</span></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    {cta_band()}
  </div>
</section>
"""
    schema = [
        local_business_schema(),
        breadcrumb_schema([("Home", "/")]),
    ]
    write("index.html", page(
        title="Masmot Logistics Ltd | Freight Forwarding & Logistics Services",
        description="Masmot Logistics Ltd is a Canadian freight forwarder offering ocean and air freight forwarding, customs brokerage support, ship husbandry, temperature-controlled warehousing, project cargo, and cargo insurance.",
        path="/",
        body=body,
        active="/",
        extra_schema=schema,
    ))


# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------

def build_about():
    body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumbs"><a href="/">Home</a> / About</div>
    <h1>Freight forwarding, run by people who pick up the phone</h1>
    <p class="lead">Masmot Logistics Ltd was built on a simple premise: a freight forwarder's job is to make cargo somebody else's easiest problem. That means clear communication, accurate documentation, and coordinators who know the shipment, not just the shipment number.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="split reverse reveal">
      <div>
        <span class="eyebrow">Our Story</span>
        <h2>Built around the shipments other forwarders find inconvenient</h2>
        <p>Masmot Logistics handles the freight forwarding work every shipper needs — ocean and air bookings, documentation, customs coordination — alongside the ancillary services that are harder to find a reliable partner for: ship husbandry while a vessel is in port, temperature-controlled warehousing for cargo that can't tolerate a gap in the cold chain, and project cargo moves that need a route survey before anyone books a truck.</p>
        <p>We'd rather be the forwarder you call when a shipment is complicated than the cheapest quote for the shipment that isn't.</p>
      </div>
      <div class="split-media">
        <svg viewBox="0 0 400 320" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <rect x="30" y="30" width="150" height="120" rx="10" fill="#0F2A47"/>
          <rect x="200" y="30" width="150" height="70" rx="10" fill="#F2A93B"/>
          <rect x="200" y="112" width="150" height="90" rx="10" fill="#163A5F"/>
          <rect x="30" y="168" width="150" height="122" rx="10" fill="#F3F6FA" stroke="#D8DEE6"/>
          <g fill="#FFFFFF">
            <circle cx="60" cy="70" r="6"/><rect x="76" y="65" width="80" height="10" rx="4"/>
            <circle cx="60" cy="100" r="6"/><rect x="76" y="95" width="60" height="10" rx="4"/>
          </g>
        </svg>
      </div>
    </div>
  </div>
</section>

<section class="band-off">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">What We Value</span>
      <h2>The standard we hold every shipment to</h2>
    </div>
    <div class="grid grid-3">
      <div class="card reveal"><div class="icon-tile">{icon('target',28)}</div><h3>Accountability</h3><p>One coordinator owns your account end to end — no handoffs between quoting, booking, and tracking teams.</p></div>
      <div class="card reveal"><div class="icon-tile">{icon('file-check',28)}</div><h3>Precision on paperwork</h3><p>Documentation is checked before it becomes a customs hold, not corrected after cargo is already stuck.</p></div>
      <div class="card reveal"><div class="icon-tile">{icon('users',28)}</div><h3>Plain communication</h3><p>Status updates in plain language, including the ones that say "this is delayed" — before you have to ask.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Where We Operate</span>
      <h2>Head office in Oakville, reach across the major trade lanes</h2>
      <p class="lead">Masmot Logistics is headquartered in Oakville, Ontario, coordinating shipments across ocean and air freight lanes through an established network of carrier and agency partners.</p>
    </div>
    <div class="map-wrap reveal">
      <iframe title="Masmot Logistics head office location" loading="lazy" src="https://www.google.com/maps?q={SITE['address_full'].replace(' ', '+').replace(',', '%2C')}&output=embed"></iframe>
    </div>
  </div>
</section>

<section class="band-off">
  <div class="container">
    {cta_band(heading="Have a shipment in mind?", sub="Send us the details and we'll come back with routing and pricing.", primary=("Contact Us", "/contact.html"), secondary=("View Services", "/services/"))}
  </div>
</section>
"""
    schema = [breadcrumb_schema([("Home", "/"), ("About", "/about.html")])]
    write("about.html", page(
        title="About Masmot Logistics Ltd | Freight Forwarder in Oakville, ON",
        description="Masmot Logistics Ltd is a Canadian freight forwarder headquartered in Oakville, Ontario, providing ocean and air freight forwarding plus ancillary logistics services.",
        path="/about.html",
        body=body,
        active="/about.html",
        extra_schema=schema,
    ))


# ---------------------------------------------------------------------------
# SERVICES HUB
# ---------------------------------------------------------------------------

def build_services_hub():
    body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumbs"><a href="/">Home</a> / Services</div>
    <h1>Freight forwarding and ancillary logistics services</h1>
    <p class="lead">Seven service lines, one coordinator per account. Explore each service below, or get in touch and describe what you're moving — we'll tell you exactly what applies.</p>
  </div>
</section>

<section>
  <div class="container">
    {services_grid(cols=3)}
  </div>
</section>

<section class="band-navy">
  <div class="container">
    {cta_band(heading="Not sure which service you need?", sub="Describe the shipment and we'll map it to the right service — or combination of services.", primary=("Talk to Us", "/contact.html"), secondary=("Call Us", SITE['phone_href']))}
  </div>
</section>
"""
    schema = [breadcrumb_schema([("Home", "/"), ("Services", "/services/")])]
    write("services/index.html", page(
        title="Freight Forwarding Services | Masmot Logistics",
        description="Ocean freight, air freight, customs brokerage support, ship husbandry, temperature-controlled warehousing, project cargo, and cargo insurance — all from Masmot Logistics Ltd.",
        path="/services/",
        body=body,
        active="/services/",
        extra_schema=schema,
    ))


# ---------------------------------------------------------------------------
# SERVICE DETAIL PAGES
# ---------------------------------------------------------------------------

def build_service_pages():
    for s in SERVICES:
        c = SERVICE_CONTENT[s["slug"]]
        features_html = "\n".join(
            f"""<div class="card reveal"><div class="icon-tile amber">{icon('check',24)}</div><h3>{title}</h3><p>{desc}</p></div>"""
            for title, desc in c["features"]
        )
        process_html = "\n".join(
            f'<div class="step"><h3>{title}</h3><p>{desc}</p></div>' for title, desc in c["process"]
        )
        other_services = [x for x in SERVICES if x["slug"] != s["slug"]][:3]
        related_html = "\n".join(
            f"""<div class="card reveal"><div class="icon-tile">{service_icon_svg(o['icon'])}</div><h3>{o['title']}</h3><p>{o['summary']}</p><a class="card-link" href="/services/{o['slug']}.html">Learn more {icon('arrow-right',16)}</a></div>"""
            for o in other_services
        )

        body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumbs"><a href="/">Home</a> / <a href="/services/">Services</a> / {s['title']}</div>
    <h1>{s['title']}</h1>
    <p class="lead">{c['intro']}</p>
    <div class="hero-cta">
      <a href="/contact.html" class="btn btn-primary">Request a Quote {icon('arrow-right',18)}</a>
      <a href="/services/" class="btn btn-outline-light">All Services</a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">What's Included</span>
      <h2>{s['title']} capabilities</h2>
    </div>
    <div class="grid grid-3">
      {features_html}
    </div>
  </div>
</section>

<section class="band-off">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Process</span>
      <h2>How it works</h2>
    </div>
    <div class="steps reveal">
      {process_html}
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">FAQ</span>
      <h2>Common questions about {s['title'].lower()}</h2>
    </div>
    <div style="max-width:760px;margin:0 auto">
      {faq_block(c['faqs'])}
    </div>
  </div>
</section>

<section class="band-off">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Related Services</span>
      <h2>Often paired with {s['title']}</h2>
    </div>
    <div class="grid grid-3">
      {related_html}
    </div>
  </div>
</section>

<section>
  <div class="container">
    {cta_band(heading=f"Ready to move forward with {s['title'].lower()}?", sub="Send over your shipment details and we'll come back with next steps.")}
  </div>
</section>
"""
        schema = [
            service_schema(s),
            faq_schema(c["faqs"]),
            breadcrumb_schema([("Home", "/"), ("Services", "/services/"), (s["title"], f"/services/{s['slug']}.html")]),
        ]
        write(f"services/{s['slug']}.html", page(
            title=c["meta_title"],
            description=c["meta_description"],
            path=f"/services/{s['slug']}.html",
            body=body,
            active="/services/",
            extra_schema=schema,
        ))


if __name__ == "__main__":
    build_home()
    build_about()
    build_services_hub()
    build_service_pages()
