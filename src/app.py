from flask import Flask, render_template, request, redirect, url_for
import os
import database as cn

templates_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
templates_dir = os.path.join(templates_dir, 'src', 'templates')

app = Flask(__name__, template_folder = templates_dir)

#Rutas de la app
@app.route('/')
def home():
    cursor = cn.database.cursor()
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall()
    #Listar datos
    insertObject = []
    columnName = [column [0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnName, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)

#Guardar Usuarios en DataBase
@app.route('/user', methods=['POST'])
def addUser():
    username = request.form['username']
    nombre = request.form['nombre']
    password =request.form['pass']
    if username and nombre and password: 
        cursor = cn.database.cursor()
        sql = "INSERT INTO users (username, nombre, pass) VALUES (%s, %s,%s)"
        data = (username,nombre,password)
        cursor.execute(sql, data)
        cn.database.commit()
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)