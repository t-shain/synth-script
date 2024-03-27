Steps to start flask:


1: Type "hostname -I" to get your IP address, use the one that starts with "10.xxx..."

2: Type "http://10.xxx.xxx.xxx.xxx:5000" into browser

3: Copy paste this into the finalproj directory to start FLASK website stuff:

export FLASK_APP=app.py \
flask run --host=0.0.0.0


