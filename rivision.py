from flask import Flask, request, redirect, url_for, Response, session, render_template
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = os.getenv('secret_code')