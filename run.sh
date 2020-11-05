port_nginx=31443
port_python=31442

sudo nginx -s quit 2> /dev/null
pid=$(sudo netstat -tnlp | grep ":${port_nginx} " | awk '{print $7}' | cut -f 1 -d '/')
while [ ${pid} ]; do
sudo kill -9 ${pid} 2> /dev/null
pid=$(sudo netstat -tnlp | grep ":${port_nginx} " | awk '{print $7}' | cut -f 1 -d '/')
done

pid=$(sudo netstat -tnlp | grep ":${port_python} " | awk '{print $7}' | cut -f 1 -d '/')
while [ ${pid} ]; do
sudo kill -9 ${pid} 2> /dev/null
pid=$(sudo netstat -tnlp | grep ":${port_python} " | awk '{print $7}' | cut -f 1 -d '/')
done

sudo nginx -c /home/hanch/ku_ctf/conf/nginx/http.conf 
nohup sudo python3 serve.py --crt ssl/fullchain.pem --pem ssl/privkey.pem --port ${port_python} &