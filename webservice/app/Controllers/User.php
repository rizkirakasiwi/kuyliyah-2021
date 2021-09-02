<?php

namespace App\Controllers;

use CodeIgniter\RESTful\ResourceController;

class User extends ResourceController
{
    protected $modelName = 'App\Models\UserModel';
    protected $format    = 'json';

    public function getNameByEmail($email){
        $select = $this->model->getNameByEmail($email);
        return $this->respond($select);
    }

    public function getUserByEmail($email){
        $select = $this->model->getUserByEmail($email);
        return $this->respond($select);
    }

    public function login(){
        $email = $this->request->getPost('email');
        $password = $this->request->getPost('password');
        $login = $this->model->login($email, $password);
        return $this->respond($login);
    }

}