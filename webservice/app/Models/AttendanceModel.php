<?php

namespace App\Models;

use CodeIgniter\Model;

class AttendanceModel extends Model
{
    protected $table = 'student_attendance';

    protected $db;

    public function __construct(){
        $this->db = \Config\Database::connect();
    }

    public function doAttendance($email, $attendace_time_at){
        $student = $this->db->query("SELECT * FROM student WHERE email = '".$email."'")->getRow();
        $teacher = $this->db->query("SELECT * FROM teacher WHERE email = '".$email."'")->getRow();

        if($student){
            $school_code = $student->school_code;

            $time = $this->db->query("SELECT * FROM student_attendance_time WHERE school_code = '".$school_code."'")->getRow();
            
            $time_in = $time->time_in;
            $time_out = $time->time_out;
            
            $time_in_start = "01:00:00";
            $time_out_end = "23:00:00";

            if($attendace_time_at <= $time_in && $attendace_time_at > $time_in_start && $attendace_time_at < $time_out){
                $check_user_already_done_absent = $this->db->query("SELECT id FROM student_attendance WHERE email = '".$email."' AND date = CURDATE() AND time_in IS NOT NULL")->getResult();
                if($check_user_already_done_absent){
                    return ['message' => "You've done attendance"];
                }else{
                    $insert_query = "INSERT INTO student_attendance(date, time_in, time_out, email, school_code) VALUES(CURDATE(), '".$attendace_time_at."', null, '".$email."', '".$school_code."')";
                    $insert = $this->db->query($insert_query);
                    if($insert){
                        return ['message' => 'Attendance is successful'];
                    }else{
                        return ['message' => 'Attendance is failed'];
                    }
                }
            }else if($attendace_time_at > $time_in && $attendace_time_at < $time_out){
                $check_user_already_done_absent = $this->db->query("SELECT id FROM student_attendance WHERE email = '".$email."' AND date = CURDATE() AND time_in IS NOT NULL")->getResult();
                if($check_user_already_done_absent){
                    return ['message' => "You've done attendance"];
                }else{
                    $insert_query = "INSERT INTO student_attendance(date, time_in, time_out, email, school_code, description) VALUES(CURDATE(), '".$attendace_time_at."', null, '".$email."', '".$school_code."', 't')";
                    $insert = $this->db->query($insert_query);
                    if($insert){
                        return ['message' => 'Attendance is successful'];
                    }else{
                        return ['message' => 'Attendance is failed'];
                    }
                }
            }else if($attendace_time_at >= $time_out && $attendace_time_at < $time_out_end){
                $check_user_already_done_absent = $this->db->query("SELECT id FROM student_attendance WHERE email = '".$email."' AND date = CURDATE() AND time_out IS NOT NULL")->getResult();
                if($check_user_already_done_absent){
                    return ['message' => "You've done attendance"];
                }else{
                    $check_user_do_time_in = $this->db->query("SELECT id FROM student_attendance WHERE email = '".$email."' AND date = CURDATE() AND time_in IS NOT NULL")->getResult();
                    if(!$check_user_do_time_in){
                        $insert_query = "INSERT INTO student_attendance(date, time_in, time_out, email, school_code) VALUES(CURDATE(), null, '".$attendace_time_at."', '".$email."', '".$school_code."')";
                        $insert = $this->db->query($insert_query);
                        if($insert){
                            return ['message' => 'Attendance is successful'];
                        }else{
                            return ['message' => 'Attendance is failed'];
                        }
                    }else{
                        $update_query = "UPDATE student_attendance SET time_out = '".$attendace_time_at."' WHERE email = '".$email."' AND date = CURDATE()";
                        $query = $this->db->query($update_query);
                        if($query){
                            return ['message' => 'Attendance is successful'];
                        }else{
                            return ['message' => 'Attendance is failed'];
                        }
                    }
                }
            }else{
                return ['message' => 'Cannot do attendance yet'];
            }
        }
    }
}