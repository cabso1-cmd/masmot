# -*- coding: utf-8 -*-
"""Shared data + templates for generating the Masmot Logistics static site."""

SITE = {
    "name": "Masmot Logistics Ltd",
    "short": "Masmot Logistics",
    "domain": "https://masmotlogistics.ca",
    "phone_display": "+1 647 848 7287",
    "phone_href": "tel:+16478487287",
    "fax_display": "+1 647 946 8310",
    "email": "operations@masmotlogistics.ca",
    "address_line1": "2150 Winston Park Dr, Unit 203",
    "address_line2": "Oakville, ON L6H 5V1, Canada",
    "address_full": "2150 Winston Park Dr, Unit 203, Oakville, ON L6H 5V1, Canada",
    "hours": "Mon–Fri, 8:30 AM–5:30 PM ET",
    "linkedin": "https://www.linkedin.com/company/masmot-logistics",
    "twitter": "https://x.com/masmotlogistics",
    "facebook": "https://www.facebook.com/masmotlogistics",
}

# -- Icon library (24x24 stroke icons, currentColor) -------------------------
ICONS = {
"ship": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 18h20l-2 3H4l-2-3Z"/><path d="M5 18V9h14v9"/><path d="M9 9V4h6v5"/><path d="M12 4V2"/></svg>',
"plane": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M10.5 20.5 12 17l-3-1-1.5 1.5-1.5-.5.9-2.6L2 12l1-2 5 1 3-3-6-4 2-1 8 3 3.5-3.5c.7-.7 2-.7 2.7 0 .7.7.7 2 0 2.7L18 9l3 8-2 1-3.9-4.9-3 3 1 5-2.6.9Z"/></svg>',
"customs": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h9l4 4v14a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1Z"/><path d="M14 3v5h5"/><path d="m8.5 15 2 2 4-4"/></svg>',
"anchor": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="5" r="2"/><path d="M12 7v14"/><path d="M5 12H2a10 10 0 0 0 10 10 10 10 0 0 0 10-10h-3"/><path d="M7 12h10"/></svg>',
"snowflake": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M4.5 6.5l15 11M19.5 6.5l-15 11"/><path d="m8 3 4 2 4-2M8 21l4-2 4 2M3 8l2 4-2 4M21 8l-2 4 2 4"/></svg>',
"crane": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 21V8l10-5v6"/><path d="M4 8h13l4 3"/><path d="M18 11v10"/><path d="M14 21v-6h4v6"/><path d="M18 11l2 4"/></svg>',
"shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 4 6v6c0 5 3.5 8.5 8 9 4.5-.5 8-4 8-9V6l-8-3Z"/><path d="m9 12 2 2 4-4"/></svg>',
"route": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="19" r="2.2"/><circle cx="18" cy="5" r="2.2"/><path d="M6 16.8V13a4 4 0 0 1 4-4h4a4 4 0 0 0 4-4"/></svg>',
"truck": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 17V7a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v10"/><path d="M14 10h4l4 4v3h-2"/><circle cx="7" cy="18" r="2"/><circle cx="17.5" cy="18" r="2"/><path d="M2 17h3M9.5 18h5.5"/></svg>',
"warehouse": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21V10l9-6 9 6v11"/><path d="M3 21h18"/><path d="M8 21v-7h8v7"/></svg>',
"pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s7-6.6 7-12a7 7 0 1 0-14 0c0 5.4 7 12 7 12Z"/><circle cx="12" cy="10" r="2.4"/></svg>',
"phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5c0-.6.4-1 1-1h3l2 5-2 1.5a11 11 0 0 0 5.5 5.5L15 14l5 2v3c0 .6-.4 1-1 1A15 15 0 0 1 4 5Z"/></svg>',
"mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6 8.5 7 8.5-7"/></svg>',
"clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/></svg>',
"fax": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 8V3h9l3 3v2"/><rect x="3" y="8" width="18" height="9" rx="1.5"/><rect x="7" y="17" width="10" height="4"/><path d="M7 11h2"/></svg>',
"check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 5 5 9-10"/></svg>',
"arrow-right": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
"menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
"chevron-down": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>',
"plus": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>',
"linkedin": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9h4v12H3zM9 9h3.8v1.7h.05c.53-1 1.83-2 3.77-2 4.03 0 4.78 2.65 4.78 6.1V21h-4v-5.4c0-1.3-.02-3-1.83-3-1.83 0-2.11 1.42-2.11 2.9V21H9Z"/></svg>',
"twitter": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.9 2H22l-7.6 8.7L23.3 22h-6.9l-5.4-6.9L4.7 22H1.6l8.1-9.3L1 2h7.1l4.9 6.3Zm-1.2 18h1.9L7.4 3.9H5.4Z"/></svg>',
"facebook": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-8h2.7l.4-3.1h-3.1V8c0-.9.25-1.5 1.55-1.5H17V3.7c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.3H8v3.1h2.8v8Z"/></svg>',
"package": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m3.5 7.5 8.5-4 8.5 4-8.5 4-8.5-4Z"/><path d="M3.5 7.5v9l8.5 4 8.5-4v-9"/><path d="M12 11.5V21"/></svg>',
"globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-6-3.8-9S9.5 5.6 12 3Z"/></svg>',
"search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>',
"file-check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h9l4 4v14a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1Z"/><path d="M14 3v5h5"/><path d="m8.5 15.5 2 2 5-5"/></svg>',
"users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3.2"/><path d="M2.8 20a6.2 6.2 0 0 1 12.4 0"/><circle cx="17.5" cy="8.5" r="2.6"/><path d="M15 13.2A5.6 5.6 0 0 1 21.2 20"/></svg>',
"target": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/></svg>',
"leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20c8-.5 13-5 13-14C8 6.5 4.5 11.5 4 20Z"/><path d="M4 20c1-3 3-6 6-8"/></svg>',
}

