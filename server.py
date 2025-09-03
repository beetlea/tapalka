#!/usr/bin/env python3
from flask import Flask, send_from_directory, send_file, request, jsonify

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

@app.route('/user_info', methods=['POST'])
def user_info():
    data = request.get_json()
    if data:
        user_id = data.get('id')
        username = data.get('username', 'Не указан')
        first_name = data.get('first_name', 'Не указано')
        last_name = data.get('last_name', '')
        
        print(f"Пользователь подключился:")
        print(f"ID: {user_id}")
        print(f"Username: @{username}")
        print(f"Имя: {first_name} {last_name}")
        print("-" * 40)
        
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error'})

if __name__ == "__main__":
    
    try:
        app.run(host='0.0.0.0', port=PORT, debug=False)
    except OSError as e:
        print(f"Ошибка запуска сервера: {e}")
        print(f"Попробуйте другой порт или остановите процесс на порту {PORT}")