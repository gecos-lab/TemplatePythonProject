foldername=venv
if [ -d "$foldername" ]; then 
    ./$foldername/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade -r requirements.txt 
else
    python3 -m venv $foldername
    ./$foldername/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
fi