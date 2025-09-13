import http.server
import socketserver
import webbrowser
import os

PORT = 3000
ARQUIVO = "index.html"

# Garante que o arquivo existe
if not os.path.exists(ARQUIVO):
    raise FileNotFoundError(f"O arquivo {ARQUIVO} não foi encontrado.")

# Abre no navegador
webbrowser.open(f"http://localhost:{PORT}/{ARQUIVO}")

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servindo {ARQUIVO} em http://localhost:{PORT}")
    httpd.serve_forever()