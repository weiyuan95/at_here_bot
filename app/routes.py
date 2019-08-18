from app import app
import os
import app.bot.HereBot as HereBot
from flask import request
import logging

@app.route('/')
def index():
    return '<h1>hi</h1>'

@app.route('/key_check')
def bot_test():
    return HereBot.auth_check()

@app.route(f'/{os.getenv("HOOK_SECRET")}')
def get_updates():
    logging.info(f'{request.json}\n\n')
    return f'{request.json}'