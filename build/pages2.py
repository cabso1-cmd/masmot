# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import SITE, icon, SERVICES
from templates import page, breadcrumb_schema
from pages import write, cta_band, faq_block, check_items

# ---------------------------------------------------------------------------
# TRACK SHIPMENT
# ---------------------------------------------------------------------------

def build_track():
    body = f"""
<section class="page-hero" style="padding-bottom:170px">
  <div class="container">
    <div class="breadcrumbs"><a href="/">Home</a> / Track Shipment</div>
    <h1>Track your shipment</h1>
    <p class="lead">Enter the reference number from your booking confirmation or bill of lading to check status. For anything not showing here yet, your coordinator can pull a live update directly from the carrier.</p>
  </div>
</section>

<section style="padding-top:0">
  <div class="container">
    <div class="tracker-box reveal">
      <form id="tracker-form">
        <label for="tracking-number">Tracking / booking reference</label>
        <div class="tracker-row">
          <input type="text" id="tracking-number" name="tracking-number" placeholder="e.g. MML-284719" required>
          <button type="submit" class="btn btn-primary">{icon('search',18)} Track Shipment</button>
        </div>
        <p class="form-note">Reference numbers are provided in your booking confirmation email. Formats vary by mode (ocean / air) and carrier.</p>
      </form>

      <div class="tracker-result" id="tracker-result">
        <p><strong>Reference:</strong> <span id="tracker-ref">MML-000000</span> &nbsp;·&nbsp; <span class="badge">{icon('truck',14)} In Transit</span></p>
        <div class="timeline">
          <div class="timeline-item done"><strong>Booking confirmed</strong><span>Carrier booking accepted, documentation issued.</span></div>
          <div class="timeline-item done"><strong>Departed origin</strong><span>Cargo has left the origin port / airport.</span></div>
          <div class="timeline-item current"><strong>In transit</strong><span>Currently moving toward destination — this is a sample status for demonstration.</span></div>
          <div class="timeline-item"><strong>Arrived destination</strong><span>Pending.</span></div>
          <div class="timeline-item"><strong>Delivered</strong><span>Pending.</span></div>
        </div>
        <p class="form-note">This tracker shows illustrative status while the live carrier-data connection is being configured. Contact your coordinator any time for a confirmed, real-time update.</p>
      </div>
    </div>
  </div>
</section>

<section class="band-off">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Need a Direct Answer</span>
      <h2>Prefer to just ask?</h2>
      <p class="lead">Your account coordinator can confirm status, ETA, and any exceptions directly.</p>
    </div>
    <div class="grid grid-3">
      <div class="card text-center reveal"><div class="icon-tile" style="margin:0 auto 18px">{icon('phone',28)}</div><h3>Call</h3><p><a href="tel:{SITE['phone_href'].replace('tel:','')}">{SITE['phone_display']}</a></p></div>
      <div class="card text-center reveal"><div class="icon-tile" style="margin:0 auto 18px">{icon('mail',28)}</div><h3>Email</h3><p><a href="mailto:{SITE['email']}">{SITE['email']}</a></p></div>
      <div class="card text-center reveal"><div class="icon-tile" style="margin:0 auto 18px">{icon('clock',28)}</div><h3>Hours</h3><p>{SITE['hours']}</p></div>
    </div>
  </div>
</section>
"""
    schema = [breadcrumb_schema([("Home", "/"), ("Track Shipment", "/track-shipment.html")])]
    write("track-shipment.html", page(
        title="Track a Shipment | Masmot Logistics",
        description="Track your Masmot Logistics shipment by booking reference, or contact your coordinator directly for a confirmed real-time status update.",
        path="/track-shipment.html",
        body=body,
        active="/track-shipment.html",
        extra_schema=schema,
    ))


# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------

