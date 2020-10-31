import sqlite3
import json
import os
import shutil
from hashlib import sha256
from init_setting import config as raw_config, pages, teams, users, admin_id, admin_pw

con = sqlite3.connect('./CTFd/ctfd.db')
cur = con.cursor()

def delete(table):
    cur.execute("DELETE FROM "+table+" WHERE 1=1")

def _insert(table, data):
    sql = "INSERT INTO "+table+" VALUES (?"+",?"*(len(data)-1)+")"
    cur.execute(sql, data)

def insert(table, datas):
    if type(datas) == list:
        for data in datas:
            _insert(table, data)
    elif type(datas) == tuple:
        _insert(table, datas)


challs = []
for (cur_dir, dirs, files) in os.walk('supplier'):
    if 'props.json' in files:
        with open(cur_dir+'/props.json') as f:
            props = f.read()
            props = json.loads(props)
            props.update({'chall_dir':cur_dir})
            challs.append(props)




i = 0
config = []
for key in list(raw_config.keys()):
    i += 1
    config.append((i, key, raw_config[key]))
"""
delete("config")
delete("pages")
delete("teams")
delete("users")

insert("config", config)
insert("pages", pages)
insert("teams", teams)
insert("users", users)

print("admin id: "+admin_id)
print("admin pw: "+admin_pw.decode())
"""

print(json.dumps(challs, indent=4, ensure_ascii=False))

challenges = []
dynamic_challenge = []
flags = []
files = []

i = 0
f = 0

for chall in challs:
    i += 1

    challenges.append((i, chall['name'], chall['description'], 0, 
    1000, chall['category'], 
    'dynamic', 'visible', None))

    dynamic_challenge.append((i, 500, 100, 30))

    flags.append((i, i, 'static', chall['flag'],''))

    if len(chall['files']) != 0:
        f += 1
        upload_dir = sha256(chall['name'].encode()).hexdigest()
        for filename in chall['files']:
            files.append((f, 'challenge', upload_dir+'/'+filename, i, None))
            os.mkdir("./CTFd/uploads/"+upload_dir)
            shutil.copy(chall['chall_dir']+'/'+filename, "./CTFd/uploads/"+upload_dir+'/'+filename)

delete("challenges")
delete("dynamic_challenge")
delete("flags")
delete("files")

delete("tracking")
delete("submissions")
delete("solves")

insert("challenges", challenges)
insert("dynamic_challenge", dynamic_challenge)
insert("flags", flags)
insert("files", files)

con.commit()
con.close()