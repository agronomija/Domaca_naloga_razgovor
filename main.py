from flask import Flask, request, render_template
from funkcije import get_vse_valute, get_casovna_obdobja, get_tecaji, pretvorba
import requests

app = Flask(__name__)


@app.route("/")
def index():
    vse_valute = get_vse_valute()
    letnice = get_casovna_obdobja()
    return render_template('izberi_valuto.html', vse_valute=vse_valute, letnice=letnice)



@app.route("/valuta", methods=['POST'])
def valuta():
    if request.method == 'POST':
        ime_valute1 = request.form.get('valuta1')
        ime_valute2 = request.form.get('valuta2')
        leto = request.form.get('leto')


        return render_template('valuta.html', ime_valute1=ime_valute1, ime_valute2=ime_valute2, leto=leto)




if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)