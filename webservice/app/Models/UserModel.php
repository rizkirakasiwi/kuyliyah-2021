<?php

namespace App\Models;

use CodeIgniter\Model;

class UserModel extends Model
{
    protected $table = 'student';

    protected $db;

    public function __construct(){
        $this->db = \Config\Database::connect();
    }

    public function getNameByEmail($email){
        $student = $this->db->query("SELECT name FROM student WHERE email = '".$email."'")->getResult();
        $teacher = $this->db->query("SELECT name FROM teacher WHERE email = '".$email."'")->getResult();

        if($student){
            return $student[0];
        }else if($teacher){
            return $teacher[0];
        }else{
            return ['name' => 'Unknown'];
        }
    }

    public function getUserByEmail($email){
        $query = "SELECT accounts.*, schools.name as school_name FROM accounts INNER JOIN schools ON accounts.school_code = schools.code WHERE email = '".$email."'";
        $login = $this->db->query($query)->getResult();
        if($login){
            return $login[0];
        }else{
            return ['message' => 'User tidak ditemukan'];
        }
    }

    public function login($email, $password){
        $query = "SELECT accounts.*, schools.name as school_name FROM accounts INNER JOIN schools ON accounts.school_code = schools.code WHERE email = '".$email."' AND password= '".$password."'";
        $login = $this->db->query($query)->getResult();
        if($login){
            return ['code' => 200, 'data' => $login[0]];
        }else{
            return ['code' => 402, 'data' => ['message' => 'User tidak ditemukan']];
        }
    }

}