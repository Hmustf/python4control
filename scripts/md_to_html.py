#!/usr/bin/env python3
import os
import re
import json
from pathlib import Path
import markdown
from markdown.extensions import fenced_code
from markdown.extensions import codehilite
from markdown.extensions.toc import TocExtension
from markdown.extensions.tables import TableExtension

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title} - Python4Control</title>
    <link rel="stylesheet" href="https://pages-themes.github.io/cayman/assets/css/style.css">
    <link rel="stylesheet" href="{css_path}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/line-numbers/prism-line-numbers.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/line-numbers/prism-line-numbers.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/toolbar/prism-toolbar.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/copy-to-clipboard/prism-copy-to-clipboard.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/toolbar/prism-toolbar.min.css">
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script>
        window.MathJax = {{
            tex: {{
                inlineMath: [['$', '$'], ['\\(', '\\)']],
                displayMath: [['$$', '$$'], ['\\[', '\\]']],
                processEscapes: true
            }},
            svg: {{
                fontCache: 'global'
            }}
        }};
    </script>
</head>
<body>
    <div class="page-header">
        <h1 class="project-name">{title}</h1>
        <div class="project-tagline">
            Python is a versatile programming language widely used in scientific computing and engineering. With libraries like 
            <a href="https://numpy.org/">NumPy</a>, 
            <a href="https://python-control.org/">Control</a>, and 
            <a href="https://matplotlib.org/">Matplotlib</a>, 
            it provides powerful tools for control system analysis and design.
        </div>
        <a href="{home_path}" class="btn">← Back to Home</a>
        <a href="https://github.com/Hmustf/python4control" class="btn">View on GitHub</a>
    </div>

    <div class="main-content">
        <div class="tutorial-navigation">
            <a href="{prev_link}" class="nav-button">← {prev_title}</a>
            <a href="{next_link}" class="nav-button{next_disabled}">{next_title} →</a>
        </div>

        {content}

        <div class="tutorial-navigation">
            <a href="{prev_link}" class="nav-button">← {prev_title}</a>
            <a href="{next_link}" class="nav-button{next_disabled}">{next_title} →</a>
        </div>

        <footer class="site-footer">
            <span class="site-footer-owner">
                <a href="https://github.com/Hmustf/python4control">Python4Control</a> is maintained by 
                <a href="https://github.com/Hmustf">Hmustf</a>.
            </span>
        </footer>
    </div>

    <script>
        // Highlight code blocks
        Prism.highlightAll();
        
        // Force MathJax to reprocess the page
        if (window.MathJax) {{
            window.MathJax.typeset();
        }}
    </script>
</body>
</html>
"""

def get_tutorial_info():
    """Get information about all tutorials."""
    tutorials_dir = Path("tutorials")
    tutorials = []
    
    for tut_dir in sorted(tutorials_dir.glob("tutorial-*")):
        if not tut_dir.is_dir():
            continue
            
        md_file = tut_dir.joinpath("README.md")
        if not md_file.exists():
            continue
            
        with open(md_file, "r") as f:
            content = f.read()
            # Extract title from first h1
            title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
            title = title_match.group(1) if title_match else str(tut_dir.name)
            
            # Extract description from first paragraph after title
            desc_match = re.search(r"^#.+\n+([^\n#]+)", content, re.MULTILINE)
            description = desc_match.group(1).strip() if desc_match else ""
            
        tutorials.append({
            "id": int(tut_dir.name.split("-")[1]),
            "path": str(tut_dir.relative_to(tutorials_dir)),
            "title": title,
            "description": description
        })
    
    return sorted(tutorials, key=lambda x: x["id"])

def convert_md_to_html(md_path, tutorial_info, current_id):
    """Convert a Markdown file to HTML with navigation."""
    with open(md_path, "r") as f:
        md_content = f.read()
    
    # Convert Markdown to HTML with proper code highlighting
    html_content = markdown.markdown(
        md_content,
        extensions=[
            'fenced_code',
            'codehilite',
            'tables',
            'toc',
            'md_in_html'
        ],
        extension_configs={
            'codehilite': {
                'css_class': 'language-python line-numbers',
                'linenums': True,
                'use_pygments': True
            }
        }
    )
    
    # Replace code blocks to work with Prism.js
    html_content = html_content.replace('<div class="codehilite">',
        '<div class="code-toolbar"><pre class="line-numbers language-python"><code class="language-python">')
    
    # Don't add syntax highlighting to output blocks
    html_content = html_content.replace('</div>\n\n<p>Output:</p>\n<div class="codehilite">',
        '</code></pre></div>\n\n<p>Output:</p>\n<div class="output"><pre><code>')
    
    # Fix output blocks
    html_content = html_content.replace('<pre><span></span><code>',
        '<pre><code>')
    
    # Close code blocks properly
    html_content = html_content.replace('</code></pre></div>',
        '</code></pre></div>')
    
    # Get navigation info
    current_tutorial = next(t for t in tutorial_info if t["id"] == current_id)
    prev_tutorial = next((t for t in tutorial_info if t["id"] == current_id - 1), None)
    next_tutorial = next((t for t in tutorial_info if t["id"] == current_id + 1), None)
    
    # Calculate relative paths
    depth = len(str(md_path).split("/")) - 1
    home_path = "../" * depth
    css_path = home_path + "style.css"
    
    # Prepare navigation links
    if prev_tutorial:
        prev_link = f"../{prev_tutorial['path']}"
        prev_title = f"Tutorial {prev_tutorial['id']}"
    else:
        prev_link = home_path
        prev_title = "Home"
        
    if next_tutorial:
        next_link = f"../{next_tutorial['path']}"
        next_title = f"Tutorial {next_tutorial['id']}"
        next_disabled = ""
    else:
        next_link = "#"
        next_title = "Next"
        next_disabled = " disabled"
    
    # Generate HTML
    html = HTML_TEMPLATE.format(
        title=current_tutorial["title"],
        description=current_tutorial["description"],
        content=html_content,
        css_path=css_path,
        home_path=home_path,
        prev_link=prev_link,
        prev_title=prev_title,
        next_link=next_link,
        next_title=next_title,
        next_disabled=next_disabled
    )
    
    return html

def main():
    """Convert all tutorial Markdown files to HTML."""
    # Get info about all tutorials
    tutorial_info = get_tutorial_info()
    
    # Save tutorial info for the website
    with open("docs/tutorials.json", "w") as f:
        json.dump(tutorial_info, f, indent=2)
    
    # Convert each tutorial
    for tutorial in tutorial_info:
        md_path = Path(f"tutorials/{tutorial['path']}/README.md")
        html_path = Path(f"docs/tutorials/{tutorial['path']}/index.html")
        
        # Create output directory if it doesn't exist
        html_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Convert and save
        html_content = convert_md_to_html(md_path, tutorial_info, tutorial["id"])
        with open(html_path, "w") as f:
            f.write(html_content)
        
        print(f"Converted {md_path} -> {html_path}")

if __name__ == "__main__":
    main() 