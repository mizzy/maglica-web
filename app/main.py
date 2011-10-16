# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

from views import root
app.register_blueprint(root.app, url_prefix='/')

from views import vm
app.register_blueprint(vm.app, url_prefix='/vm')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
