import sqlite3
import json
from contextlib import closing

dbname = 'eijirodb.sqlite3'

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()

    query = [
        'kick back'
    ]
    # TODO: よりセキュアに実装する
    select_sql = 'select data from word where entry=="{}"'.format('" OR entry== "'.join(query))
    

    for row in c.execute(select_sql):
        print(json.loads(row[0]))