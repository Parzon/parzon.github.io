const content_dir = 'contents/';
const config_file = 'config.yml';
const section_names = ['home', 'research-interests', 'awards', 'projects', 'experience'];  // Added 'experience' to the array

window.addEventListener('DOMContentLoaded', event => {

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    }

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(document.querySelectorAll('#navbarResponsive .nav-link'));
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

    // Load and apply YAML config to HTML
    fetch(content_dir + config_file)
        .then(response => response.text())
        .then(text => {
            const yml = jsyaml.load(text);
            Object.keys(yml).forEach(key => {
                try {
                    document.getElementById(key).innerHTML = yml[key];
                } catch (error) {
                    console.error("Error setting content for ID:", key, "with error:", error);
                }
            });
        })
        .catch(error => console.error("Error loading YAML config:", error));

    // Load Markdown files, parse them, and inject into the webpage
    marked.use({ mangle: false, headerIds: false });
    section_names.forEach((section) => {
        fetch(`${content_dir}${section}.md`)
            .then(response => response.text())
            .then(markdown => {
                const html = marked.parse(markdown);
                document.getElementById(`${section}-md`).innerHTML = html;
            })
            .then(() => {
                // Update MathJax typesetting
                MathJax.typeset();
            })
            .catch(error => console.error("Error loading or parsing markdown for section:", section, "with error:", error));
    });

});
