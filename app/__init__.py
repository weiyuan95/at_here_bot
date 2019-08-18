from flask import Flask
from dotenv import load_dotenv
from os.path import join, dirname
import logging

app = Flask(__name__)

env_path = join(dirname(__file__), '..', '.env')
load_dotenv(env_path)

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

from app import routes