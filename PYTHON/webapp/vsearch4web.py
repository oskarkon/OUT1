#próba do git
from flask import Flask, render_template, request
from PYTHON.modul.vsearch import search4letters
from PYTHON.webapp.DBcm import UseDatabase

app = Flask(__name__)
app.config['dbconfig'] = {'host': '127.0.0.1',
             'user': 'vsearch',
             'password': 'vsearchpasswd',
             'database': 'vsearchlogdb',
             'auth_plugin': 'mysql_native_password'}

def log_request(req: 'flask_request', res: str) -> None:

    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
            (phrase,letters,ip,browser_string,results)
            values
            (%s, %s, %s, %s, %s)"""

        cursor.execute(_SQL,(req.form['phrase'],
                            req.form['letters'],
                            req.remote_addr,
                            req.user_agent.browser,
                            res,))


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Oto twoje wyniki'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
        the_phrase =phrase,
        the_letters =letters,
        the_title =title,
        the_results =results,)

@app.route('/')
@app.route('/entry')
def entry_page() ->'html':
    return render_template('entry.html', the_title = "Witaj "
                                                     "na stronie internetowej search4letters!")


@app.route('/viewlog')
def view_the_log() -> 'html':
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL= """select phrase, letters, ip, browser_string, results from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        titles =('Dane z formularzea', 'Adres klienta', 'Agent uzytkownika', 'Wyniki')
        return render_template('viewlog.html', the_title = 'Widok_logu',
                           the_row =titles, the_data=contents,)

if __name__ == '__main__':
    app.run(debug=True)
