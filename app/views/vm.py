# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
app = Blueprint('vm', __name__)
import maglica.vm

@app.route('')
def list():
    vms = maglica.vm.list()
    return render_template('vm/list.html', vms=vms)

@app.route('/console/<name>')
def console(name):
    info = maglica.vm.info({"name": name})
    return render_template('vm/console.html', info=info)


