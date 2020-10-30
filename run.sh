export PYTHONIOENCODING=utf-8
nohup sudo python3 serve.py --crt 'ssl/fullchain.pem' --pem 'ssl/privkey.pem' &
