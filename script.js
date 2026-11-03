'use strict';
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
const languageLinks = document.querySelectorAll('.language-link');
const sections = [...document.querySelectorAll('main > section[id]')];
const validSections = new Set(sections.map(section => section.id));

function closeMenu(restoreFocus = false) {
  navigation.classList.remove('is-open');
  menuButton.setAttribute('aria-expanded', 'false');
  if (restoreFocus) menuButton.focus();
}
menuButton.addEventListener('click', () => {
  const open = navigation.classList.toggle('is-open');
  menuButton.setAttribute('aria-expanded', String(open));
});
navigation.querySelectorAll('a').forEach(link => link.addEventListener('click', () => closeMenu()));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && navigation.classList.contains('is-open')) closeMenu(true);
});
window.matchMedia('(min-width: 781px)').addEventListener('change', event => {
  if (event.matches) closeMenu();
});

function setCurrentSection(id) {
  if (!validSections.has(id)) return;
  languageLinks.forEach(link => {
    const destination = new URL(link.getAttribute('href'), document.baseURI);
    destination.hash = id;
    link.href = destination.href;
  });
  navigation.querySelectorAll('a').forEach(link => {
    const current = link.hash === '#' + id;
    link.classList.toggle('active', current);
    if (current) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  });
}
setCurrentSection(location.hash.slice(1) || 'home');
window.addEventListener('hashchange', () => setCurrentSection(location.hash.slice(1) || 'home'));
let ticking = false;
function updateSection() {
  let current = 'home';
  sections.forEach(section => { if (section.getBoundingClientRect().top <= 155) current = section.id; });
  setCurrentSection(current);
  ticking = false;
}
window.addEventListener('scroll', () => {
  if (!ticking) { requestAnimationFrame(updateSection); ticking = true; }
}, { passive: true });

document.querySelectorAll('.video-stage').forEach(stage => {
  const button = stage.querySelector('.video-play');
  button.addEventListener('click', () => {
    const iframe = document.createElement('iframe');
    iframe.src = 'https://www.youtube-nocookie.com/embed/' + stage.dataset.videoId + '?autoplay=1&rel=0';
    iframe.title = stage.dataset.videoTitle;
    iframe.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
    iframe.allowFullscreen = true;
    iframe.referrerPolicy = 'strict-origin-when-cross-origin';
    stage.replaceChildren(iframe);
    iframe.focus();
  });
});
document.querySelector('#year').textContent = new Date().getFullYear();
