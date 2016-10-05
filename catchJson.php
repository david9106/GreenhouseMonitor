<?php
//cachamos el json que envio la rpi
$content = file_get_contents("php://input");
//Enviamos el json al .py encargado de la insercion de datos
$result = shell_exec('python ./main.py ' . escapeshellarg(json_encode($content)));
echo $result;


/*
import sys, json
data = json.loads(sys.argv[1])
measures = json.dumps(data)


*/
?>