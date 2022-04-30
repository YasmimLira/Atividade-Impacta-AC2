from ast import Str
import re
from flask import Flask,jsonify,abort, render_template
from flask import make_response, request, url_for
from flaskext.mysql import MySQL


app = Flask(__name__)
#app.url_map.strict_slashes = False


mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pass02345'
app.config['MYSQL_DATABASE_DB'] = 'ac2'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')


@app.route('/cadastrar', methods=["GET","POST"])
def cadastrar():
    _name = request.form['nome_aluno']
    _email = request.form['email_aluno']
    _endereco = request.form['endereco_aluno']
    if _name and _email and _endereco:
        conn = mysql.connect()
        cursor = conn.cursor()

        sql = "INSERT INTO tb_users(nome_aluno, email_aluno, endereco_aluno) VALUES (%s, %s, %s)"
        value = (_name, _email, _endereco)
        cursor.execute(sql, value)
        conn.commit()

    
 
    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True, host='localhost', port=5000)