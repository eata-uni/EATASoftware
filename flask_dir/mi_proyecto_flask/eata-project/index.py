from flask import Flask, render_template, jsonify
from datetime import timedelta
import firebase_admin
from firebase_admin import credentials, db
from firebase_admin import storage
import boto3
from datetime import datetime

app = Flask(__name__)
#cred = credentials.Certificate("key.json")
#firebase_admin.initialize_app(cred, {'databaseURL': 'https://eata-project-default-rtdb.firebaseio.com/',
 #                                    'storageBucket': 'eata-project.appspot.com'})

# Definir las rutas de productos
nombre_bucket = 'eata-smartmachines'

numbertext_product = [
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight'
]
numerotexto_producto = [
    'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho'
]
departments = [
    'Amazonas', 'Ancash', 'Apurímac', 'Arequipa','Ayacucho', 'Cajamarca', 'Cusco', 'Huancavelica', 'Huánuco','Ica','Junín','La_Libertad','Lambayeque','Lima','Lima_Province','Loreto','Madre_de_Dios','Moquegua','Pasco','Piura','Puno','San_Martín','Tacna','Tumbes','Ucayali'
]

title_department = [
    'Amazonas', 'Ancash', 'Apurimac', 'Arequipa','Ayacucho', 'Cajamarca', 'Cusco', 'Huancavelica', 'Huanuco','Ica','Junin','La Libertad','Lambayeque','Lima','Lima Metropolitana','Loreto','Madre de Dios','Moquegua','Pasco','Piura','Puno','San Martin','Tacna','Tumbes','Ucayali'
]

number_product = [
    '1', '2', '3', '4', '5', '6', '7', '8'
]

title_product = [
    'Tasa de precipitaciones ',
  'Temperatura de la superficie terrestre', 
 'Máscara de Cielo despejado', 
  'Agua Precipitable Total ',
   'Altura superior de la nube', 
  'Vientos de movimiento derivado' ,
  'Temperatura superior de las nubes',
  'Fase superior de la nube'
]

products3={'uno':'ACHA','2':'ACHT','3':'ACM','4':'ACTP','5':'GeoColor','6':'LST','7':'RGB','8':'RRQPE'}

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/products')
def products():
    return render_template('products.html')


@app.route('/about')
def about():
    return render_template('nosotros.html')
 
@app.route('/contact')
def contact():
    return render_template('contact.html')

# productos

# Rutas de productos
@app.route('/products/<product_name>')
def product(product_name):
    if product_name in numbertext_product:
        if product_name == 'one':
            return render_template(f'product.html', product_number = number_product[0], numerotexto_producto=numerotexto_producto[0], title_product=title_product[0], numbertext_product=numbertext_product[0])
        elif product_name == 'two':
            return render_template(f'product.html', product_number = number_product[1], numerotexto_producto=numerotexto_producto[1], title_product=title_product[1], numbertext_product=numbertext_product[1])
        elif product_name == 'three':
            return render_template(f'product.html', product_number = number_product[4], numerotexto_producto=numerotexto_producto[4], title_product=title_product[2], numbertext_product=numbertext_product[4])
        elif product_name == 'four':
            return render_template(f'product.html', product_number = number_product[6], numerotexto_producto=numerotexto_producto[6], title_product=title_product[3], numbertext_product=numbertext_product[6])
        elif product_name == 'five':
            return render_template(f'product.html', product_number = number_product[4], numerotexto_producto=numerotexto_producto[4], title_product=title_product[2], numbertext_product=numbertext_product[4])
        elif product_name == 'six':
            return render_template(f'product.html', product_number = number_product[5], numerotexto_producto=numerotexto_producto[5], title_product=title_product[5], numbertext_product=numbertext_product[5])
        elif product_name == 'seven':
            return render_template(f'product.html', product_number = number_product[6], numerotexto_producto=numerotexto_producto[6], title_product=title_product[3], numbertext_product=numbertext_product[6])
        elif product_name == 'eight':
            return render_template(f'product.html', product_number = number_product[7], numerotexto_producto=numerotexto_producto[7], title_product=title_product[7], numbertext_product=numbertext_product[7])

    else:
        return f"El producto {product_name} no está disponible en este momento."

