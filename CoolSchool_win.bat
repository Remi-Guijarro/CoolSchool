runas /user:Administrator cmd
cd /d %~dp0
pip install colorama 
pip install sympy
pip install numpy
pip install pyinstaller
pip install flask
cls

echo 

set /p bool_flask_app=Do you want to run the flask app version [y/n]?: 
if [%bool_flask_app%] equ [y] (
	set FLASK_APP=CoolSchool_flask.py
	set FLASK_DEBUG=1
	flask run
) else (
	python ./CoolSchool.py
    cmd /k
)
