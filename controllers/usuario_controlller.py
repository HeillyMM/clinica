from flask import Blueprint, redirect, url_for, request, session
from models.usuario_model import Usuario
from views import usuario_view

usuario_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

@usuario_bp.route("/", methods=['GET', 'POST'])
def login():
    if 'usuario_id' in session:
        return usuario_view.home()

    if request.method == 'GET':
        return usuario_view.login()
        
    username = request.form['username']
    password = request.form['password'] 
    
    usuario_autenticado = Usuario.login(username, password)
    
    if usuario_autenticado:
        session['usuario_id'] = usuario_autenticado.id_usuario
        session['username'] = usuario_autenticado.username
        session['rol'] = usuario_autenticado.rol
        return usuario_view.home()
    
    return usuario_view.login()

@usuario_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('usuarios.login'))
