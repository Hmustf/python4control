document.addEventListener('DOMContentLoaded', function() {
    // Create modal container once
    const modal = document.createElement('div');
    modal.style.display = 'none';
    modal.style.position = 'fixed';
    modal.style.zIndex = '1000';
    modal.style.left = '0';
    modal.style.top = '0';
    modal.style.width = '100%';
    modal.style.height = '100%';
    modal.style.backgroundColor = 'rgba(0,0,0,0.9)';
    modal.style.cursor = 'zoom-out';

    // Create close button
    const closeButton = document.createElement('span');
    closeButton.innerHTML = '×';
    closeButton.style.position = 'absolute';
    closeButton.style.right = '25px';
    closeButton.style.top = '15px';
    closeButton.style.color = '#f1f1f1';
    closeButton.style.fontSize = '40px';
    closeButton.style.fontWeight = 'bold';
    closeButton.style.cursor = 'pointer';
    closeButton.style.zIndex = '1001';
    closeButton.style.transition = 'color 0.2s ease';

    // Add hover effect for close button
    closeButton.onmouseover = function() {
        this.style.color = '#fff';
    }
    closeButton.onmouseout = function() {
        this.style.color = '#f1f1f1';
    }

    // Create modal image
    const modalImg = document.createElement('img');
    modalImg.style.margin = 'auto';
    modalImg.style.display = 'block';
    modalImg.style.maxWidth = '90%';
    modalImg.style.maxHeight = '90vh';
    modalImg.style.position = 'absolute';
    modalImg.style.top = '50%';
    modalImg.style.left = '50%';
    modalImg.style.transform = 'translate(-50%, -50%)';

    // Add elements to modal
    modal.appendChild(closeButton);
    modal.appendChild(modalImg);
    document.body.appendChild(modal);

    // Get all images that should be zoomable
    const images = document.querySelectorAll('.responsive-image, img[alt="Second-Order Response"], img[alt="Second-Order System Performance Matrix"]');
    
    images.forEach(img => {
        img.style.cursor = 'zoom-in';
        
        img.onclick = function(e) {
            e.preventDefault();
            modal.style.display = 'block';
            modalImg.src = this.src;
            document.body.style.overflow = 'hidden';
        }
    });

    // Close modal when clicking close button
    closeButton.onclick = function() {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }

    // Close modal when clicking outside the image
    modal.onclick = function(e) {
        if (e.target === modal) {
            this.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    }

    // Handle escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.style.display === 'block') {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });
}); 