def build_contact():
    body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumbs"><a href="/">Home</a> / Contact</div>
    <h1>Get in touch</h1>
    <p class="lead">Tell us what you're shipping and where. If it's urgent, call — otherwise the form below reaches the same inbox our coordinators work from.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="split reveal">
      <div>
        <form id="contact-form" action="mailto:{SITE['email']}" method="post" enctype="text/plain">
          <div class="form-grid">
            <div>
              <label for="name">Full name</label>
              <input type="text" id="name" name="name" required>
            </div>
            <div>
              <label for="company">Company</label>
              <input type="text" id="company" name="company">
            </div>
            <div>
              <label for="email">Email</label>
              <input type="email" id="email" name="email" required>
            </div>
            <div>
              <label for="phone">Phone</label>
              <input type="tel" id="phone" name="phone">
            </div>
            <div class="full">
              <label for="service">Service of interest</label>
              <select id="service" name="service">
                <option value="">General enquiry</option>
                {"".join(f'<option value="{s["title"]}">{s["title"]}</option>' for s in SERVICES)}
              </select>
            </div>
            <div class="full">
              <label for="message">Shipment details</label>
              <textarea id="message" name="message" placeholder="Origin, destination, commodity, dimensions/weight, target dates..." required></textarea>
            </div>
          </div>
          <button type="submit" class="btn btn-primary" style="margin-top:18px">Send Enquiry {icon('arrow-right',18)}</button>
          <p class="form-note" id="contact-form-note">We reply within one business day. For urgent shipments, please call us directly.</p>
        </form>
      </div>
      <div class="contact-info-card">
        <h3>Head Office</h3>
        <div class="contact-row"><div class="icon-tile">{icon('pin',22)}</div><div><strong>Address</strong><span>{SITE['address_line1']}<br>{SITE['address_line2']}</span></div></div>
        <div class="contact-row"><div class="icon-tile">{icon('phone',22)}</div><div><strong>Phone</strong><br><a href="tel:{SITE['phone_href'].replace('tel:','')}">{SITE['phone_display']}</a></div></div>
        <div class="contact-row"><div class="icon-tile">{icon('fax',22)}</div><div><strong>Fax</strong><span>{SITE['fax_display']}</span></div></div>
        <div class="contact-row"><div class="icon-tile">{icon('mail',22)}</div><div><strong>Email</strong><br><a href="mailto:{SITE['email']}">{SITE['email']}</a></div></div>
        <div class="contact-row"><div class="icon-tile">{icon('clock',22)}</div><div><strong>Hours</strong><span>{SITE['hours']}</span></div></div>
        <div class="social-row">
          <a href="{SITE['linkedin']}" aria-label="LinkedIn" target="_blank" rel="noopener">{icon('linkedin',18)}</a>
          <a href="{SITE['twitter']}" aria-label="X" target="_blank" rel="noopener">{icon('twitter',18)}</a>
          <a href="{SITE['facebook']}" aria-label="Facebook" target="_blank" rel="noopener">{icon('facebook',18)}</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="band-off">
  <div class="container">
    <div class="map-wrap reveal">
      <iframe title="Masmot Logistics head office location" loading="lazy" src="https://www.google.com/maps?q={SITE['address_full'].replace(' ', '+').replace(',', '%2C')}&output=embed"></iframe>
    </div>
  </div>
</section>
"""
    schema = [breadcrumb_schema([("Home", "/"), ("Contact", "/contact.html")])]
    write("contact.html", page(
        title="Contact Masmot Logistics | Get a Freight Quote",
        description="Contact Masmot Logistics Ltd for freight forwarding quotes and enquiries. Head office in Oakville, Ontario, Canada.",
        path="/contact.html",
        body=body,
        active="/contact.html",
        extra_schema=schema,
    ))


# ---------------------------------------------------------------------------
# 404
# ---------------------------------------------------------------------------

def build_404():
    body = f"""