# rutas de  departamenos
@app.route('/products/<int:product_number>/<department_name>')
def product_department(product_number, department_name):
    if department_name in departments:
        if product_number == 1:
            return render_template('product_department.html', product_number=product_number, department_name=department_name, numerotexto_producto=numerotexto_producto[0], title_product=title_product[0], numbertext_product=numbertext_product[0])
        elif product_number == 2:
            return render_template('product_department.html', product_number=product_number, department_name=department_name, numerotexto_producto=numerotexto_producto[1], title_product=title_product[1], numbertext_product=numbertext_product[1])
        elif product_number == 3:
            return render_template('product_department.html', product_number=product_number, department_name=department_name, numerotexto_producto=numerotexto_producto[2], title_product=title_product[2], numbertext_product=numbertext_product[2])
        elif product_number == 4:
            return render_template('product_department.html', product_number=product_number, department_name=department_name, numerotexto_producto=numerotexto_producto[3], title_product=title_product[3], numbertext_product=numbertext_product[3])
        elif product_number == 5:
            return render_template('product_department.html', product_number=product_number, department_name=department_name, numerotexto_producto=numerotexto_producto[4], title_product=title_product[4], numbertext_product=numbertext_product[4])
        elif product_number == 6:
            return render_template('product_department.html', product_number=product_number, department_name=department_name, numerotexto_producto=numerotexto_producto[5], title_product=title_product[5], numbertext_product=numbertext_product[5])
        elif product_number == 7:
            return render_template('product_department.html', product_number=product_number, department_name=department_name, numerotexto_producto=numerotexto_producto[6], title_product=title_product[6], numbertext_product=numbertext_product[6])
        elif product_number == 8:
            return render_template('product_department.html', product_number=product_number, department_name=department_name, numerotexto_producto=numerotexto_producto[7], title_product=title_product[7], numbertext_product=numbertext_product[7])
    else:
        return f"El departamento {department_name} no está disponible en este momento."

# obtener comentarios de los productos





@app.route('/get_producto/<nombre_producto>', methods=['GET'])
def get_producto(nombre_producto):
    products3 = {'uno':'RRQPE','dos':'LST','tres':'ACHA','cuatro':'ACHT','cinco':'ACM','seis':'DMWV','siete':'TPW','ocho':'ACTP'}
    prefix = f'{products3[nombre_producto]}/Peru'
    s3 = boto3.client('s3')
    bucket_name = 'eata-smartmachines'

    # Listar objetos en la carpeta especificada
    objetos = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

    # Buscar un archivo .txt específico y leer su contenido
    response = {
            "fecha": "",
            "texto": ""
        }
    # Buscar un archivo .txt específico y leer su contenido
    for objeto in objetos.get('Contents', []):
        if objeto['Key'].endswith('.txt'):  # Asegurarse de que es un archivo .txt
            # Obtener el objeto
            file = s3.get_object(Bucket=bucket_name, Key=objeto['Key'])
            # Leer el contenido del archivo
            content = file['Body'].read().decode('utf-8')  # Asumiendo que el texto está en UTF-8
            
            # Obtener la fecha y hora de la última modificación del archivo
            last_modified = objeto['LastModified']
            last_modified_adjusted = last_modified - timedelta(hours=5)
            # Formatear la fecha y hora en el formato deseado y almacenar en el diccionario
            response['fecha'] = last_modified_adjusted.strftime("%Y-%m-%d HORA:%H:%M")
            
            # Almacenar el contenido del archivo en la clave 'texto'
            response['texto'] = content
            
            break  # Romper el bucle después de encontrar y leer el primer archivo .txt

    return jsonify({'value': response})

'''def get_images_by_type(image_type):
    bucket = storage.bucket()
    images = bucket.list_blobs(prefix=f'Images/{image_type}')
    image_urls = [image.generate_signed_url(
        version="v4",
        expiration=timedelta(days=7),
        method="GET"
    ) for image in images]

    return jsonify({'image_urls': image_urls[1:]}) if len(image_urls) > 1 else jsonify({'image_urls': []})'''

