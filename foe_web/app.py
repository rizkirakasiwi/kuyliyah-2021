from flask import Flask, render_template, Response, request, redirect, url_for
from camera import VideoCamera
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from webservice_manager import get_user, login


app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/attendance')
def attendance():
    return render_template('attendance.html')

@app.route('/home')
def home():
    return render_template('home.html')

@login_manager.user_loader
def load_user(email):
    return get_user(email)


@app.route('/login')
def login_layout():
    return render_template('login.html')

@app.route('/handle_login', methods=['POST'])
def handle_login():
    email = request.form['email']
    password = request.form['password']
    log = login(email, password)
    if log['code'] == 200:
        # login_user(log)
        print('login berhasil')
        return redirect(url_for('attendance'))
    else:
        print('login gagal')
        return 'login gagal'

def gen(camera):
    while True:
        
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n'+frame
               + b'\r\n\r\n')
        
@app.route('/recognize')
# @login_required
def recognize():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def gen_camera(camera):
    while True:
        frame = camera.get_camera()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n'+frame)
               
@app.route('/camera')
# @login_required
def camera():
    return Response(gen_camera(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)