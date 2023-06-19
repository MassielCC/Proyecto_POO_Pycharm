from flask import Flask, render_template, request, redirect, url_for
from forms import SignupForm, PostForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
# app.config['SECRET_KEY'] = 'pass'

HaIniciado_sesion = False
esAdmin = False
@app.route("/")
def index():
    return render_template("index.html", posts=publicaciones, inicioSesion=HaIniciado_sesion, admin=esAdmin)

@app.route('/carta')
def carta():
    return render_template('/admin/carta.html')

usuarios=[]
@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    # creamos el objeto form de la clase SignupForm() que está en forms.py
    form = SignupForm()
    # verificamos cuando el usuario haga click en submit (botón Registrar)
    if form.validate_on_submit():
        # si ha pasado la validación, creamos las siguientes variables
        # y obtenemos sus datos:
        name = form.name.data
        email = form.email.data
        password = form.password.data
        user = {'nombre': name, 'usuario':email, 'clave': password}
        usuarios.append(user)
        try:
            with open("usuarios1.txt", "a+") as archivo1:
                archivo1.write(f"{user}")
        finally:
            archivo1.close()
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        # redigire a la página principal!
        return redirect(url_for('index'))
    # caso contrario, redirige a signup_form con el contenido de form.
    return render_template("/admin/signup_form.html", form=form, inicioSesion=HaIniciado_sesion, admin=esAdmin)

# publicaciones es una lista vacía
publicaciones = []
@app.route("/admin/post/", methods=['GET', 'POST'], defaults={'post_id': None})
@app.route("/admin/post/<int:post_id>/", methods=['GET', 'POST'])
def post_form(post_id):
    # form es un objeto de la clase PostForm
    form = PostForm()
    # si yo hago click en Enviar, y la validación ha sido correcta:
    if form.validate_on_submit():
        title = form.title.data
        title_slug = form.title_slug.data
        content = form.content.data
        # post es un diccionario con title, title_slug y content
        post = {'title': title, 'title_sub2': title_slug, 'content': content}
        # agregar el post creado en la lista 'publicaciones'
        publicaciones.append(post)
        try:
            with open("publicaciones.txt", "a+") as archivo1:
                archivo1.write(f"{post}")
        finally:
            archivo1.close()
        return redirect(url_for('index'))
    return render_template("/admin/post_form.html", form=form, inicioSesion=HaIniciado_sesion, admin=esAdmin)

@app.route("/admin/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == 'POST':
        # tomamos los valores ingresados por teclado en el formulario
        email = form.email.data
        password = form.password.data
        print('email ingresado: ' +email)
        print('contraseña ingresada: ' +password)
        # recoro la lista usuarios
        for elemento in usuarios:
            print(elemento)
            # evaluo el valor de 'usuario' y contraseña en el diccionario vs el ingresado en el formulario
            if elemento['usuario'] == email and elemento['clave'].strip() == password:
                # si cumple imprimimos en pantalla: inicio de sesión correcto!
                print('Inicio de sesión correcto!')
                global HaIniciado_sesion # modifico el valor de la linea 10
                HaIniciado_sesion = True # lo modifico por Verdadero
                if email == "marelly.colla@upch.pe" or email == "sebastian.saldana@upch.pe":
                    print("Es administrador")
                    global esAdmin
                    esAdmin = True
            else:
                print("Error")
        return render_template("index.html", posts=publicaciones, inicioSesion= HaIniciado_sesion, admin=esAdmin)
    return render_template("/admin/login.html", form=form)

@app.route("/signout")
def cerrar_sesion():
    global HaIniciado_sesion # indicamos que vamos a modificar el valor de la linea 10
    HaIniciado_sesion = False # modificamos el valor de HaIniciado_sesion a False
    global esAdmin
    esAdmin = False
    # retornamos la página web index.html con HaIniciado_sesion en False
    return render_template('index.html', posts=publicaciones, inicioSesion = HaIniciado_sesion, admin=esAdmin)

if __name__ == '__main__':
    try:
        # lectura del archivo usuarios.txt
        with open("usuarios.txt", "r") as archivo2:
            # en usuarios_ guardamos el contenido de usuarios.txt como una lista de str
            usuarios_ = archivo2.readlines()
    finally:
        archivo2.close()
        for u_ in usuarios_:
            # divido en una lista el contenido de cada linea
            info = u_.split(',')
            elemento = {}  # creo el diccionario elemento
            elemento['usuario'] = info[1]  # el key 'usuario' toma el valor del correo
            elemento['clave'] = info[2]  # el key 'clave' guarda la contraseña
            usuarios.append(elemento)

    app.run(debug=True)
