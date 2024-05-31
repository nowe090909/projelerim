from flask import Flask, render_template,request
from datetime import datetime

app = Flask(__name__)
@app.before_request
def before_request():
    # Tarih bilgisini hesapla
    current_time = datetime.now()

@app.errorhandler(404)
def not_found(e):
  return render_template('404.html'), 404

@app.route('/')
def giris_sayfasi()->'html':
    current_time = datetime.now()
    return render_template('hesapla.html',page_title='Hesaplama sistemimize hoş geldiniz ',current_time=current_time)
 
@app.route('/hakkimizda')
def hakkimizda():
    return render_template('hakkimizda.html')

@app.route('/hizmetlerimiz')
def hizmetlerimiz():
    return render_template('hizmetlerimiz.html')
    
@app.route('/galeri')
def galeri():
    return render_template('galeri.html')

@app.route('/topla',methods=['POST'])
def topla()->'html':
    x=int(request.form['ilkdeger'])
    y=int(request.form['ikincideger'])
    return render_template('sonuc.html',page_title='Hesaplama Sonucu',toplam_sonuc=(x+y),ilk_deger=x,ikinci_deger=y)
 
if __name__ == '__main__':
 app.run(debug=True)


#py -m pip install flask  
#python3 -m http.server