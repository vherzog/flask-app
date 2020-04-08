from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, InputRequired

class EnterGameForm(FlaskForm):
  username = StringField('Username', validators=[InputRequired()])
  # password = PasswordField('Password', validators=[DataRequired()])
  game_code = StringField('Game Code', validators=[InputRequired()])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Join the game!')
