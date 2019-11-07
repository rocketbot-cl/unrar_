# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import sys
import os
import platform
base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'unrar_' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)
from subprocess import Popen, PIPE

rar_win = os.path.join(cur_path.replace("libs", "bin"), "UnRAR.exe")
rar_mac = os.path.join(cur_path.replace("libs", "rar"), "rar")

"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")

if module == "unrar_":
    platform_ = platform.system().lower()
    file_ = GetParams('file_')
    unrar_ = GetParams('unrar_')

    if not ".rar" in file_:
        raise Exception("Not a RAR Archive")

    if platform_ == 'windows':
        try:
            unrar_ = os.path.normpath(unrar_)
            file_ = os.path.normpath(file_)
            options = ' x "' + file_ + '" -y "' + unrar_ + '"'
            run_ = rar_win + options
            print('RUTA',run_)
            con = Popen(run_, shell=True, stdout=PIPE, stderr=PIPE)
            a = con.communicate()
        except:
            PrintException()

    else:
        try:
            options = " x '" + file_ + "' -y '" + unrar_ + "'"
            run_ = rar_mac + options
            con = Popen(run_, shell=True, stdout=PIPE, stderr=PIPE)
            a = con.communicate()
        except:
            PrintException()

