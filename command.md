pip3 install virtualenv
python3 -m venv .venv
pip3 freeze > requirements.txt
pip3 install -r requirements.txt
source .venv/bin/activate

pip install pygame
