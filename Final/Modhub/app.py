from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['SECRET_KEY'] = 'gelistirme_anahtari'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class SupportTicket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False) 
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='open') 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('E-posta veya şifre hatalı!', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if User.query.filter_by(email=email).first():
            flash('Bu e-posta zaten kayıtlı!', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        name = request.form.get('name')
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Kayıt başarılı! Giriş yapabilirsiniz.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        subject = request.form['subject']
        message = request.form['message']
        user_id = current_user.id

       
        ticket = SupportTicket(subject=subject, message=message, user_id=user_id)
        db.session.add(ticket)
        db.session.commit()

        flash('Destek talebiniz başarıyla gönderildi!', 'success')
        return redirect(url_for('dashboard'))

    support_tickets = SupportTicket.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', support_tickets=support_tickets)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/destek', methods=['GET', 'POST'])
@login_required
def destek():
    if request.method == 'POST':
        subject = request.form['subject']
        message = request.form['message']
        user_id = current_user.id  

       
        ticket = SupportTicket(subject=subject, message=message, user_id=user_id)
        db.session.add(ticket)
        db.session.commit()

        flash('Destek biletiniz başarıyla gönderildi!', 'success')
        return redirect(url_for('destek')) 

    return render_template('destek.html')

@app.route('/delete_ticket/<int:ticket_id>', methods=['POST'])
@login_required
def delete_ticket(ticket_id):
    ticket = SupportTicket.query.get_or_404(ticket_id)

    # Kullanıcı bu ticket'ı oluşturmuşsa silebilir
    if ticket.user_id == current_user.id:
        db.session.delete(ticket)
        db.session.commit()
        flash('Destek biletiniz başarıyla silindi!', 'success')
    else:
        flash('Bu bilet size ait değil!', 'danger')

    return redirect(url_for('dashboard'))

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

@app.route('/mod_sayfa_5')
def mod_sayfa_5():
    return render_template('mod_sayfa_5.html')  # Yeni mod sayfası

@app.route('/mod_sayfa_6')
def mod_sayfa_6():
    return render_template('mod_sayfa_6.html')  # Yeni mod sayfası

@app.route('/mod_sayfa_7')
def mod_sayfa_7():
    return render_template('mod_sayfa_7.html')  # Yeni mod sayfası

@app.route('/mod_sayfa_8')
def mod_sayfa_8():
    return render_template('mod_sayfa_8.html')  # Yeni mod sayfası

#if __name__ == '__main__':
#    with app.app_context():
 #       db.create_all()  # Database tablolarını oluştur
  #  app.run(debug=True)

import os
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
