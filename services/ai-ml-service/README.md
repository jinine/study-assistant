Run Commands 

```deactivate
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app/main.py
flask run
```