def get_images_by_type(image_type):
    products3={'1':'RRQPE','2':'LST','3':'ACHA','4':'ACHT','5':'ACM','6':'DMWV','7':'TPW','8':'ACTP'}
    # Configura el cliente de S3
    prefix = f'{products3[image_type]}/Peru'
    #prefix = 'ACHT/Peru'
    s3 = boto3.client('s3')


    # Lista objetos en la carpeta
    objetos = s3.list_objects_v2(Bucket='eata-smartmachines', Prefix=prefix)

    # Obtiene las URLs prefirmadas para cada objeto en la carpeta
    urls_publicas = []
    for objeto in objetos.get('Contents', []):
        objeto_key = objeto['Key']
        # Genera la URL prefirmada
        if objeto_key.lower().endswith('.png'):
            url = s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': 'eata-smartmachines', 'Key': objeto_key},
                ExpiresIn=3600  # Caducidad en segundos (1 hora)
            )
            urls_publicas.append(url)

    return jsonify({'image_urls': urls_publicas[0:]}) if len(urls_publicas) >= 1 else jsonify({'image_urls': []})


@app.route('/get_images/<string:image_type>', methods=['GET'])
def get_images(image_type):
    return get_images_by_type(image_type)
   

# producto uno comentarios
@app.route('/get_producto_<string:nombre_producto>/<departamento>', methods=['GET'])
def get_producto_uno(nombre_producto,departamento):
    products3 = {'uno':'RRQPE','dos':'LST','tres':'ACHA','cuatro':'ACHT','cinco':'ACM','seis':'DMWV','siete':'TPW','ocho':'ACTP'}
    prefix = f'{products3[nombre_producto]}/{departamento}'
    s3 = boto3.client('s3')
    bucket_name = 'eata-smartmachines'

    # Listar objetos en la carpeta especificada
    objetos = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

    # Buscar un archivo .txt específico y leer su contenido
    response = {
            "fecha": "",
            "texto": ""
        }
    # Buscar un archivo .txt específico y leer su contenido
    for objeto in objetos.get('Contents', []):
        if objeto['Key'].endswith('.txt'):  # Asegurarse de que es un archivo .txt
            # Obtener el objeto
            file = s3.get_object(Bucket=bucket_name, Key=objeto['Key'])
            # Leer el contenido del archivo
            content = file['Body'].read().decode('utf-8')  # Asumiendo que el texto está en UTF-8
            
            # Obtener la fecha y hora de la última modificación del archivo
            last_modified = objeto['LastModified']
            last_modified_adjusted = last_modified - timedelta(hours=5)
            # Formatear la fecha y hora en el formato deseado y almacenar en el diccionario
            response['fecha'] = last_modified_adjusted.strftime("%Y-%m-%d HORA:%H:%M")
            
            # Almacenar el contenido del archivo en la clave 'texto'
            response['texto'] = content
            
            break  # Romper el bucle después de encontrar y leer el primer archivo .txt

    return jsonify({'value': response})
# producto dos comentarios





'''
def get_images_by_type_and_department(image_type, department):
    prefix = f'Images/T{image_type}{department.capitalize()}/'
    bucket = storage.bucket()
    images = bucket.list_blobs(prefix=prefix)
    existing_images = [image for image in images if image.exists()]
    image_urls = [image.generate_signed_url(
                version="v4",
                expiration=timedelta(days=7),
                method="GET"
            ) for image in existing_images]
    return jsonify({'image_urls': image_urls[1:]}) if len(image_urls) > 1 else jsonify({'image_urls': []})'''


def get_images_by_type_and_department(image_type, department):
    products3={1:'RRQPE',2:'LST',3:'ACHA',4:'ACHT',5:'ACM',6:'DMWV',7:'TPW',8:'ACTP'}
    # Configura el cliente de S
    prefix = f'{products3[image_type]}/{department}'
    s3 = boto3.client('s3')

    # Lista objetos en la carpeta
    objetos = s3.list_objects_v2(Bucket='eata-smartmachines', Prefix=prefix)

    # Obtiene las URLs prefirmadas para cada objeto en la carpeta
    urls_publicas = []
    for objeto in objetos.get('Contents', []):
        objeto_key = objeto['Key']
        # Genera la URL prefirmada
        if objeto_key.lower().endswith('.png'):
            url = s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': 'eata-smartmachines', 'Key': objeto_key},
                ExpiresIn=3600  # Caducidad en segundos (1 hora)
            )
            urls_publicas.append(url)

    return jsonify({'image_urls': urls_publicas[0:]}) if len(urls_publicas) >= 1 else jsonify({'image_urls': []})

@app.route('/get_images_t<int:image_type>_<string:department>', methods=['GET'])
def get_images_d(image_type, department):
    return get_images_by_type_and_department(image_type, department)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug=True)
