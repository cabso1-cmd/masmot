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

  /* Contact form — submits to Formspree (https://formspree.io/f/mnpqjjwr) via fetch so the
     visitor stays on the page. If JS fails to run for any reason, the form still works: it
     falls back to a normal POST straight to Formspree, which shows its own confirmation page. */
  var contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = document.getElementById('contact-form-note');
      var successPanel = document.getElementById('contact-form-success');
      var submitBtn = contactForm.querySelector('button[type="submit"]');
      var btnLabel = submitBtn ? submitBtn.querySelector('.btn-label') : null;

      if (submitBtn) submitBtn.disabled = true;
      if (btnLabel) btnLabel.textContent = 'Sending…';
      if (note) { note.textContent = ''; }

      var fallbackMessage = 'Something went wrong sending that — please email us directly at operations@masmotlogistics.ca.';

      fetch(contactForm.action, {
        method: 'POST',
        body: new FormData(contactForm),
        headers: { 'Accept': 'application/json' },
      }).then(function (response) {
        if (response.ok) {
          contactForm.hidden = true;
          if (successPanel) {
            successPanel.hidden = false;
            successPanel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
          }
          return;
        }
        // Non-OK response from Formspree (e.g. validation error) — try to surface its message,
        // but never let a JSON-parsing failure escape as an unhandled/technical error.
        return response.json().catch(function () { return null; }).then(function (data) {
          if (note) {
            note.textContent = (data && data.errors && data.errors.length)
              ? data.errors.map(function (err) { return err.message; }).join(', ')
              : fallbackMessage;
          }
        });
      }).catch(function () {
        // Network-level failure (offline, blocked, DNS, etc.) — always show the friendly
        // message rather than the browser's raw "Failed to fetch" text.
        if (note) { note.textContent = fallbackMessage; }
      }).finally(function () {
        if (submitBtn) submitBtn.disabled = false;
        if (btnLabel) btnLabel.textContent = 'Send Enquiry';
      });
    });
  }

  /* Footer year */
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
});
