from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,RadioField
from wtforms.validators import DataRequired

class indexForm(FlaskForm):
    seed = StringField('seed', validators=[DataRequired()])
    direction =  RadioField('direction', choices=[('fromHtoU','fromHtoU'),('fromUtoH','fromUtoH')])
    recepient = StringField('recepient', validators=[DataRequired()])
    amount = StringField('amount', validators=[DataRequired()])
    assetId =StringField('assetId', validators=[DataRequired()])
    submit = SubmitField('Sent')