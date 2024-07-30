from desafioadl.models import Tarea,SubTarea
# a. recupera_tareas_y_sub_tareas
def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.filter(eliminada=False)
    subtareas = SubTarea.objects.filter(eliminada=False)
    return tareas, subtareas

# b. crear_nueva_tarea
def crear_nueva_tarea(descripcion):
    tarea = Tarea(descripcion=descripcion)
    tarea.save()
    return tarea

# c. crear_sub_tarea
def crear_sub_tarea(descripcion, tarea):
    subtarea = SubTarea(descripcion=descripcion, tarea_id=tarea)
    subtarea.save()
    return subtarea


# d. elimina_tarea
def elimina_tarea(tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.eliminada = True
    tarea.save()
    return tarea

# e. elimina_sub_tarea
def elimina_sub_tarea(subtarea_id):
    subtarea = SubTarea.objects.get(id=subtarea_id)
    subtarea.eliminada = True
    subtarea.save()
    return subtarea

# f. imprimir_en_pantalla 
def imprimir_en_pantalla():
    tareas, subtareas = recupera_tareas_y_sub_tareas()
    for tarea in tareas:
        print(f"Tarea: {tarea.descripcion}")
        subtareas_tarea = subtareas.filter(tarea_id=tarea)
        for subtarea in subtareas_tarea:
            print(f"  SubTarea: {subtarea.descripcion}")
