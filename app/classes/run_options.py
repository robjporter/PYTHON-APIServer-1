# Run options
#  gunicorn -w 4 -b 127.0.0.1:5000 main:app
#  waitress main:app
#  python3 main.py runserver
#  uwsgi --http 0.0.0.0:8000 --home env --wsgi-file main.py --callable app --master --enable-threads --thunder-lock
#  virtualenv -p /usr/local/bin/python3 env
#    source env/bin/activate
#    pip3 install --upgrade pip
#    pip3 install -r requirements.txt
