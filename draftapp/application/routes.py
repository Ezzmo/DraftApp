from application import app, db, bcrypt
from flask import render_template, redirect, url_for, request
from application.forms import ChooseForm, RegistrationForm, LoginForm, UpdateTeamForm
from application.models import Userteams, Users, Players
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
@app.route('/board')
def home():
	teamData = Userteams.query.all()
	return render_template('home.html', title='Board', teams=teamData)

@app.route('/about')
def about():
    return render_template('about.html', title='about')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = Users.query.filter_by(name=form.name.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect('board')
	return render_template('login.html', title='Login', form=form)

@app.route('/make', methods=['GET', 'POST'])
def make():
	form = ChooseForm()
	form.player1.choices = [(player.name, player.name) for player in Players.query.all()]
	form.player2.choices = [(player.name, player.name) for player in Players.query.all()]
	form.player3.choices = [(player.name, player.name) for player in Players.query.all()]
	form.player4.choices = [(player.name, player.name) for player in Players.query.all()]
	form.player5.choices = [(player.name, player.name) for player in Players.query.all()]
	if form.validate_on_submit():
		teamData = Userteams(
			teamname = form.name.data,
			player1 = form.player1.data,
			player2 = form.player2.data,
			player3 = form.player3.data,
			player4 = form.player4.data,
			player5 = form.player5.data,
			user_id = current_user.id
		)
		db.session.add(teamData)
		db.session.commit()
		return redirect(url_for('home'))

	else:
		print(form.errors)
	return render_template('post.html', title='Post', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/edit', methods=['GET', 'POST'])
def edit():
	form = UpdateTeamForm()
	form.player1.choices = [(player.name, player.name) for player in Players.query.all()]
	form.player2.choices = [(player.name, player.name) for player in Players.query.all()]
	form.player3.choices = [(player.name, player.name) for player in Players.query.all()]
	form.player4.choices = [(player.name, player.name) for player in Players.query.all()]
	form.player5.choices = [(player.name, player.name) for player in Players.query.all()]
	latest = db.session.query(Userteams).order_by(Userteams.id.desc()).first()
	if form.validate_on_submit():
		latest.name = form.name.data
		latest.player1 = form.player1.data
		latest.player2 = form.player2.data
		latest.player3 = form.player3.data
		latest.player4 = form.player4.data
		latest.player5 = form.player5.data
		db.session.commit()
		return redirect(url_for('edit'))
	return render_template('edit.html', title='Editor', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		player = Players(
			name=form.name.data,
			age=form.age.data,
			position=form.position.data,
			)

		db.session.add(player)
		db.session.commit()
		return redirect(url_for('register'))

	return render_template('register.html', title='Register', form=form)

@app.route("/board/clear", methods=["GET", "POST"])
@login_required
def board_delete():
	teams = Userteams.query.filter_by(user_id=current_user.id)
	for team in teams:
		db.session.delete(team)
		db.session.commit()
	return redirect(url_for('home'))
