/* PumaPulse — Theme Toggle */
(function() {
  var STORAGE_KEY = 'pp-theme';
  var root = document.documentElement;

  // Load saved theme or default to dark
  var saved = localStorage.getItem(STORAGE_KEY) || 'dark';
  root.setAttribute('data-theme', saved);

  // Inject toggle button into navbar after nav is ready
  function injectToggle() {
    var navCta = document.getElementById('navCta');
    if (!navCta) return;

    var btn = document.createElement('button');
    btn.className = 'theme-toggle';
    btn.setAttribute('aria-label', 'Toggle theme');
    btn.setAttribute('title', 'Toggle light/dark mode');
    btn.innerHTML = `
      <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="5"/>
        <line x1="12" y1="1" x2="12" y2="3"/>
        <line x1="12" y1="21" x2="12" y2="23"/>
        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/>
        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>
        <line x1="1" y1="12" x2="3" y2="12"/>
        <line x1="21" y1="12" x2="23" y2="12"/>
        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/>
        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>
      </svg>
      <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
      </svg>`;

    btn.addEventListener('click', function() {
      var current = root.getAttribute('data-theme');
      var next = current === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      localStorage.setItem(STORAGE_KEY, next);
    });

    // Insert before the CTA button
    navCta.insertBefore(btn, navCta.firstChild);
  }

  // Try immediately, then retry after nav.js injects the navbar
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      setTimeout(injectToggle, 10);
    });
  } else {
    setTimeout(injectToggle, 10);
  }
})();
