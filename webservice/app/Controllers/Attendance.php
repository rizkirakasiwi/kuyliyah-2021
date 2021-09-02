<?php

namespace App\Controllers;

use CodeIgniter\RESTful\ResourceController;

class Attendance extends ResourceController
{
    protected $modelName = 'App\Models\AttendanceModel';
    protected $format    = 'json';

    public function doAttendance(){
        $email = $this->request->getPost("email");
        $time_attendance_at = $this->request->getPost("time");

        $result = $this->model->doAttendance($email, $time_attendance_at);

        return $this->respond($result, 200);
    }

}