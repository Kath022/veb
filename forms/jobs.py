from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, BooleanField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    title = TextAreaField('Title of activity', validators=[DataRequired()])
    team_leader_id = IntegerField("Team leader id", validators=[DataRequired()])
    duration = IntegerField('Duration', validators=[DataRequired()])
    list_of_collaboration = StringField('List of collaboration')
    is_finished = BooleanField('Is finished')
    submit = SubmitField('Submit')