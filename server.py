#!/usr/bin/env python3
import http.server
import socketserver
import ssl
import os

PORT = 80

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_GET(self):
        if self.path == '/':
            self.path = '/menu.html'
        return super().do_GET()

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        # Настройка SSL
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        try:
            context.load_cert_chain('YOURPUBLIC.pem', 'YOURPUBLIC.pem')
            httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
            print(f"HTTPS сервер запущен на https://localhost:{PORT}")
        except FileNotFoundError:
            print("Файл YOURPUBLIC.pem не найден. Запуск HTTP сервера...")
            print(f"HTTP сервер запущен на http://localhost:{PORT}")
        except Exception as e:
            print(f"Ошибка SSL: {e}. Запуск HTTP сервера...")
            print(f"HTTP сервер запущен на http://localhost:{PORT}")
        
        print("Для остановки нажмите Ctrl+C")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nСервер остановлен")