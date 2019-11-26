from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, DataRequired


class NameForm(Form):
    name = StringField('input base64', validators=[DataRequired()])
    submit = SubmitField('Submit')
