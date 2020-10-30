export PYTHONIOENCODING=utf-8
nohup sudo python3 serve.py --crt 'ssl/fullchain.pem' --pem 'ssl/privkey.pem' &> nohup_https.out
nohup sudo python3 serve.py --port 80 &> nohup_http.out
