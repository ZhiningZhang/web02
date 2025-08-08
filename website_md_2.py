import os
import markdown
import pypandoc
from collections import defaultdict

# pypandoc.download_pandoc()

def convert_all_md(source_dir, output_dir):
    folder_links = defaultdict(list)

    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)

                # Get relative path
                rel_path = os.path.relpath(md_path, source_dir)
                html_rel_path = rel_path.replace(".md", ".html")

                # Target HTML path
                html_path = os.path.join(output_dir, html_rel_path)
                os.makedirs(os.path.dirname(html_path), exist_ok=True)

                # Read and convert Markdown
                with open(md_path, "r", encoding='utf-8', errors='ignore') as f:
                    text = f.read()
                # html = markdown.markdown(text)
                html = pypandoc.convert_text(text, 'html', format='md')

                with open(html_path, "w", encoding='utf-8', errors='ignore') as f:
                    f.write(f"<html><body>{html}</body></html>")

                # Group by folder
                folder = os.path.dirname(html_rel_path).replace("\\", "/") or "."
                folder_links[folder].append(html_rel_path.replace("\\", "/"))

    # Generate index.html with nested folders
    index_path = os.path.join(output_dir, "index.html")
    with open(index_path, "w", encoding='utf-8') as f:
        f.write("""<html>
<head>
<style>
    body { font-family: Arial, sans-serif; font-size: 18px; padding: 20px; }
    h1 { font-size: 26px; }
    h2 { font-size: 22px; margin-top: 30px; color: #333366; }
    ul { list-style-type: none; padding-left: 20px; }
    li { margin: 5px 0; }
    a { text-decoration: none; color: #0066cc; }
    a:hover { text-decoration: underline; }
</style>
</head>
<body>
<h1>Hannah</h1>
""")
        for folder in sorted(folder_links):
            f.write(f'<h2>{folder}</h2>\n<ul>\n')
            for link in sorted(folder_links[folder]):
                f.write(f'<li><a href="{link}" target="_blank">{link}</a></li>\n')
            f.write('</ul>\n')
        f.write("</body></html>")

    print(f"✅ HTML files created in: {output_dir}")
    print(f"📄 Index file: {index_path}")

# Example usage
convert_all_md(
    source_dir=r'C:\Temp\ANNUITIES',
    output_dir=r'C:\Temp\ANNUITIES_HTML'
)
