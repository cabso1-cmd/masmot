# -*- coding: utf-8 -*-
import os, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from common import SITE, SERVICES

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TODAY = datetime.date.today().isoformat()

URLS = [
    ("/", 1.0, "weekly"),
    ("/about.html", 0.8, "monthly"),
    ("/services/", 0.9, "weekly"),
    ("/track-shipment.html", 0.7, "monthly"),
    ("/contact.html", 0.8, "monthly"),
] + [
    (f"/services/{s['slug']}.html", 0.85, "monthly") for s in SERVICES
] + [
    ("/privacy-policy.html", 0.2, "yearly"),
    ("/terms-of-service.html", 0.2, "yearly"),
]

def build_sitemap():
    entries = "\n".join(
        f"""  <url>
    <loc>{SITE['domain']}{path}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
  </url>""" for path, prio, freq in URLS
    )
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>
"""
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    print("wrote sitemap.xml with", len(URLS), "urls")


def build_robots():
    txt = f"""User-agent: *
Allow: /

Sitemap: {SITE['domain']}/sitemap.xml
"""
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(txt)
    print("wrote robots.txt")


if __name__ == "__main__":
    build_sitemap()
    build_robots()
