from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf import FlaskForm

# creamos los formularios de Registro y de Publicación
class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')

#class PostForm(FlaskForm):
    #title = StringField('Título', validators=[DataRequired(), Length(max=128)])
    #title_slug = StringField('Título slug', validators=[Length(max=128)])
    #content = TextAreaField('Contenido')
    #submit = SubmitField('Enviar')
class CartaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción', validators=[DataRequired()])
    precio = StringField('Precio', validators=[DataRequired()])
    submit = SubmitField('Agregar plato')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

class ComentarioForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    correo = StringField('Correo', validators=[DataRequired(), Email()])
    comentario = StringField('Comentario', validators=[DataRequired()])
    submit = SubmitField('Crear Comentario')