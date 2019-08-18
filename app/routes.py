from app import app
import app.bot.HereBot as HereBot

@app.route('/')
def index():
    return '<h1>hi</h1>'

@app.route('/key_check')
def bot_test():
    return HereBot.auth_check()