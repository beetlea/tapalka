#!/usr/bin/env python3
import subprocess
import sys
import os

def generate_self_signed_cert():
    """Генерирует самоподписанный SSL сертификат"""
    try:
        # Команда для создания самоподписанного сертификата
        cmd = [
            'openssl', 'req', '-x509', '-newkey', 'rsa:4096', 
            '-keyout', 'YOURPUBLIC.pem', '-out', 'YOURPUBLIC.pem',
            '-days', '365', '-nodes', '-subj', 
            '/C=US/ST=State/L=City/O=Organization/CN=localhost'
        ]
        
        subprocess.run(cmd, check=True)
        print("SSL сертификат YOURPUBLIC.pem успешно создан!")
        print("Сертификат действителен для localhost на 365 дней")
        
    except subprocess.CalledProcessError:
        print("Ошибка: OpenSSL не найден или произошла ошибка при создании сертификата")
        print("Установите OpenSSL или создайте сертификат вручную")
    except FileNotFoundError:
        print("OpenSSL не установлен в системе")
        print("Для Windows: скачайте OpenSSL с https://slproweb.com/products/Win32OpenSSL.html")
        print("Для Linux: sudo apt-get install openssl")
        print("Для macOS: brew install openssl")

if __name__ == "__main__":
    if os.path.exists('YOURPUBLIC.pem'):
        response = input("Файл YOURPUBLIC.pem уже существует. Перезаписать? (y/n): ")
        if response.lower() != 'y':
            print("Операция отменена")
            sys.exit(0)
    
    generate_self_signed_cert()