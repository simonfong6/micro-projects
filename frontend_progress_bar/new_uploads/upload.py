from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'media' in request.files:
        return 100

    return render_template('upload.html')

@app.route('/upload/progress')
def progress():
    return 100
    
@app.route('/progress')
def short_progress():
    return 100

if __name__ == '__main__':
	app.run(debug=True)
