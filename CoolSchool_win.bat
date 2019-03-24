runas /user:Administrator cmd
cd /d %~dp0
pip install colorama 
pip install sympy
pip install numpy
cls
python ./CoolSchool.py
cmd /k