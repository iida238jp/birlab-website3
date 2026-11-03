'use strict';
const sections = [...document.querySelectorAll('main > section[id]')];
document.querySelectorAll('.language-link').forEach(link => {
  link.addEventListener('click', () => {
    let current = 'home';
    sections.forEach(section => {
      if (section.getBoundingClientRect().top <= 160) current = section.id;
    });
    const target = new URL(link.href, document.baseURI);
    target.hash = current;
    link.href = target.href;
  });
});
