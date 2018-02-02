from flask import request, Flask

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def data():
    print(request.json)
    return "Hello"

app.run(port=8000)
