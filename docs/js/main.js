// Generate QR Code
document.addEventListener('DOMContentLoaded', function() {
    // QR Code untuk repository URL
    const repoUrl = window.location.href;
    
    new QRCode(document.getElementById("qrcode"), {
        text: repoUrl,
        width: 200,
        height: 200,
        colorDark: "#2c3e50",
        colorLight: "#ffffff",
        correctLevel: QRCode.CorrectLevel.H
    });
    
    // Smooth scroll
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
    
    // Copy URL to clipboard
    document.querySelector('.qr-url').addEventListener('click', function() {
        const url = this.textContent;
        navigator.clipboard.writeText(url).then(() => {
            alert('URL copied to clipboard!');
        });
    });
});