<section style="padding:120px 0">
  <div class="container text-center">
    <span class="eyebrow">404</span>
    <h1>This shipment took a wrong turn</h1>
    <p class="lead" style="margin:0 auto 32px">The page you're looking for doesn't exist or has moved. Try the links below, or head back to the homepage.</p>
    <div class="hero-cta" style="justify-content:center">
      <a href="/" class="btn btn-primary">Back to Home {icon('arrow-right',18)}</a>
      <a href="/services/" class="btn btn-secondary">View Services</a>
      <a href="/contact.html" class="btn btn-secondary">Contact Us</a>
    </div>
  </div>
</section>
"""
    write("404.html", page(
        title="Page Not Found | Masmot Logistics",
        description="The page you're looking for doesn't exist or has moved.",
        path="/404.html",
        body=body,
        noindex=True,
    ))


# ---------------------------------------------------------------------------
# LEGAL PAGES (basic, so footer links aren't dead)
# ---------------------------------------------------------------------------

def build_legal():
    privacy_body = f"""
<section class="page-hero"><div class="container"><div class="breadcrumbs"><a href="/">Home</a> / Privacy Policy</div><h1>Privacy Policy</h1><p class="lead">Last updated: August 2026</p></div></section>
<section>
  <div class="container" style="max-width:820px">
    <p>Masmot Logistics Ltd ("Masmot", "we", "us") respects your privacy. This policy explains, in plain terms, what information we collect through this website and how it's used.</p>
    <h2>Information we collect</h2>
    <p>When you submit a quote request or contact form, we collect the details you provide — such as name, company, email, phone number, and shipment information — solely to respond to your enquiry and provide freight forwarding services.</p>
    <h2>How we use information</h2>
    <p>Information submitted through this site is used to prepare quotes, coordinate shipments, and respond to enquiries. We do not sell personal information to third parties.</p>
    <h2>Third parties</h2>
    <p>We may share shipment-relevant information with carriers, customs brokers, and port agents strictly as needed to execute a booking on your behalf.</p>
    <h2>Contact</h2>
    <p>Questions about this policy can be directed to <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p>
    <p class="form-note">This is a template privacy policy. Please have it reviewed by legal counsel before relying on it for compliance (e.g. PIPEDA) purposes.</p>
  </div>
</section>
"""
    write("privacy-policy.html", page(
        title="Privacy Policy | Masmot Logistics",
        description="Privacy policy for Masmot Logistics Ltd.",
        path="/privacy-policy.html",
        body=privacy_body,
        noindex=False,
    ))

    terms_body = f"""
<section class="page-hero"><div class="container"><div class="breadcrumbs"><a href="/">Home</a> / Terms of Service</div><h1>Terms of Service</h1><p class="lead">Last updated: August 2026</p></div></section>
<section>
  <div class="container" style="max-width:820px">
    <p>These terms govern use of the masmotlogistics.ca website. Use of this site does not itself create a contract of carriage or forwarding agency — those are governed by the specific booking confirmation, bill of lading, or service agreement issued for each shipment.</p>
    <h2>Website use</h2>
    <p>Content on this site is provided for general information about Masmot Logistics Ltd's services and does not constitute a binding quote until confirmed in writing by a coordinator.</p>
    <h2>Liability</h2>
    <p>Carriage and forwarding services are subject to the applicable carrier tariffs, international conventions, and Masmot Logistics Ltd's standard trading conditions, provided separately upon booking.</p>
    <h2>Contact</h2>
    <p>Questions about these terms can be directed to <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p>
    <p class="form-note">This is a template terms page. Please have it reviewed by legal counsel before relying on it.</p>
  </div>
</section>
"""
    write("terms-of-service.html", page(
        title="Terms of Service | Masmot Logistics",
        description="Terms of service for the Masmot Logistics Ltd website.",
        path="/terms-of-service.html",
        body=terms_body,
        noindex=False,
    ))


if __name__ == "__main__":
    build_track()
    build_contact()
    build_404()
    build_legal()
