#Importar Librerias Instaladas
#pip install flask
#pip install flask-sqlalchemy   -----Para Conectar a una BD SQL
#pip install flask-marshmallow  -----Definir Esquema con la BD
#pip install marshmallow-sqlalchemy
#pip install pymysql            ------Para Conectar a MySQL Driver MySQL
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#Instancia de FLASK mi aplicacion
app = Flask(__name__)
#Dando la configuracion a app Cadena de Conexion
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/bdpythonapi'
#Configuracion por defecto para no alertar o warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#SQL alchemy pasar la configuracion
db = SQLAlchemy(app)
#Instanciar Marshmellow utiliza la instacion de app (Marshemellow sirve para esquema)
ma = Marshmallow(app)

#Creacion de Tabla Categoria
#Datos de mi tabla, definir sus propiedades los mismos que la de BD
class Categoria(db.Model):
    cat_id = db.Column(db.Integer,primary_key=True)
    cat_nom = db.Column(db.String(100))
    cat_desp = db.Column(db.String(100))

    #Constructor cada vez que se instancia la clase
    #Al recibir asignar los datos
    def __init_(self,cat_nom,cat_desp):
        self.cat_nom = cat_nom
        self.cat_desp = cat_desp
    #Modelo de Datos completado

#Crea las tablas
with app.app_context():
    db.create_all()


# Esquema Categoria
class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('cat_id','cat_nom','cat_desp')

# Una sola respuesta
categoria_schema = CategoriaSchema()
# Cuando sena muchas resouestasd
categoria_schema = CategoriaSchema(many=True)

# Get##########################################################
@app.route('/categoria',methods=['GET'])
def get_categoria():
    all_categoria = Categoria.query.all()
    result = categoria_schema.dump(all_categoria)
    return jsonify(result)

# Mensaje de bienvenida
@app.route('/',methods=['GET'])
def index():
    return jsonify({'Mensaje':'Bienvenido remy'})

if __name__=="__main__":
    app.run(debug=True)
    
