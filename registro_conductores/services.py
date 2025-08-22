from .models import Conductor, Direccion, Vehiculo,Artista, Album, ArtistaGrupo, Grupo
from datetime import date

def imprimir_modelos():
    conductores = Conductor.objects.all()
    for c in conductores:
        print(f"[{c.rut}]: {c.nombre} {c.apellido} - {c.fecha_nac}")
        if hasattr(c, "direccion"):
            d = c.direccion
            print(f"dirección: {d.calle} {d.numero} / {d.comuna} /{d.ciudad} / {d.region}")
        if hasattr(c, "vehiculo_set"):
            vehiculos = c.vehiculo_set.all()
            for v in vehiculos:
                print(f"Vehiculo: {v.marca} / {v.modelo} / {v.patente} /{v.year} ")

def crear_conductor(rut, nombre, apellido, fecha_nac):
    if not rut.isdigit() and not isinstance(fecha_nac, date):
        print("por favor validar los datos del conductor")
        return
    
    conductor = Conductor(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        fecha_nac=fecha_nac
    )
    conductor.save()
    imprimir_modelos()

def obtener_conductor(rut):
    return Conductor.objects.get(rut=rut)

def crear_direccion(conductor, calle, numero, dpto, comuna, ciudad, region):
    direccion = Direccion(
        conductor=conductor,
        calle=calle,
        numero=numero,
        dpto=dpto,
        comuna=comuna,
        ciudad=ciudad,
        region=region
    )
    direccion.save()
    imprimir_modelos()

def agregar_un_vehiculo(conductor, patente, marca, modelo, year):
    vehiculo = Vehiculo(
        conductor=conductor,
        patente=patente,
        marca=marca,
        modelo=modelo,
        year=year
    )

    vehiculo.save()
    imprimir_modelos()

def eliminar_vehiculo(vehiculo):
    Vehiculo.objects.get(id=vehiculo.id).delete()
    imprimir_modelos()

def eliminar_conductor(conductor):
    Conductor.objects.get(rut=conductor.rut).delete()


######################################################################################


def crear_artista(nombre, apellido, cantante=False, instrumento=""):
    artista = Artista(
    nombre=nombre, apellido=apellido, cantante=cantante,
    instrumento=instrumento
    )
    artista.save()
    return artista

def crear_grupo(nombre, fecha_creacion):
    if not isinstance(fecha_creacion, date):
        print("fecha con formato invalido, por favor, \
        ingresar en este formato. date(2000, 02, 28")
        return None
    grupo = Grupo(nombre=nombre, fecha_creacion=fecha_creacion)
    grupo.save()
    return grupo

def relacion_artista_grupo(artista, grupo, fecha_ingreso=None, agregado_por=None):
    if not isinstance(fecha_ingreso, date):
        print("fecha con formato invalido, por favor, \
        ingresar en este formato. date(2000, 02, 28")
        return None

    artista_relacion_grupo = ArtistaGrupo(
        artista=artista,
        grupo=grupo,
        fecha_ingreso=fecha_ingreso,
        agregado_por=agregado_por
        )
    artista_relacion_grupo.save()
    return artista_relacion_grupo

def agregar_album(grupo, titulo, year):
    album = Album(
    grupo=grupo, titulo=titulo, year=year
    )
    album.save()
    return album

def obtiene_artista(nombre, apellido):
    return (
    Artista.objects
    .filter(nombre=nombre)
    .filter(apellido=apellido).first()
    )

def obtiene_grupo(nombre):
    og = Grupo.objects.filter(nombre=nombre).first()
    return f"{og.nombre}"

def artista_pertenece_a_grupos(artista):
    if hasattr(artista, "grupos"):
        return artista.grupos.all()
    else:
        return None

def artista_participa_albumes(artista):
    """si el artista no tiene el
    atributo grupos, retorna None"""
    if not hasattr(artista, "grupos"):
        return None
    
    """Si por cada grupo al que pertenece el
    artista, no tiene el atributo album_set
    el ciclo continua."""
    encontrado = []
    for g in artista.grupos.all():
        if not hasattr(g, "albumes"):
            continue
        albumes = g.albumes.all()
        datos = {
        "grupo": g.nombre,
        "albumes": albumes
        }
        encontrado.append(datos)
    return encontrado

def grupo_albumes(grupo):
    if not hasattr(grupo, "albumes"):
        return None
    encontrado = []
    for a in grupo.albumes.all():
        encontrado.append(a)
    return encontrado
