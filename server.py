import http.server
import socketserver

PORT = 8000

# Crear un servidor HTTP que sirva archivos de la carpeta actual
Handler = http.server.SimpleHTTPRequestHandler

# Iniciar el servidor en el puerto especificado
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Sirviendo en http://localhost:{PORT}")
    httpd.serve_forever()
