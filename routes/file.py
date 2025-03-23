from flask import Blueprint, send_file, render_template, abort
import os
from config import Config

file_bp = Blueprint('file', __name__)

@file_bp.route('/file/<path:filename>')
def serve_file(filename):
    filepath = os.path.join(Config.CWD, filename)
    
    if not os.path.isfile(filepath):
        return abort(404)

    text_extensions = [
        '.txt', '.py', '.html', '.css', '.js', '.md', '.csv', '.json', '.xml', '.yaml', '.yml',
        '.c', '.cpp', '.h', '.hpp', '.java', '.cs', '.php', '.rb', '.swift', '.go', '.rs', '.ts',
        '.sh', '.bat', '.cmd', '.ini', '.cfg', '.toml', '.makefile', '.dockerfile', '.gitignore'
    ]

    if any(filename.endswith(ext) for ext in text_extensions):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace("</", "&lt;/")  # Escape "</" to prevent breaking textarea
        return render_template('view_file.html', filename=filename, content=content)

    return send_file(filepath, as_attachment=True)