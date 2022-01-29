from flask import request, redirect, url_for, render_template, session, Response
from werkzeug.utils import secure_filename

from rankapp import app
import os



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST' and request.files['file0']:
        f0 = request.files['file0']
        f0.save(f'./rankapp/application/files/{f0.filename}.csv')
        return render_template('result.html')

    elif request.method == 'POST' and not request.files['file0']:
        message = True
        return render_template('home.html', message=message)

    return render_template('home.html')