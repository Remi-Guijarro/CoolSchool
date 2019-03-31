from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length

class ProbabilityForm(FlaskForm):
    proba = StringField('Probability',validators=[DataRequired(),Length(min=2,max=2)])
    submit = SubmitField('Next')