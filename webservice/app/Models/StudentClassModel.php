<?php

namespace App\Models;

use CodeIgniter\Model;

class StudentClassModel extends Model
{
    protected $table = 'student_class';

    protected $db;

    public function __construct(){
        $this->db = \Config\Database::connect();
    }

    public function getClass($school_code){
        return $this->db->query("SELECT * FROM student_class WHERE school_code = '".$school_code."'")->getResult();
    }
}