// FAQ Accordion
const faqQuestions = document.querySelectorAll('.faq-question');
    
faqQuestions.forEach(question => {
    question.addEventListener('click', () => {
        const faqItem = question.parentElement;
        faqItem.classList.toggle('active');
        
        // Close other open FAQs
        faqQuestions.forEach(q => {
            if (q !== question && q.parentElement.classList.contains('active')) {
                q.parentElement.classList.remove('active');
            }
        });
    });
});


// Form Validation
const contactForm = document.getElementById('contactForm');

if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        let isValid = true;
        const formData = {};
        
        // Validate each field
        const formGroups = contactForm.querySelectorAll('.form-group');
        formGroups.forEach(group => {
            group.classList.remove('error');
            const input = group.querySelector('input, select, textarea');
            const errorMessage = group.querySelector('.error-message');
            
            if (input) {
                if (input.required && !input.value.trim()) {
                    group.classList.add('error');
                    isValid = false;
                } else if (input.type === 'email' && !validateEmail(input.value)) {
                    group.classList.add('error');
                    if (errorMessage) errorMessage.textContent = 'Please enter a valid email address';
                    isValid = false;
                } else if (input.id === 'name' && !validateName(input.value)) {
                    group.classList.add('error');
                    if (errorMessage) errorMessage.textContent = 'Please enter a valid full name (letters and spaces only)';
                    isValid = false;
                }
                
                // Store form data
                formData[input.name] = input.value;
            }
        });
        
        if (isValid) {
            // Here you would typically send the form data to a server
            console.log('Form submitted:', formData);
            
            // Show success message
            const successMessage = document.createElement('div');
            successMessage.className = 'success-message';
            successMessage.innerHTML = '<i class="fas fa-check-circle"></i> Thank you! Your message has been sent successfully.';
            contactForm.prepend(successMessage);
            successMessage.style.display = 'block';
            
            // Reset form
            contactForm.reset();
            
            // Hide success message after 5 seconds
            setTimeout(() => {
                successMessage.style.display = 'none';
            }, 5000);
        }
    });
}

// Email validation helper
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}

// Name validation helper
function validateName(name) {
    // Allows letters, spaces, hyphens, and apostrophes in names
    const re = /^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð '-]+$/u;
    return re.test(String(name).trim());
}

// Optional: Add real-time validation for the name field
document.addEventListener('DOMContentLoaded', function() {
    const nameInput = document.getElementById('name');
    if (nameInput) {
        nameInput.addEventListener('input', function() {
            const formGroup = this.closest('.form-group');
            if (!validateName(this.value)) {
                formGroup.classList.add('error');
            } else {
                formGroup.classList.remove('error');
            }
        });
    }
});
