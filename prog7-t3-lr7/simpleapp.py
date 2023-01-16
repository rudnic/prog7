from flask import Flask
import os
import socket

app = Flask(__name__)

counter = 0

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
    global counter
    counter += 1

    return f"""
        <h1>Counter = {counter}</h1>
    """
    

@app.route('/about')
def about():
    html = hello() + "<h1>Rudnitskii Nikita</h1>"
    return  html

#localhost:port/stat - инкремент и возвращает текущее значение счетчика

# localhost:port/about псевдоним для того, что возвращает def hello()

# Значение счетчика хранится в переменной и не сохраняется между сеансами работы приложения.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    # app.run(host='127.0.0.1', port=80)
