window.MathJax = {
    tex: {
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']],
        processEscapes: true,
        processEnvironments: true
    },
    options: {
        ignoreHtmlClass: '.*',
        processHtmlClass: 'arithmatex'
    },
    startup: {
        pageReady: () => {
            return MathJax.startup.defaultPageReady().then(() => {
                // Function to reload MathJax
                window.reloadMathJax = function() {
                    MathJax.typesetPromise();
                };

                // Reload when URL changes (for SPAs)
                window.addEventListener('popstate', reloadMathJax);

                // Optional: Reload periodically during first load
                let attempts = 0;
                const interval = setInterval(function() {
                    reloadMathJax();
                    attempts++;
                    if (attempts >= 6) { // Stop after 30 seconds
                        clearInterval(interval);
                    }
                }, 5000);
            });
        }
    }
};
