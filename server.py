#!/usr/bin/env python3
from flask import Flask, send_from_directory, send_file

import os
import ssl

PORT = 80

app = Flask(__name__)


@app.route('/')
def index():
    return send_file('menu.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

if __name__ == "__main__":
    
    try:
        app.run(host='0.0.0.0', port=PORT, debug=False)
    except OSError as e:
        print(f"Ошибка запуска сервера: {e}")
        print(f"Попробуйте другой порт или остановите процесс на порту {PORT}")