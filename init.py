import sqlite3

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


i = 0
config = []
for key in list(raw_config.keys()):
    i += 1
    config.append((i, key, raw_config[key]))

delete("config")
delete("pages")
delete("teams")
delete("users")

insert("config", config)
insert("pages", pages)
insert("teams", teams)
insert("users", users)

print("admin id: "+str(admin_id))
print("admin pw: "+str(admin_pw))

challenges = [
    (1, 'test_chall_1', 'description', 0, 
    1000, 'pwn', 
    'dynamic', 'visible', None),
    (2, 'test_chall_2', 'description', 0, 
    1000, 'pwn', 
    'dynamic', 'visible', None),
    (3, 'test_chall_3', 'description', 0, 
    1000, 'web', 
    'dynamic', 'visible', None),
    (4, 'test_chall_4', 'description', 0, 
    1000, 'web', 
    'dynamic', 'visible', None),
]
dynamic_challenge = [
    (1, 1000, 100, 50),
    (2, 1000, 100, 50),
    (3, 1000, 100, 50),
    (4, 1000, 100, 50),
]
flags = [
    (1, 1, 'static', 'KOREA{flag}',''),
    (2, 2, 'static', 'KOREA{flag}',''),
    (3, 3, 'static', 'KOREA{flag}',''),
    (4, 4, 'static', 'KOREA{flag}',''),
]

delete("challenges")
delete("dynamic_challenge")
delete("flags")

insert("challenges", challenges)
insert("dynamic_challenge", dynamic_challenge)
insert("flags", flags)

con.commit()
con.close()