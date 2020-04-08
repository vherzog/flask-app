from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DontTellAnyone'

class EnterGameForm(FlaskForm):
  username = StringField('Username', validators=[InputRequired()])
  # password = PasswordField('Password', validators=[DataRequired()])
  game_code = StringField('Game Code', validators=[InputRequired()])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Join the game!')

@app.route('/join', methods=['GET', 'POST'])
def joinAGame():
  form = EnterGameForm()
  if form.validate_on_submit():
      return "Entered game!"
  return render_template('FormEnterGame.html', title='Join A Game', form=form)

if __name__ == '__main__':
  app.run(debug=True)
