from flask import Flask, request, render_template
from funkcije import get_vse_valute, get_casovna_obdobja, get_tecaji, pretvorba, get_tecaji_vsi, spremeni_letnico_datuma
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
        ime_valute1 = request.form.get('valuta1') #iz forme preberemo prvo valuto
        ime_valute2 = request.form.get('valuta2')
        leto = request.form.get('leto') #iz forme preberemo leto

        obdobje = ['2009-03-03', '2009-03-04', '2009-03-05']
        novo_obdobje = spremeni_letnico_datuma(leto, obdobje) #spremeni obdobje na leto pridobljeno iz forme
        print(novo_obdobje)
        # za primer bomo prikazali obdobje od '2009-03-03'-'2009-03-05'
        x1 = get_tecaji_vsi(leto, ime_valute1) #dobimo slovar vseh tecajev, za doloceno leto za doloceno valuto pridobljeno iz forme
        x2 = get_tecaji_vsi(leto, ime_valute2)

        return render_template('valuta.html', ime_valute1=ime_valute1, ime_valute2=ime_valute2, leto=leto,
                               novo_obdobje=novo_obdobje,
                               x1=x1, x2=x2)




if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)