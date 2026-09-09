import http.server, socketserver, webbrowser, os
PORT=8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))
Handler=http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("",PORT),Handler) as httpd:
    print(f"Family Tree running at http://localhost:{PORT}")
    try: webbrowser.open(f"http://localhost:{PORT}")
    except: pass
    try: httpd.serve_forever()
    except KeyboardInterrupt: pass