def icon(name, size=24):
    svg = ICONS[name]
    return svg.replace("<svg ", f'<svg width="{size}" height="{size}" ', 1)


NAV_ITEMS = [
    ("Home", "/"),
    ("About", "/about.html"),
    ("Services", "/services/"),
    ("Track Shipment", "/track-shipment.html"),
    ("Contact", "/contact.html"),
]

SERVICES = [
    {
        "slug": "ocean-freight-forwarding",
        "title": "Ocean Freight Forwarding",
        "short": "FCL and LCL ocean freight",
        "icon": "ship",
        "summary": "Full container load and less-than-container load ocean freight, booked across reliable carrier partnerships on the major East–West and North–South trade lanes.",
    },
    {
        "slug": "air-freight-forwarding",
        "title": "Air Freight Forwarding",
        "short": "Time-critical air cargo",
        "icon": "plane",
        "summary": "Consolidated and direct air freight for time-sensitive, high-value, and perishable cargo, with express options when deadlines can't move.",
    },
    {
        "slug": "customs-brokerage",
        "title": "Customs Brokerage Support",
        "short": "Clearance & compliance",
        "icon": "customs",
        "summary": "Import/export documentation support, tariff classification, and coordination with licensed customs brokers to keep cargo compliant and moving.",
    },
    {
        "slug": "ship-husbandry",
        "title": "Ship Husbandry",
        "short": "Port & vessel agency services",
        "icon": "anchor",
        "summary": "Port call coordination, crew change logistics, provisioning, spares delivery, and vessel agency support while your ship is in port.",
    },
    {
        "slug": "temperature-controlled-warehousing",
        "title": "Temperature-Controlled Warehousing",
        "short": "Cold chain & climate storage",
        "icon": "snowflake",
        "summary": "Chilled and frozen warehousing with continuous monitoring, for cargo that can't tolerate a break in the cold chain.",
    },
    {
        "slug": "project-cargo",
        "title": "Project & Breakbulk Cargo",
        "short": "Out-of-gauge & heavy-lift",
        "icon": "crane",
        "summary": "Route surveys, heavy-lift and out-of-gauge equipment moves, and breakbulk shipments planned end to end by hand, not by algorithm.",
    },
    {
        "slug": "cargo-insurance",
        "title": "Cargo Insurance",
        "short": "Coverage for what's in transit",
        "icon": "shield",
        "summary": "Marine cargo insurance placement so a single shipment's worth of risk never sits uncovered between origin and destination.",
    },
]

def service_by_slug(slug):
    for s in SERVICES:
        if s["slug"] == slug:
            return s
    raise KeyError(slug)
