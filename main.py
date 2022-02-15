from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route("/emails/create/")
def emails_create():
    name = request.args['name']
    email = request.args['email']

    con = sqlite3.connect('example.db')
    cur = con.cursor()

    sql = f'''
    INSERT INTO emails (name, email) 
    VALUES ('{name}', '{email}');
    '''

    cur.execute(sql)
    con.commit()
    con.close()
    return 'OK'


@app.route("/emails/read/")
def emails_read():
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    sql = '''SELECT * FROM emails;'''

    cur.execute(sql)
    results = cur.fetchall()
    con.close()
    return str(results)


@app.route("/emails/update/")
def emails_update():
    id_ = request.args['id']
    name = request.args['name']

    con = sqlite3.connect('example.db')
    cur = con.cursor()

    sql = f'''
        UPDATE emails 
        SET name='{name}'
        WHERE id={id_};
        '''

    cur.execute(sql)
    con.commit()
    con.close()
    return 'OK'


@app.route("/emails/delete/")
def emails_delete():
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    sql = '''DELETE FROM emails;'''

    cur.execute(sql)
    con.commit()
    con.close()
    return 'OK'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

