class Personaje:
    # Attributes
    nombre = 'default'
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

# Constructor variable of the class
mi_personaje = Personaje()

mi_personaje.nombre = "queso"
mi_personaje.fuerza = 666
print("El nombre del personaje es", mi_personaje.nombre)
print("La fuerza del personaje es", mi_personaje.fuerza)