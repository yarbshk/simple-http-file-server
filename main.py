from http.server import HTTPServer, BaseHTTPRequestHandler
import os

UPLOAD_DIR = "./uploads"  # Folder to store uploaded files

class SimplePUTHandler(BaseHTTPRequestHandler):
    def do_PUT(self):
        # Extract filename from the path
        filename = os.path.basename(self.path)
        if not filename:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Filename not provided in URL.")
            return

        # Ensure upload directory exists
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        filepath = os.path.join(UPLOAD_DIR, filename)
        file_length = int(self.headers['Content-Length'])

        with open(filepath, 'wb') as output_file:
            output_file.write(self.rfile.read(file_length))

        self.send_response(201)
        self.end_headers()
        self.wfile.write(b"File uploaded successfully.")

if __name__ == '__main__':
    server_address = ('', 8000)  # Listen on port 8000
    httpd = HTTPServer(server_address, SimplePUTHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()
