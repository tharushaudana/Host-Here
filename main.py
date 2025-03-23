from flask import Flask, send_file, render_template_string
import os

app = Flask(__name__)
CWD = os.getcwd()

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>File Browser</title>
</head>
<body>
    <h1>Files in {{ cwd }}</h1>
    <ul>
        {% for file in files %}
            <li><a href="/file/{{ file }}">{{ file }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route('/')
def index():
    files = os.listdir(CWD)
    return render_template_string(TEMPLATE, files=files, cwd=CWD)

@app.route('/file/<path:filename>')
def serve_file(filename):
    filepath = os.path.join(CWD, filename)
    if not os.path.isfile(filepath):
        return "File not found", 404
    
    # Check if file is text-based
    text_extensions = ['.txt', '.py', '.html', '.css', '.js', '.md', '.csv']
    if any(filename.endswith(ext) for ext in text_extensions):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        # Escape </ to prevent breaking the textarea
        content = content.replace("</", "&lt;/")
        return f"<textarea style='width:100%; height:400px;'>{content}</textarea>"
    
    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)