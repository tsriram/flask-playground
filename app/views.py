from app import app
from flask import request, render_template
from werkzeug.utils import secure_filename

@app.route('/')
def index():
    return 'Index page'

@app.route('/hello/')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return "User %s" % username

@app.route('/post/<int:post_id>/')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload_form.html')
    if request.method == 'POST':
        f = request.files['my_file']
        print "Uploaded file name - %s" % f.filename
        f.save('/tmp/' + secure_filename(f.filename));
        return 'File saved successfully'