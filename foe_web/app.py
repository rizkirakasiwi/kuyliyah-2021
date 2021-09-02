from flask import Flask, render_template, Response, request, redirect, url_for, session
from camera import VideoCamera
from webservice_manager import get_user, login, get_class

app = Flask(__name__)
app.secret_key = "123qweasdjkl"


@app.route('/attendance')
def attendance():
    if "email" in session:
        return render_template('attendance.html')
    else:
        return redirect(url_for('login_layout'))

@app.route('/home')
def home():
    if "email" in session:
        return render_template('home.html')
    else:
        return redirect(url_for('login_layout'))

@app.route('/report')
def report():
    if "email" in session:
        user = get_user(session['email'])
        school_code = user['school_code']
        student_class = get_class(school_code)
        return render_template('report.html', student_class=student_class)
    else:
        return redirect(url_for('login_layout'))
    
@app.route("/handle_report", methods=['POST'])
def handle_report():
    class_id = request.form['student_class']
    time_from = request.form['from_time']
    time_to = request.form['to_time']
    is_guru = False
    user = get_user(session['email'])
    school_code = user['school_code']
    
    return f"{class_id}/{time_from}/{time_to}/{is_guru}/{school_code}"

@app.route("/handle_report_teacher", methods=['POST'])
def handle_report_teacher():
    time_from = request.form['from_time']
    time_to = request.form['to_time']
    is_guru = True
    user = get_user(session['email'])
    school_code = user['school_code']
    
    return f"/{time_from}/{time_to}/{is_guru}/{school_code}"


@app.route('/report_teacher')
def report_teacher():
    if "email" in session:
        return render_template('report_teacher.html')
    else:
        return redirect(url_for('login_layout'))

@app.route('/logout')
def logout():
    session.pop("email", None)
    return redirect(url_for('login_layout'))


def load_user(email):
    return get_user(email)


@app.route('/login')
def login_layout():
    if "email" in session:
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/handle_login', methods=['POST'])
def handle_login():
    email = request.form['email']
    session["email"] = email
    password = request.form['password']
    log = login(email, password)
    if log['code'] == 200:
        print('login berhasil')
        return redirect(url_for('home'))
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
def recognize():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def gen_camera(camera):
    while True:
        frame = camera.get_camera()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n'+frame)
               
@app.route('/camera')
def camera():
    return Response(gen_camera(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)