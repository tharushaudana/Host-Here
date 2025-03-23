# HostHere

**HostHere** is a simple Flask-based file hosting and browsing tool. It allows users to browse and view files in the current working directory directly in their web browser. Text-based files can be viewed without downloading, while other files can be downloaded easily.

## Features
- 📂 Browse all files in the current directory.
- 📝 View text-based files (.txt, .py, .html, .css, .js, .md, etc.) directly in the browser.
- 📥 Download non-text files.
- 🎨 Simple and user-friendly interface.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/tharushaudana/Host-Here.git
cd Host-Here
```

### 2. Install Dependencies
Ensure you have Python installed, then install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Run the Server
```bash
python run.py
```
This will start the Flask server on `http://127.0.0.1:5000/`, and you can browse the files.

### Run as a Command
You can add `hosthere` as a command to your system:
1. Add the project folder to your system `PATH`.
2. Use the following command to start the server from any directory:
   ```bash
   hosthere
   ```

