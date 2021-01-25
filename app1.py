#Co do backendu, zaprojektuj prostą aplikację z Flask. 
#W sumie musisz zdefiniować trzy funkcje adnotowane @app.route – dwie, 
#które wyświetlą strony i trzecią przeznaczoną dla zapisywania danych z formularza. 
#Oznacz je odpowiednio.

#/mypage/me – informacje o mnie
#/mypage/contact – informacje kontaktowe
#/mypage/contact (POST) – zapis formularza
#Kod, który ma wysyłać informację, niech po prostu zapisze tę wiadomość na konsoli.
from flask import Flask
from flask import request, redirect, render_template

app1=Flask(__name__)

@app1.route('/')

@app1.route('/mypage/me', methods=['GET'])
def about_me():
    return render_template("index.html")

@app1.route('/mypage/contact.html')
def contact_me():
    return render_template("contact.html")

@app1.route('/mypage/contact', methods=['GET','POST'])
def contact_me_form():
    if request.methods=='POST':
        print(request.form)
        return redirect("/mypage/contact")
        