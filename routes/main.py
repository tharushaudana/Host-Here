from flask import Blueprint, render_template
import os
from config import Config

main_bp = Blueprint('main', __name__, template_folder='../templates')  # Explicitly specify templates folder

@main_bp.route('/')
def index():
    files = os.listdir(Config.CWD)
    return render_template('index.html', files=files, cwd=Config.CWD)