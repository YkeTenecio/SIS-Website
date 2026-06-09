/* nav.js — mobile hamburger toggle */
(function () {
  const toggle = document.querySelector('.nav-toggle');
  const menu   = document.querySelector('.menu-bar > ul');

  if (!toggle || !menu) return;

  toggle.addEventListener('click', function () {
    const isOpen = menu.classList.toggle('nav-open');
    toggle.setAttribute('aria-expanded', isOpen);
  });

  menu.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      menu.classList.remove('nav-open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });
})();
