from database import db, cursor, sql
from datetime import datetime


def log():
    query = "SELECT uid, time FROM log WHERE date = CURDATE() ORDER BY time DESC"
    cursor.execute(query)
    return cursor.fetchall()
          

def to_datetime(time):
    time_now = datetime.now()
    ntime = datetime.strptime(str(time), '%H:%M:%S')
    return time_now.replace(
        hour=ntime.time().hour, 
        minute=ntime.time().minute, 
        second=ntime.time().second, microsecond=0)
    
def get_name(email):
    cursor.execute(f"SELECT name FROM student WHERE email = '{email}' LIMIT 1")
    student = cursor.fetchone()
    if student:
        return student[0]
    else:
        cursor.execute(f"SELECT name FROM teacher WHERE email = '{email}' LIMIT 1")
        teacher = cursor.fetchone()
        if teacher:
            return teacher[0]
        else:
            return "[Unknow]"
        

def do_attendance(email):
    attendance_time_at = datetime.now()
    cursor.execute(f"SELECT * FROM student WHERE email = '{email}'")
    student = cursor.fetchall()
    
    time_in_start = to_datetime("00:00:00")
    time_out_end = to_datetime("23:00:00")
    
    if student:
        cursor.execute(f"SELECT school_code FROM student WHERE email = '{email}'")
        school_code = cursor.fetchone()
        
        cursor.execute(f"SELECT uid FROM student WHERE email = '{email}'")
        student_uid = cursor.fetchone()
        
        if school_code:
            school_code = school_code[0]
            cursor.execute(f"SELECT time_in, time_out FROM student_attendance_time WHERE school_code = '{school_code}'")
            time = cursor.fetchall()
            if time:
                time_in = to_datetime(time[0][0])
                time_out = to_datetime(time[0][1])
                if attendance_time_at <= time_in and attendance_time_at > time_in_start and attendance_time_at < time_out:
                    cursor.execute(f"SELECT id FROM student_attendance WHERE email = '{email}' AND date = CURDATE() AND time_in IS NOT NULL")
                    check_done_absent = cursor.fetchall()
                    if check_done_absent:
                        return "Anda sudah melakukan absensi"
                    else:
                        try:
                            db.autocommit = False
                            attendance_time_at = attendance_time_at.strftime('%H:%M:%S')
                            query = "INSERT INTO student_attendance(date, time_in, time_out, email, school_code) VALUES(CURDATE(), %s, null, %s, %s)"
                            values = (attendance_time_at, email, school_code)
                            cursor.execute(query, values)
                            
                            query = "INSERT INTO log(uid,school_code, date, time) VALUES(%s,%s, CURDATE(), %s)"
                            values = (student_uid[0], school_code, attendance_time_at)
                            cursor.execute(query, values)
                            db.commit()
                            if cursor.rowcount > 0:
                                return "Absensi berhasil"
                            else:
                                return "Absensi gagal"
                        except sql.Error as error:
                            db.rollback()
                            return "Absensi gagal"
                        
                elif attendance_time_at > time_in and attendance_time_at < time_out:    
                    cursor.execute(f"SELECT id FROM student_attendance WHERE email = '{email}' AND date = CURDATE() AND time_in IS NOT NULL")
                    check_done_absent = cursor.fetchall()
                    if check_done_absent:
                        return "Anda sudah melakukan absensi"
                    else:
                        try:
                            db.autocommit = False
                            attendance_time_at = attendance_time_at.strftime('%H:%M:%S')
                            query =  "INSERT INTO student_attendance(date, time_in, time_out, email, school_code, description) VALUES(CURDATE(), %s, null, %s, %s, 't')"
                            values = (attendance_time_at, email, school_code)
                            cursor.execute(query, values)
                            query = "INSERT INTO log(uid,school_code, date, time) VALUES(%s,%s, CURDATE(), %s)"
                            values = (student_uid[0], school_code, attendance_time_at)
                            cursor.execute(query, values)
                            db.commit()
                            if cursor.rowcount > 0:
                                return "Absensi berhasil, Terlambat"
                            else:
                                return "Absensi gagal"
                        except sql.Error as error:
                            db.rollback()
                            return "Absensi gagal"
                        
                elif attendance_time_at >= time_out and attendance_time_at < time_out_end:
                    cursor.execute(f"SELECT id FROM student_attendance WHERE email = '{email}' AND date = CURDATE() AND time_out IS NOT NULL")
                    check_done_absent = cursor.fetchall()
                    if check_done_absent:
                        return "Anda sudah melakukan absensi"
                    else:
                        cursor.execute(f"SELECT id FROM student_attendance WHERE email = '{email}' AND date = CURDATE() AND time_in IS NOT NULL")
                        check_already_do_attendance_in = cursor.fetchall()
                        if check_already_do_attendance_in:
                            try:
                                db.autocommit = False
                                attendance_time_at = attendance_time_at.strftime('%H:%M:%S')
                                query = "UPDATE student_attendance SET time_out = '{attendance_time_at}' WHERE email = '{email}' AND date = CURDATE()"
                                cursor.execute(query)
                                query = "INSERT INTO log(uid,school_code, date, time) VALUES(%s,%s, CURDATE(), %s)"
                                values = (student_uid[0], school_code, attendance_time_at)
                                cursor.execute(query, values)
                                db.commit()
                                if cursor.rowcount > 0:
                                    return "Absensi berhasil"
                                else:
                                    return "Absensi gagal"
                            except sql.Error as error:
                                db.rollback()
                                return "Absensi gagal"
                        else:
                            try:
                                db.autocommit = False
                                attendance_time_at = attendance_time_at.strftime('%H:%M:%S')
                                query = "INSERT INTO student_attendance(date, time_in, time_out, email, school_code) VALUES(CURDATE(), null, %s, %s, %s)"
                                values = (attendance_time_at, email, school_code)
                                cursor.execute(query, values)
                                query = "INSERT INTO log(uid,school_code, date, time) VALUES(%s,%s, CURDATE(), %s)"
                                values = (student_uid[0], school_code, attendance_time_at)
                                cursor.execute(query, values)
                                db.commit()
                                if cursor.rowcount > 0:
                                    return "Absensi berhasil"
                                else:
                                    return "Absensi gagal"
                            except sql.Error as error:
                                db.rollback()
                                return "Absensi gagal"
                             
    else:
        cursor.execute(f"SELECT school_code FROM teacher WHERE email = '{email}'")
        school_code = cursor.fetchone()
        
        cursor.execute(f"SELECT uid FROM teacher WHERE email = '{email}'")
        teacher_uid = cursor.fetchone()
        if school_code:
            school_code = school_code[0]
            cursor.execute(f"SELECT time_in, time_out FROM teacher_attendance_time WHERE school_code = '{school_code}'")
            time = cursor.fetchall()
            if time:
                time_in = to_datetime(time[0][0])
                time_out = to_datetime(time[0][1])
                if attendance_time_at <= time_in and attendance_time_at > time_in_start and attendance_time_at < time_out:
                    cursor.execute(f"SELECT id FROM teacher_attendance WHERE email = '{email}' AND date = CURDATE() AND time_in IS NOT NULL")
                    check_done_absent = cursor.fetchall()
                    if check_done_absent:
                        return "Anda sudah melakukan absensi"
                    else:
                        try:
                            db.autocommit = False
                            attendance_time_at = attendance_time_at.strftime('%H:%M:%S')
                            query = "INSERT INTO teacher_attendance(date, time_in, time_out, email, school_code) VALUES(CURDATE(), %s, null, %s, %s)"
                            values = (attendance_time_at, email, school_code)
                            cursor.execute(query, values)
                            query = "INSERT INTO log(uid,school_code, date, time) VALUES(%s,%s, CURDATE(), %s)"
                            values = (teacher_uid[0], school_code, attendance_time_at)
                            cursor.execute(query, values)
                            db.commit()
                            if cursor.rowcount > 0:
                                return "Absensi berhasil"
                            else:
                                return "Absensi gagal"
                        except sql.Error as error:
                            db.rollback()
                            return "Absensi gagal"
                        
                elif attendance_time_at > time_in and attendance_time_at < time_out:    
                    cursor.execute(f"SELECT id FROM teacher_attendance WHERE email = '{email}' AND date = CURDATE() AND time_in IS NOT NULL")
                    check_done_absent = cursor.fetchall()
                    if check_done_absent:
                        return "Anda sudah melakukan absensi"
                    else:
                        try:
                            db.autocommit = False
                            attendance_time_at = attendance_time_at.strftime('%H:%M:%S')
                            query =  "INSERT INTO teacher_attendance(date, time_in, time_out, email, school_code, description) VALUES(CURDATE(), %s, null, %s, %s, 't')"
                            values = (attendance_time_at, email, school_code)
                            cursor.execute(query, values)
                            query = "INSERT INTO log(uid,school_code, date, time) VALUES(%s,%s, CURDATE(), %s)"
                            values = (teacher_uid[0], school_code, attendance_time_at)
                            cursor.execute(query, values)
                            db.commit()
                            if cursor.rowcount > 0:
                                return "Absensi berhasil, Terlambat"
                            else:
                                return "Absensi gagal"
                        except sql.Error as error:
                            db.rollback()
                            return "Absensi gagal"
                elif attendance_time_at >= time_out and attendance_time_at < time_out_end:
                    cursor.execute(f"SELECT id FROM teacher_attendance WHERE email = '{email}' AND date = CURDATE() AND time_out IS NOT NULL")
                    check_done_absent = cursor.fetchall()
                    if check_done_absent:
                        return "Anda sudah melakukan absensi"
                    else:
                        cursor.execute(f"SELECT id FROM teacher_attendance WHERE email = '{email}' AND date = CURDATE() AND time_in IS NOT NULL")
                        check_already_do_attendance_in = cursor.fetchall()
                        if check_already_do_attendance_in:
                            try:
                                db.autocommit = False
                                attendance_time_at = attendance_time_at.strftime('%H:%M:%S')
                                query = "UPDATE teacher_attendance SET time_out = '{attendance_time_at}' WHERE email = '{email}' AND date = CURDATE()"
                                cursor.execute(query)
                                query = "INSERT INTO log(uid,school_code, date, time) VALUES(%s,%s, CURDATE(), %s)"
                                values = (teacher_uid[0], school_code, attendance_time_at)
                                cursor.execute(query, values)
                                db.commit()
                                if cursor.rowcount > 0:
                                    return "Absensi berhasil"
                                else:
                                    return "Absensi gagal"
                            except sql.Error as error:
                                db.rollback()
                                return "Absensi gagal"
                        else:
                            try:
                                db.autocommit = False
                                attendance_time_at = attendance_time_at.strftime('%H:%M:%S')
                                query = "INSERT INTO teacher_attendance(date, time_in, time_out, email, school_code) VALUES(CURDATE(), null, %s, %s, %s)"
                                values = (attendance_time_at, email, school_code)
                                cursor.execute(query, values)
                                query = "INSERT INTO log(uid,school_code, date, time) VALUES(%s,%s, CURDATE(), %s)"
                                values = (teacher_uid[0], school_code, attendance_time_at)
                                cursor.execute(query, values)
                                db.commit()
                                if cursor.rowcount > 0:
                                    return "Absensi berhasil"
                                else:
                                    return "Absensi gagal"
                            except sql.Error as error:
                                db.rollback()
                                return "Absensi gagal"
                            
# print(do_attendance('rizkirakasiwirizki@gmail.com'))
