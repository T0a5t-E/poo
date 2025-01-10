class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(f"Nombre: {self.nombre}\nFuerza: {self.fuerza}\nInteligencia: {self.inteligencia}\nDefensa: {self.defensa}\nVida: {self.vida}")
    
    def subir_nivel(self, fuerza, inteligencia, defensa, vida):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
        self.vida += vida

    def confirmar_vida(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
    
    def dmg(self, enemigo):
        return enemigo.defensa - self.fuerza

    def atacar(self, enemigo):
        dmg = self.dmg(enemigo)
        enemigo.vida -= dmg
        print(self.nombre, "ha hecho", dmg, "de daño a", enemigo.nombre)
        print("La vida de", enemigo.nombre, "es", enemigo.vida)

mi_personaje = Personaje("Abadon", 616, 616, 616, 616) # Character constructor
mi_enemigo = Personaje("Gabriel", 777, 777, 777, 777)
print()
mi_personaje.atributos()
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()