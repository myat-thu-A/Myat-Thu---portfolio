// Mobile menu toggle
const menuToggle = document.getElementById('menu-toggle');
const navList = document.querySelector('.nav-list');

if (menuToggle) {
  menuToggle.addEventListener('click', () => {
    const isVisible = window.getComputedStyle(navList).display !== 'none';
    navList.style.display = isVisible ? 'none' : 'flex';
  });
}

// --- menu toggle script ---
//const toggle = document.getElementById('menu-toggle');
//const navList = document.querySelector('.nav-list');

if (toggle) {
  toggle.addEventListener('click', () => {
    navList.classList.toggle('active');
  });
}

// Smooth scrolling for internal links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      if (navList && window.innerWidth <= 900) navList.style.display = 'none';
    }
  });
});

// Contact form AJAX submit
const contactForm = document.getElementById('contactForm');
const formStatus = document.getElementById('form-status');

if (contactForm) {
  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    formStatus.textContent = '⏳ Sending…';
    const formData = new FormData(contactForm);

    try {
      const res = await fetch(contactForm.action || '/contact', {
        method: 'POST',
        body: formData
      });
      const data = await res.json();
      if (data.success) {
        formStatus.textContent = '✅ Message sent! Thank you.';
        contactForm.reset();
      } else {
        formStatus.textContent = '❌ Failed to send. Please try again later.';
      }
    } catch (err) {
      console.error(err);
      formStatus.textContent = '❌ Network error. Try again.';
    }
  });
}

// Header shadow toggle on scroll
window.addEventListener('scroll', () => {
  const header = document.querySelector('.site-header');
  if (window.scrollY > 20) header.classList.add('scrolled');
  else header.classList.remove('scrolled');
});