from wtforms import Form, StringField, PasswordField, SubmitField, SelectField
from wtforms.fields import EmailField, DateField

class Cadastro(Form):
    name = StringField('Nome')
    lastName = StringField('Sobrenome')
    username = StringField('Usuário')
    passwd = PasswordField('Senha')
    email = EmailField('Email')
    gender = SelectField('Sexo', choices=[('masculino', 'Masculino'),
                                          ('feminino', 'Feminino')])
    btnSend = SubmitField('Enviar')
    age = DateField('Nascimento', format='%d/%m/%Y')


class Login(Form):
    username = StringField('Usuário')
    password = PasswordField('Senha')
    btnLogin = SubmitField('Entrar')