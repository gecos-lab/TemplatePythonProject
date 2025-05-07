SET foldername=venv
if EXIST %foldername% (
call %foldername%\Scripts\activate
python -m pip install --upgrade pip
python -m pip install --upgrade -r requirements.txt 
) else ( 
py -3.11-64 -m venv %foldername%
call %foldername%\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
)
pause