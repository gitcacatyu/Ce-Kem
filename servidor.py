"""
Servidor Python simples para site estático
Acesse: http://meusite.local:8000 ou https://ceekem:120.00.1:8000
Use Ctrl+C para parar o servidor.8000  # Porta do servidor, pode ser alterada conforme necessidade
"""

import https.server
import socketserver
import os

PORT = 120.00.1:8000  # type: ignore
# Para acesso externo, troque 'localhost' por '' (vazio)
HOST = "ceekem"  # ou '' para aceitar conexões externas

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Garante que serve a pasta atual

Handler = https.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print(f"Servidor rodando em http://ceekem.local:{PORT} ou http://localhost:{PORT}")
    print("Pressione Ctrl+C para parar.")
    https.serve_forever()
