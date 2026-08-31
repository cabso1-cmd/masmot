// Masmot Logistics Ltd — site scripts
document.addEventListener('DOMContentLoaded', function () {

  /* Mobile nav toggle */
  var toggle = document.querySelector('.nav-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      document.body.classList.toggle('nav-open');
      var expanded = document.body.classList.contains('nav-open');
      toggle.setAttribute('aria-expanded', expanded ? 'true' : 'false');
    });
  }

  /* Mobile dropdown expand */
  document.querySelectorAll('.has-dropdown > a').forEach(function (link) {
    link.addEventListener('click', function (e) {
      if (window.innerWidth <= 980) {
        e.preventDefault();
        link.parentElement.classList.toggle('open');
      }
    });
  });

  /* FAQ accordion */
  document.querySelectorAll('.accordion-trigger').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.accordion-item');
      var panel = item.querySelector('.accordion-panel');
      var isOpen = item.classList.contains('open');
      item.closest('.accordion').querySelectorAll('.accordion-item').forEach(function (i) {
        i.classList.remove('open');
        i.querySelector('.accordion-panel').style.maxHeight = null;
      });
      if (!isOpen) {
        item.classList.add('open');
        panel.style.maxHeight = panel.scrollHeight + 40 + 'px';
      }
    });
  });

  /* Scroll reveal */
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }

  /* Active nav link highlighting */
  var path = window.location.pathname.replace(/\/index\.html$/, '/');
  document.querySelectorAll('.nav-links a[href]').forEach(function (a) {
    var href = a.getAttribute('href');
    if (href === path || (href !== '/' && path.indexOf(href.replace(/^\.*\//, '/')) !== -1)) {
      // best-effort match handled per-page via data-active instead
    }
  });

  /* Shipment tracker demo (front-end only — wire up to a real carrier/API later) */
  var trackerForm = document.getElementById('tracker-form');
  if (trackerForm) {
    trackerForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var result = document.getElementById('tracker-result');
      var input = document.getElementById('tracking-number');
      var refEl = document.getElementById('tracker-ref');
      if (refEl) refEl.textContent = input.value || 'MML-000000';
      result.classList.add('show');
      result.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    });
  }

  /* Contact form (static hosting — routes to mailto by default; swap in Formspree/Cloudflare Worker as needed) */
  var contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      var note = document.getElementById('contact-form-note');
      if (note) {
        note.textContent = "Thanks — your email client will open to send this to operations@masmotlogistics.ca.";
      }
    });
  }

  /* Footer year */
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
});
