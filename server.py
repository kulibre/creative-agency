import http.server
import socketserver
import mimetypes
import os
import sys

PORT = 8000

# Add explicit MIME types
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('application/javascript', '.mjs')
# Add a catch, but mimetypes uses extension.
# We will override the handler.

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        # Default guess
        ctype = super().guess_type(path)
        
        # Override for specific Framer file patterns
        if '.js' in path and '@' in path: 
            return 'application/javascript'
        if '.js@' in path:
            return 'application/javascript'
        if path.endswith('.mjs'):
            return 'application/javascript'
        if path.endswith('.framercms'): 
            return 'application/json'
        
        # Fallback for weird Framer JS files that might not have extension but are in modules
        if 'modules' in path and 'js' in path:
             return 'application/javascript'

        return ctype
    
    def end_headers(self):
        # Add CORS headers if needed (usually harmless)
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

Handler = CustomHandler

socketserver.TCPServer.allow_reuse_address = True
try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        print("Press Ctrl+C to stop.")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down server.")
    sys.exit(0)
except Exception as e:
    print(f"Error: {e}")
