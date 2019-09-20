from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, logout_user, current_user, login_user, login_required

from forms import LoginForm
from models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rlw2s0SskHEi3U&JY9K4bZ2O!FfKRVNT'

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == user_id:
            return user
    return None

users = [User('dvelasquez@vicomtech.org','123')]

def get_user(email):
    for user in users:
        if user.email == email:
            return user
    return None

@app.route('/')
@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        # email = form.email.data
        # print(email)
        # password = form.password.data
        # print(password)
        # logged_usr = User(form.email.data, form.password.data)
        user = get_user(form.email.data)
        print(f'Trying to log in user: {form.email.data} and password: {form.password.data}')
        if user and form.password.data == user.password:
            print(f'User exists, logging in {form.email.data}')
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
            return redirect(url_for('home'))
        else:
            print('User does not exists')
            return redirect(url_for('login'))
    return render_template('login.html', form = form)

@app.route('/protected')
@login_required
def protected():
    return render_template('protected.html')
    
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__":
    print('Hola mundo')
    app.run(debug=True)