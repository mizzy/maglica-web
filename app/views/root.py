# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect
app = Blueprint('root', __name__)

@app.route('/')
def index():
    return redirect('/vm')
