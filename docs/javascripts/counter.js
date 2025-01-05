async function updateViewCount() {
    try {
        // Make API call to increment and get the count
        const response = await fetch('https://api.countapi.xyz/hit/hmustf.github.io/python4control');
        const data = await response.json();
        
        // Update the counter element
        const counterElement = document.getElementById('view-counter');
        if (counterElement) {
            counterElement.textContent = data.value.toLocaleString();
        }
    } catch (error) {
        console.error('Error updating view count:', error);
    }
}

// Add counter element to footer when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    const footer = document.querySelector('.md-footer-meta__inner');
    if (footer) {
        // Create counter container
        const counterContainer = document.createElement('div');
        counterContainer.className = 'view-counter-container';
        counterContainer.innerHTML = `
            <span class="view-counter-label">Views: </span>
            <span id="view-counter">...</span>
        `;
        
        // Insert counter before the last child (copyright)
        footer.insertBefore(counterContainer, footer.lastElementChild);
        
        // Update the counter
        updateViewCount();
    }
}); 