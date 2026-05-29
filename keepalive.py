# keepalive.py
from threading import Thread
from flask import Flask

app = Flask('')

@app.route('/')
def main():
    return "Bot is running!"

def run():
    app.run(host="0.0.0.0", port=10000)

def keep_alive():
    server = Thread(target=run)
    server.start()
