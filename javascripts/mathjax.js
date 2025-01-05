window.MathJax = {
    tex: {
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['\\[', '\\]'], ['$$', '$$']],
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
            document.querySelectorAll('.arithmatex').forEach(element => {
                element.style.display = 'block';
                element.style.margin = '1em 0';
            });
        }
    }
};
