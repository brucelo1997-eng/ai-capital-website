// AI Capital - Interactive JavaScript

// Set active nav link based on current page
document.addEventListener('DOMContentLoaded', function() {
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-links a');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
});

// FAQ Accordion Functionality
const faqQuestions = document.querySelectorAll('.faq-question');

faqQuestions.forEach(question => {
  question.addEventListener('click', function() {
    const answer = this.nextElementSibling;
    
    // Close all other answers
    document.querySelectorAll('.faq-answer').forEach(a => {
      if (a !== answer) {
        a.classList.remove('active');
        a.previousElementSibling.classList.remove('active');
      }
    });
    
    // Toggle current answer
    answer.classList.toggle('active');
    this.classList.toggle('active');
  });
});

// Form Submission Handler
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', function(e) {
    e.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;
    
    // Basic validation
    if (!name || !email || !message) {
      alert('Please fill out all fields');
      return;
    }
    
    if (!email.includes('@')) {
      alert('Please enter a valid email');
      return;
    }
    
    // Show success message
    alert('Thank you for your message! We\'ll get back to you soon.');
    contactForm.reset();
  });
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});
