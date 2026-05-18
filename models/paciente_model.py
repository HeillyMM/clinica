from database import db

class Paciente(db.Model):
    __tablename__ = "pacientes"

    id_paciente = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(30),nullable=False)
    edad = db.Column(db.Integer,nullable=False)
    direccion = db.Column(db.String,nullable=False)
    telefono = db.Column(db.String(30),nullable=False)

    consultas = db.relationship('Consulta',back_populates='paciente')


    def __init__(self,nombre,edad,direccion,telefono):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
    
    def guardar(self):
        db.session.add(self)
        db.session.commit()