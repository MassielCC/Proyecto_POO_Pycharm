from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf import FlaskForm

# creamos los formularios de Registro y de Publicación
class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')

    @classmethod
    def crear_archivo(cls, usuario):
        try:
            with open(usuario+".txt", "x") as archivo1:
                print("Se ha creado el archivo correctamente")
        finally:
            archivo1.close()

class CartaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción', validators=[DataRequired()])
    precio = StringField('Precio', validators=[DataRequired()])
    es_favorito = BooleanField(default=False)
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

class Favoritos(CartaForm):
    def __init__(self, user):
        self._usuario = user #Platos favoritos son por usuario
        self.listaFav = []
        super().__init__()

    def getlistaFavorito(self, _usuario):
        try:
            with open(str(_usuario) + ".txt", "r") as archivo2:
                listaFav = archivo2.readlines()
        finally:
            archivo2.close()

        for elemento in listaFav:
            self.listaFav.append(elemento)

        print("Lista favorito:", listaFav)
    def getUser(self):
        return self._usuario
    def agregarFav(self, plato, _usuario):
        try:
            with open(str(_usuario) + ".txt", "a+") as archivoF:
                archivoF.write(f"{plato}"+ "\n")
        finally:
            archivoF.close()
        self.listaFav.append(plato)