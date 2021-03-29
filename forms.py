from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class FilmForm(FlaskForm):
    title = StringField("title",validators=[DataRequired()])
    description = TextAreaField("description",validators=[DataRequired()])

class CommentForm(FlaskForm):
    login = StringField("login",validators=[DataRequired()])
    comment = TextAreaField("comment",validators=[DataRequired()])