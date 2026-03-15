// Generate QR Code & Interactive Features
document.addEventListener('DOMContentLoaded', function() {
    // Generate QR Code untuk repository URL
    const repoUrl = window.location.href;
    
    new QRCode(document.getElementById("qrcode"), {
        text: repoUrl,
        width: 200,
        height: 200,
        colorDark: "#2c3e50",
        colorLight: "#ffffff",
        correctLevel: QRCode.CorrectLevel.H
    });
    
    // Smooth scroll untuk anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Copy URL to clipboard saat klik QR URL
    const qrUrlElement = document.querySelector('.qr-url');
    if (qrUrlElement) {
        qrUrlElement.addEventListener('click', function() {
            const url = repoUrl;
            navigator.clipboard.writeText(url).then(() => {
                // Show copied notification
                const originalText = this.textContent;
                this.textContent = '✅ URL Copied!';
                this.style.color = '#27ae60';
                
                setTimeout(() => {
                    this.textContent = originalText;
                    this.style.color = '';
                }, 2000);
            }).catch(err => {
                console.error('Failed to copy:', err);
                alert('URL: ' + url);
            });
        });
    }
    
    // Add animation on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe all sections
    document.querySelectorAll('.feature-card, .download-card, .install-method').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});
