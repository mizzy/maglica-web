# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
app = Blueprint('vm', __name__)
import maglica.vm

@app.route('/')
def list():
    virtual_machines = maglica.vm.list()
    return render_template('vm/list.html', virtual_machines=virtual_machines)
