from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# SQLite veritabanına bağlanma
conn = sqlite3.connect('nottakip.db')
cur = conn.cursor()

# Tablo oluşturma
cur.execute('''CREATE TABLE IF NOT EXISTS dersler (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               ders_adi TEXT NOT NULL)'''
cur.execute('''CREATE TABLE IF NOT EXISTS notlar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ders_id INTEGER NOT NULL,
                notu INTEGER NOT NULL,
                FOREIGN KEY (ders_id) REFERENCES dersler(id)
            )''')

conn.commit()

@app.route('/')
def login():
    return render_template('login.html')
     
@app.route('/uye_kayit')
def uye_kayit():
    return render_template('uye_kayit.html')

@app.route('/anasayfa')
def ana_sayfa():
    return render_template('ana_sayfa.html')

# Ders tanımlama sayfası
@app.route('/ders_tanimla')
def ders_tanimla():
    return render_template('ders_tanimla.html')

# Not girişi sayfası
@app.route('/not_girisi')
def not_girisi():
    conn = sqlite3.connect('nottakip.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM dersler")
    dersler = cur.fetchall() 
    conn.close()
    return render_template('not_girisi.html',dersler=dersler)

# Not girişi sayfası
@app.route('/not_listesi')
def not_listesi():
    conn = sqlite3.connect('nottakip.db')
    cur = conn.cursor()
    cur.execute("SELECT d.id,d.ders_adi,n.notu FROM dersler d inner join notlar n on (d.id=n.ders_id) order by n.ders_id")
    dersnotlari = cur.fetchall()
    conn.close()
    return render_template('not_listesi.html',dersnotlari=dersnotlari)

# Not girişi sayfası
@app.route('/not_ortalama/<dersid>')
def not_ortalama(dersid):
    conn = sqlite3.connect('nottakip.db')
    cur = conn.cursor()
    cur.execute("SELECT n.notu FROM dersler d inner join notlar n on (d.id=n.ders_id) where n.ders_id=?",(dersid))
    dersnotlari = cur.fetchall()
    conn.close()
    toplam=0
    ortalama=0
    for notu in dersnotlari:
         toplam+=int(notu[0])
    ortalama=toplam/len(dersnotlari)
    
    return render_template('not_ortalama.html',ortalama=ortalama)

@app.route('/not_kaydet', methods=['POST'])
def not_kaydet():
    conn = sqlite3.connect('nottakip.db')
    cur = conn.cursor()
    notu = int(request.form['notu'])
    ders_id = request.form['ders_id']
    cur.execute("INSERT INTO notlar (ders_id,notu) VALUES (?,?)", (ders_id,notu))
    conn.commit()
    conn.close()
    return redirect(url_for('ana_sayfa'))

@app.route('/ders_kaydet',methods=['POST'])
def ders_kaydet():
    conn = sqlite3.connect('nottakip.db')
    cur = conn.cursor()
    ders_adi = request.form['ders_adi']
    cur.execute("INSERT INTO dersler (ders_adi) VALUES (?)", (ders_adi,))
    conn.commit()
    conn.close()
    return redirect(url_for('ana_sayfa'))

if __name__ == '__main__':
    app.run(debug=True)
    git config --global  user.name "nowe090909"
    git config --global user.email  "utkanaydogdu48@gmail.com"