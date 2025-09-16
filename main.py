# main.py
import os
import threading
import http.server
import socketserver

from aiogram import executor
from bot import dp

def run_health_server():
    port = int(os.getenv("PORT", "8000"))
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Health server listening on 0.0.0.0:{port}")
        httpd.serve_forever()

if __name__ == "__main__":
    # Start health server in background (so Render's web health check passes)
    t = threading.Thread(target=run_health_server, daemon=True)
    t.start()

    # Start the aiogram polling (blocks)
    executor.start_polling(dp, skip_updates=True)
