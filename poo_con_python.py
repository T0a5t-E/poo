class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    def atributos(self):
        print(f"Nombre: {self.__nombre}\nFuerza: {self.__fuerza}\nInteligencia: {self.__inteligencia}\nDefensa: {self.__defensa}\nVida: {self.__vida}")
        print(hercules.espada)
    
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
        return self.__fuerza * self.espada - enemigo.__defensa

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
    
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input(f"Elige un arma:\n(1) Espada de plata, DMG = 10\n(2) Espada de bronce, DMG = 8\n>> "))
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada = 8
        else:
            self.espada = 5

class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
    
    def atributos(self):
        return super().atributos()
        print("- Libro:", self.libro)

    def dmg(self, enemigo):
        return self.__inteligencia * self.libro - enemigo.__defensa

hercules = Guerrero("Hercules", 80, 50, 100, 100, 10)
abramelin = Mago("Abramelin", 33, 77, 77, 77, 77)
hercules.atributos()
abramelin.atributos()
abramelin.atacar(hercules)
hercules.atacar(abramelin)
hercules.atributos()
abramelin.atributos()