import os
import threading
import http.server
import socketserver
import asyncio

from bot import dp, bot

def run_health_server():
    port = int(os.getenv("PORT", "8000"))
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Health server listening on 0.0.0.0:{port}")
        httpd.serve_forever()

async def main():
    # Start polling the bot
    await dp.start_polling(bot)

if __name__ == "__main__":
    t = threading.Thread(target=run_health_server, daemon=True)
    t.start()
    asyncio.run(main())
