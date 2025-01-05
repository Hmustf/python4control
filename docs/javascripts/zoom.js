document.addEventListener('DOMContentLoaded', function() {
    // Get all images with responsive-image class
    const images = document.querySelectorAll('.responsive-image, img[alt="Second-Order Response"], img[alt="Second-Order System Performance Matrix"]');
    
    images.forEach(img => {
        // Create a modal container
        const modal = document.createElement('div');
        modal.className = 'zoom-modal';
        modal.style.display = 'none';
        modal.style.position = 'fixed';
        modal.style.zIndex = '1000';
        modal.style.top = '0';
        modal.style.left = '0';
        modal.style.width = '100%';
        modal.style.height = '100%';
        modal.style.backgroundColor = 'rgba(0,0,0,0.9)';
        modal.style.cursor = 'zoom-out';

        // Create zoomed image
        const zoomedImg = document.createElement('img');
        zoomedImg.style.maxHeight = '90%';
        zoomedImg.style.maxWidth = '90%';
        zoomedImg.style.margin = 'auto';
        zoomedImg.style.position = 'absolute';
        zoomedImg.style.top = '50%';
        zoomedImg.style.left = '50%';
        zoomedImg.style.transform = 'translate(-50%, -50%)';
        zoomedImg.style.border = '2px solid white';
        zoomedImg.style.borderRadius = '4px';

        // Add modal to body
        modal.appendChild(zoomedImg);
        document.body.appendChild(modal);

        // Add click handlers
        img.addEventListener('click', function() {
            zoomedImg.src = this.src;
            modal.style.display = 'block';
            document.body.style.overflow = 'hidden';
        });

        modal.addEventListener('click', function() {
            this.style.display = 'none';
            document.body.style.overflow = 'auto';
        });
    });
}); 