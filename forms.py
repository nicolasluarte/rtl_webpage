from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Length


class log_form(FlaskForm):
    username = StringField('username',
            validators=[DataRequired(),
                Length(min=2, max=20)])

    movement = StringField('movement',
            validators=[DataRequired()])

    weight = DecimalField('weight',
            validators=[DataRequired()])

    repetitions = IntegerField('repetitions',
            validators=[DataRequired()])

    rpe = DecimalField('rpe',
            validators=[DataRequired()])



    submit = SubmitField('Log')
