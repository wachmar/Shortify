from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddUrl(FlaskForm):

    url = StringField('Url to shorten:',
                      validators=[DataRequired()],
                      render_kw={"placeholder": "URL"})
    custom_id = StringField('Custom ID:',
                            render_kw={"placeholder": "ID"})
    submit = SubmitField('Shorten!')
