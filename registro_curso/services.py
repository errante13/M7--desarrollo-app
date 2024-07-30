from registro_curso.models import * 

def crear_curso(codigo, nombre, version):
    curso = Curso(
        codigo=codigo,
        nombre=nombre,
        version=version
    )
    curso.save()
    return curso
    
    
#● crear_profesor
def crear_profesor(rut, nombre, apellido, activo, creacion_registro, modificacion_registro, creado_por):
    profesor = Profesor(rut=rut, nombre=nombre, apellido=apellido, activo=activo,
                        creacion_registro=creacion_registro, modificacion_registro=modificacion_registro,
                        creado_por=creado_por)
    profesor.save()
    return profesor


#● crear_estudiante
def crear_estudiante(rut, nombre, apellido, fecha_nacimiento, creado_por):
    estudiante = Estudiante(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        activo=True,
        creado_por=creado_por,
        fecha_nacimiento=fecha_nacimiento
    )
    estudiante.save()
    return estudiante

# ● crear_direccion
def crear_direccion(calle, numero, depto, comuna, ciudad, region, estudiante):
    direccion = Direccion(
        calle=calle,
        numero=numero,
        depto=depto,
        comuna=comuna,
        ciudad=ciudad,
        region=region,
        estudiante_id=estudiante
    )
    direccion.save()
    return direccion


#● obtiene_estudiante
def obtiene_estudiante(rut):
    return Estudiante.objects.get(rut=rut)

#● obtiene_profesor
def obtiene_profesor(rut):
    return Profesor.objects.get(rut=rut)

#● obtiene_curso
def obtiene_curso(codigo):
    return Curso.objects.get(codigo=codigo)

# ● agrega_profesor_a_curso
def agrega_profesor_a_curso(profesor, curso):
    curso.Profesor_id.add(profesor)
    curso.save()
    
# ● agrega_cursos_a_estudiante
def agrega_cursos_a_estudiante(estudiante, cursos):
    estudiante.cursos.add(*cursos)
    estudiante.save()
    
    
# ● imprime_estudiante_cursos
def imprime_estudiante_cursos(estudiante):
    cursos = estudiante.cursos.all()
    for curso in cursos:
        print(f"Curso: {curso.nombre}, Versión: {curso.version}")
