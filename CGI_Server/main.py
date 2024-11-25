from http.server import HTTPServer, CGIHTTPRequestHandler
import os

class Server(CGIHTTPRequestHandler):
    cgi_directories = ["/cgi-bin"]  # Путь к CGI-скриптам

    def do_GET(self):
        if self.path == "/":
            # Перенаправляем запрос к HTML-файлу
            self.path = "/templates/index.html"
        return super().do_GET()

PORT = 8000

if __name__ == "__main__":
    # Устанавливаем текущую директорию как базовую
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = HTTPServer(("", PORT), Server)
    print(f"Сервер запущен: http://localhost:{PORT}")
    server.serve_forever()
