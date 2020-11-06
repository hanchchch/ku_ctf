import sqlite3
import json
import os
import shutil
from hashlib import sha256
from setting_init import config as raw_config, pages, teams, users, admin_id, admin_pw, notifications

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

def init_users():
    delete("pages")
    delete("teams")
    delete("users")

    insert("pages", pages)
    insert("teams", teams)
    insert("users", users)

    print("admin id: "+admin_id)
    print("admin pw: "+admin_pw.decode())

def init_config():
    i = 0
    config = []
    for key in list(raw_config.keys()):
        i += 1
        config.append((i, key, raw_config[key]))

    delete("config")
    insert("config", config)

def init_challs():
    challs = []
    for (cur_dir, dirs, files) in os.walk('supplier'):
        if 'props.json' in files:
            with open(cur_dir+'/props.json') as f:
                props = f.read()
                props = json.loads(props)
                props.update({'chall_dir':cur_dir})
                challs.append(props)
    
    challenges = []
    dynamic_challenge = []
    flags = []
    files = []

    i = 0
    f = 0
    for chall in challs:
        i += 1

        challenges.append((i, chall['name'], chall['description'], 0, 
        500, chall['category'], 
        'dynamic', 'visible', None))

        dynamic_challenge.append((i, 500, 100, 30))

        flags.append((i, i, 'static', chall['flag'],''))

        if len(chall['files']) != 0:
            upload_dir = sha256(chall['name'].encode()).hexdigest()
            for filename in chall['files']:
                f += 1
                files.append((f, 'challenge', upload_dir+'/'+filename, i, None))
                try:
                    os.mkdir("./CTFd/uploads/"+upload_dir)
                except:
                    pass
                shutil.copy(chall['chall_dir']+'/'+filename, "./CTFd/uploads/"+upload_dir+'/'+filename)

    i += 1
    challenges.append((i, 'Sanity check', 'Welcome!!!', 0, 
        10, 'MISC', 
        'dynamic', 'visible', None))
    dynamic_challenge.append((i, 10, 10, 10))
    flags.append((i, i, 'static', 'KOREA{zzz}',''))

    delete("challenges")
    delete("dynamic_challenge")
    delete("flags")
    delete("files")

    insert("challenges", challenges)
    insert("dynamic_challenge", dynamic_challenge)
    insert("flags", flags)
    insert("files", files)

def init_submissions():
    delete("tracking")
    delete("submissions")
    delete("solves")

def init_notifications():
    delete("notifications")
    insert("notifications", notifications)


#init_users()
#init_submissions()
#init_config()
#init_notifications()
init_challs()

con.commit()
con.close()