from flask import Flask, render_template

app = Flask(__name__)

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/destek')
def destek():
    return render_template('destek.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/skyrim_modsayfa')
def skyrim_modsayfa():
    return render_template('skyrimmods.html')

@app.route('/fallout_modsayfa')
def fallout_modsayfa():
    return render_template('fallout4mods.html')

@app.route('/bannerlord_modsayfa')
def bannerlord_modsayfa():
    return render_template('bannerlordmods.html')

@app.route('/warband_modsayfa')
def warband_modsayfa():
    return render_template('warbandmods.html')

@app.route('/mod_sayfa_1')
def mod_sayfa_1():
    return render_template('mod_sayfa_1.html')

@app.route('/mod_sayfa_2')
def mod_sayfa_2():
    return render_template('mod_sayfa_2.html')

@app.route('/mod_sayfa_3')
def mod_sayfa_3():
    return render_template('mod_sayfa_3.html')

@app.route('/mod_sayfa_4')
def mod_sayfa_4():
    return render_template('mod_sayfa_4.html')

@app.route('/music')
def music():
    return render_template('music.html')


if __name__ == '__main__':
    app.run(debug=True) 


