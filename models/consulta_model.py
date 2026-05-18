# Aunque conceptualmente Médicos y Pacientes tienen una relación Muchos a Muchos (N:M),
# NO se utiliza una tabla intermedia oculta (propiedad 'secondary="consultas"').
#
# La entidad 'Consulta' no es un simple puente de IDs; contiene atributos críticos
# del negocio (fecha, diagnóstico, tratamiento). En SQLAlchemy, usar 'secondary' 
# oculta la tabla intermedia e impide manipular estos campos extra de forma nativa.

from database import db

class Consulta(db.Model):
    __tablename__ = "consultas"
    
    id_consulta = db.Column(db.Integer,primary_key=True)
    fecha = db.Column(db.Date,nullable=False)
    diagnostico = db.Column(db.String(200),nullable=False)
    tratamiento = db.Column(db.String(200),nullable=False)
    id_medico = db.Column(db.Integer,db.ForeignKey('medicos.id_medico'))
    id_paciente = db.Column(db.Integer,db.ForeignKey('pacientes.id_paciente'))

    medico = db.relationship('Medico',back_populates ="consultas")
    paciente = db.relationship('Paciente',back_populates ="consultas")