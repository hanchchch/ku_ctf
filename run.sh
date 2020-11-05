
sudo nginx -s quit 2> /dev/null
pid=$(sudo netstat -tnlp | grep ":31443 " | awk '{print $7}' | cut -f 1 -d '/')
while [ ${pid} ]; do
sudo kill -9 $pid 2> /dev/null
pid=$(sudo netstat -tnlp | grep ":31443 " | awk '{print $7}' | cut -f 1 -d '/')
done

pid=$(sudo netstat -tnlp | grep ":80 " | awk '{print $7}' | cut -f 1 -d '/')
while [ ${pid} ]; do
sudo kill -9 $pid 2> /dev/null
pid=$(sudo netstat -tnlp | grep ":80 " | awk '{print $7}' | cut -f 1 -d '/')
done

sudo nginx -c /home/hanch/ku_ctf/conf/nginx/http.conf 
nohup sudo python3 serve.py --crt ssl/fullchain.pem --pem ssl/privkey.pem --port 443 &