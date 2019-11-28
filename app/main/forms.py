from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required, DataRequired


class NameForm(FlaskForm):
    name = StringField('input base64', validators=[DataRequired()])
    submit = SubmitField('Submit')
