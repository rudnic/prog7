from flask import Flask, request
import os
import socket
import json
import mysql.connector

app = Flask(__name__)


@app.route('/')
def hello():
    """Дополнить возврат в html значение счетчика (счетчик инициализируется в момент запуска приложения"""
    name = os.getenv("NAME", 'world')
    hostname = socket.gethostname()

    html = f"""
    <h1>Hello, {name}!</h1> 
    <b>Hostname:</b> {hostname} <br>
    """
    return html


@app.route('/stat')
def stat():
    """
    Прототип функции, возвращающей значение счетчика
    """

    import datetime

    headers = str(request.headers['User-Agent'])

    html = """
        <b>Datetime</b>: {d} <br>
        <b>Client User-Agent</b>: {req_headers}"""

    return html.format(d=datetime.datetime.now(), req_headers=headers)


@app.route('/initdb')
def db_init():
    mydb = mysql.connector.connect(host="mysqldb",
                                   user="root",
                                   password="p@ssw0rd1")
    cursor = mydb.cursor()

    cursor.execute("DROP DATABASE IF EXISTS inventory")
    cursor.execute("CREATE DATABASE inventory")
    cursor.close()
    mydb.commit()

    mydb = mysql.connector.connect(host="mysqldb",
                                   user="root",
                                   password="p@ssw0rd1",
                                   database="inventory")
    cursor = mydb.cursor()

    cursor.execute("DROP TABLE IF EXISTS widgets")
    cursor.execute("DROP TABLE IF EXISTS logs")
    cursor.execute(
        "CREATE TABLE widgets (name VARCHAR(255), description VARCHAR(255))")
    # CREATE TABLE logs (datetime VARCHAR(255), client_info VARCHAR(255))
    cursor.execute("CREATE TABLE logs (datetime VARCHAR(255), client_info VARCHAR(255))")
    cursor.close()

    mydb.commit()

    return 'init database'


@app.route('/widgets')
def get_widgets():
    mydb = mysql.connector.connect(host="mysqldb",
                                   user="root",
                                   password="p@ssw0rd1",
                                   database="inventory")
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM widgets")

    row_headers = [x[0] for x in cursor.description]

    results = cursor.fetchall()
    json_data = []
    for result in results:
        json_data.append(dict(zip(row_headers, result)))

    cursor.close()

    return json.dumps(json_data)


@app.route('/addlog')
def add_logs():
    """
    Позволяет вводить данные о посещении
    """

    import datetime
    agent = str(request.headers['User-Agent'])
    d = str(datetime.datetime.now())

    mydb = mysql.connector.connect(host="mysqldb",
                                   user="root",
                                   password="p@ssw0rd1",
                                   database="inventory")
    cursor = mydb.cursor()

    sql = "INSERT INTO logs (datetime, client_info) VALUES (%s, %s)"
    vals = (d, agent)

    cursor.execute(sql, vals)
    mydb.commit()

    return (d + " " + agent)



@app.route('/logs')
def get_logs():
    """
    Извлекает данные из таблицы logs
    
    """

    mydb = mysql.connector.connect(host="mysqldb",
                                user="root",
                                password="p@ssw0rd1",
                                database="inventory")

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM logs")

    row_headers = [x[0] for x in cursor.description]

    results = cursor.fetchall()
    json_data = []
    for result in results:
        json_data.append(dict(zip(row_headers, result)))

    cursor.close()

    return json.dumps(json_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
