from flask import Flask, render_template
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
    #Convertir los datos a diccionario
    insertObject = []
    columnName = [column [0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnName, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)


if __name__ == '__main__':
    app.run(debug=True, port=4000)