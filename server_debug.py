import http.server
import socketserver
import mimetypes
import os
import sys

PORT = 8081

# Add explicit MIME types
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('application/javascript', '.mjs')

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        # Default guess
        ctype = super().guess_type(path)
        
        # Override for specific Framer file patterns
        if '.js@' in path:
            return 'application/javascript'
        if path.endswith('.mjs'):
            return 'application/javascript'
        if path.endswith('.framercms'): 
            return 'application/json'
            
        return ctype
    
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

Handler = CustomHandler

try:
    print(f"Serving at port {PORT}")
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down server.")
except Exception as e:
    print(f"Error: {e}")
