window.MathJax = {
    tex: {
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']],
        processEscapes: true,
        processEnvironments: true,
        packages: ['base', 'ams', 'noerrors', 'noundefined']
    },
    options: {
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
        ignoreHtmlClass: '.*',
        processHtmlClass: 'arithmatex'
    },
    loader: {
        load: ['[tex]/noerrors', '[tex]/noundefined']
    },
    startup: {
        ready: () => {
            MathJax.startup.defaultReady();
        },
        pageReady: () => {
            return new Promise((resolve) => {
                // Initial typeset attempt
                const typesetMath = () => {
                    try {
                        MathJax.typesetPromise().then(() => {
                            console.log('MathJax: Initial typeset completed');
                        }).catch((err) => {
                            console.log('MathJax: Typeset failed:', err);
                        });
                    } catch (err) {
                        console.log('MathJax: Typeset error:', err);
                    }
                };

                // Function to retry typesetting
                const retryTypeset = (maxAttempts = 5, interval = 1000) => {
                    let attempts = 0;
                    const tryTypeset = () => {
                        if (attempts >= maxAttempts) {
                            console.log('MathJax: Max retry attempts reached');
                            return;
                        }
                        attempts++;
                        console.log(`MathJax: Attempt ${attempts} of ${maxAttempts}`);
                        typesetMath();
                        setTimeout(tryTypeset, interval);
                    };
                    tryTypeset();
                };

                // Initial setup
                if (document.readyState === 'complete') {
                    retryTypeset();
                } else {
                    window.addEventListener('load', () => {
                        retryTypeset();
                    });
                }

                // Handle dynamic content changes
                const observer = new MutationObserver((mutations) => {
                    typesetMath();
                });

                observer.observe(document.body, {
                    childList: true,
                    subtree: true
                });

                resolve();
            });
        }
    }
};
