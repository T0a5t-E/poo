class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    def atributos(self):
        print(f"Nombre: {self.__nombre}\nFuerza: {self.__fuerza}\nInteligencia: {self.__inteligencia}\nDefensa: {self.__defensa}\nVida: {self.__vida}")
    
    def subir_nivel(self, fuerza, inteligencia, defensa, vida):
        self.__fuerza += fuerza
        self.__inteligencia += inteligencia
        self.__defensa += defensa
        self.__vida += vida

    def esta_vivo(self):
        return self.__vida > 0
    
    def morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")
    
    def dmg(self, enemigo):
        return enemigo.__defensa - self.__fuerza

    def atacar(self, enemigo):
        dmg = self.dmg(enemigo)
        enemigo.__vida -= dmg
        if not enemigo.esta_vivo():
            enemigo.morir()
        print("La vida de", enemigo.__nombre, "es", enemigo.__vida)
    
    def get_fuerza():
        return self.__fuerza
    
    def set_fuerza(self, fuerza):
        self.__fuerza = fuerza if fuerza > 0 else print("La fuerza debe ser mayor a 0")

mi_personaje = Personaje("Abadon", 616, 616, 616, 616) # Character constructor
mi_enemigo = Personaje("Gabriel", 777, 777, 777, 777)
mi_personaje._Personaje__fuerza = 10
mi_personaje.atributos()