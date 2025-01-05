import { database, ref, runTransaction } from './firebase-config.js';

// Function to update view count
function updateViewCount() {
    const db = firebase.database();
    const viewsRef = db.ref('pageViews');

    // Transaction to safely increment the counter
    viewsRef.transaction((currentViews) => {
        return (currentViews || 0) + 1;
    }).then((result) => {
        // Update the counter display
        const counterElement = document.getElementById('view-counter');
        if (counterElement && result.snapshot.exists()) {
            counterElement.textContent = result.snapshot.val().toLocaleString();
            counterElement.classList.remove('loading');
        }
    }).catch((error) => {
        console.error('Error updating view count:', error);
        const counterElement = document.getElementById('view-counter');
        if (counterElement) {
            counterElement.textContent = '---';
            counterElement.classList.remove('loading');
        }
    });
}

// Add counter element to footer when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    const footer = document.querySelector('.md-footer-meta__inner');
    if (footer) {
        // Create counter container with loading state
        const counterContainer = document.createElement('div');
        counterContainer.className = 'view-counter-container';
        counterContainer.innerHTML = `
            <span class="view-counter-label">👁️ Views: </span>
            <span id="view-counter" class="loading">0</span>
        `;
        
        // Insert counter before the last child (copyright)
        footer.insertBefore(counterContainer, footer.lastElementChild);
        
        // Update the counter after a short delay
        setTimeout(updateViewCount, 1000);
    }
}); 