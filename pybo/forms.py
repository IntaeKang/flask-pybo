from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class UserCreateForm(FlaskForm):
    username = StringField('이름', validators=[DataRequired('이름을 입력해주세요.'), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired('비밀번호를 입력해주세요.'),
                                                  EqualTo('password2', '비밀번호가 다릅니다.')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired('비밀번호를 확인해주세요.')])
    email = EmailField('e메일', validators=[DataRequired('e메일 주소를 입력해주세요.'), Email()])


class UserLoginForm(FlaskForm):
    username = StringField('이름', validators=[DataRequired('이름을 입력해주세요.'), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired('비밀번호를 입력해주세요.')])


class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목을 입력해주세요.')])
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력해주세요.')])


class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력해주세요.')])


class CommentForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력해주세요.')])
