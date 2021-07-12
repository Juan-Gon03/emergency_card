from flask import Flask, render_template, url_for, request, redirect
import sqlite3

app = Flask(__name__)

# cur.execute('''CREATE TABLE card_values
#              (from_name text, to_name text, message text, holiday text, id integer)''')

@app.route('/')
def info():
    return render_template('info.html')

@app.route('/emergency_card_form/')
def form():
    return render_template('form.html')

@app.route('/form_input/', methods=['POST', 'GET'])
def build():
    con = sqlite3.connect('database/cards.db')
    cur = con.cursor()

    fromName =request.form['formName']
    toName = request.form['toName']
    message = request.form['message']
    holiday = request.form['holiday']

    data =(fromName, toName, message, holiday)
    cur.execute(f"INSERT INTO {holiday} (from_name,to_name,message,holiday) VALUES(?,?,?,?)", data)
    con.commit()

    global lastid
    lastid = str(cur.lastrowid)
    
    cur.execute(f'SELECT id,from_name,to_name,message,holiday FROM {holiday} WHERE id={lastid}')
    con.commit()
    data = cur.fetchall()
    con.close()
    return redirect(f'/{data[0][4]}/{lastid}')
    

@app.route('/Birthday/<id>')
def Birthday(id):
    con = sqlite3.connect('database/cards.db')
    cur = con.cursor()
    cur.execute(f'SELECT id,from_name,to_name,message,holiday FROM Birthday WHERE id={id}')
    con.commit()
    data = cur.fetchall()
    con.close()
    return render_template(f'{data[0][4]}.html', output_data=data)

@app.route('/Chrismas/<id>')
def Chrismas(id):
    con = sqlite3.connect('database/cards.db')
    cur = con.cursor()
    cur.execute(f'SELECT id,from_name,to_name,message,holiday FROM Chrismas WHERE id={id}')
    con.commit()
    data = cur.fetchall()
    con.close()
    return render_template(f'{data[0][4]}.html', output_data=data)


@app.route('/Halloween/<id>')
def Halloween(id):
    con = sqlite3.connect('database/cards.db')
    cur = con.cursor()
    cur.execute(
        f'SELECT id,from_name,to_name,message,holiday FROM Halloween WHERE id={id}')
    con.commit()
    data = cur.fetchall()
    con.close()
    return render_template(f'{data[0][4]}.html', output_data=data)

@app.route('/New_Years/<id>')
def New_Years(id):
    con = sqlite3.connect('database/cards.db')
    cur = con.cursor()
    cur.execute(f'SELECT id,from_name,to_name,message,holiday FROM New_Years WHERE id={id}')
    con.commit()
    data = cur.fetchall()
    con.close()
    return render_template(f'{data[0][4]}.html', output_data=data)

if __name__ == "__main__":
    app.run(debug=True)
