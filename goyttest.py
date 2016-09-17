import json
import sqlite3

conn=sqlite3.connect('goytdb.sqlite')
cur=conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Test;

CREATE TABLE Test (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    assignee TEXT UNIQUE,
    due_date DATE,
    status TEXT
)

'''
)
fname = raw_input("Enter File name:")
if(len(fname)<1): fname='goyt.json'

str_read=open(fname).read()
json_data=json.loads(str_read)

for entry in json_data:
    name=entry[0];
    assignee=entry[1];
    due_date=entry[2];
    status=entry[3];

    print name,status

    cur.execute(''' INSERT OR IGNORE INTO Test(name, assignee, due_date, status)
    VALUES(?, ?, ?, ?)''', (name, assignee, due_date, status))
    cur.execute('SELECT id,assignee,due_date FROM Test WHERE name = ? ', (name,))
    user_id = cur.fetchone()

    conn.commit()
print user_id


