#!/usr/bin/env python3
"""
server.py

"""
import os
import json
from flask import Flask, request, send_from_directory, redirect, url_for

app = Flask(__name__)

app.config['STATIC'] = 'static'
app.config['html'] = 'html'
app.config['css'] = 'css'
app.config['js'] = 'js'


def save_request(request):
    """
    From:
    https://gist.github.com/TheWaWaR/bd26ef76dabca2d410dd
    """
    req_data = {}
    req_data['endpoint'] = request.endpoint
    req_data['method'] = request.method
    req_data['cookies'] = request.cookies
    req_data['data'] = request.data
    req_data['headers'] = dict(request.headers)
    req_data['headers'].pop('Cookie', None)
    req_data['args'] = request.args
    req_data['form'] = request.form
    req_data['remote_addr'] = request.remote_addr
    files = []
    for name, fs in request.files.iteritems():
        dst = tempfile.NamedTemporaryFile()
        fs.save(dst)
        dst.flush()
        filesize = os.stat(dst.name).st_size
        dst.close()
        files.append({'name': name, 'filename': fs.filename, 'filesize': filesize,
         'mimetype': fs.mimetype, 'mimetype_params': fs.mimetype_params})
    req_data['files'] = files
    return req_data


@app.route('/')
def index():
    return redirect(url_for(
            'get_static_files',
            file_type=app.config['html'],
            file_name='index.html'))


@app.route('/static/<file_type>/<file_name>')
def get_static_files(file_type, file_name):
    dir_path = os.path.join(app.config['STATIC'], app.config[file_type])
    return send_from_directory(dir_path, file_name)


@app.route('/country')
def handle_country():
    r = save_request(request)
    r_json = json.dumps(r, indent=4, sort_keys=True)
    print(r_json)
    return request.args['myCountry']


def main(args):
    app.run(
        host='0.0.0.0',
        port=args.port,
        threaded=False,
        debug=args.debug)


if(__name__ == "__main__"):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port',
                        help="Port that the server will listen on.",
                        type=int, default=8080)
    parser.add_argument('-d', '--debug',
                        help="Whether or not to run in debug mode.",
                        default=False, action='store_true')

    args = parser.parse_args()
    main(args)
