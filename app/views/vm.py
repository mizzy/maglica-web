# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
app = Blueprint('vm', __name__)

@app.route('/')
def index():
    return render_template('vm/index.html')
