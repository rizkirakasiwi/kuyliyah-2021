<?php

namespace App\Controllers;

use CodeIgniter\RESTful\ResourceController;

class StudentClass extends ResourceController
{
    protected $modelName = 'App\Models\StudentClassModel';
    protected $format    = 'json';

    public function getClass($school_code){
        return $this->respond($this->model->getClass($school_code));
    }
}