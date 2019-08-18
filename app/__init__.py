from flask import Flask
from dotenv import load_dotenv
from os.path import join, dirname

app = Flask(__name__)
env_path = join(dirname(__file__), '..', '.env')
load_dotenv(env_path)

from app import routes