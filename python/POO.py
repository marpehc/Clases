class Personaje: 


    #Se inicia el constructor.
    def __init__(self, nombre, vida, fuerza, defensa ,inteligencia):
        self.vida = vida
        self.fuerza = fuerza 
        self.inteligencia = inteligencia
        self.nombre = nombre
        self.defensa = defensa
        
        
    #"Printea" los atributos del personaje
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("  Vida:", self.vida)
        print("  Fuerza:", self.fuerza)
        print("  Inteligencia:", self.inteligencia)
    #Sube de nivel los atributos.
    def SubirNivel(self, vida, fuerza, inteligencia):    
        self.vida = self.vida + vida
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
    
    
    
    def EstaVivo(self):
        #Indica si el personaje esta vivo con (True) en el caso de que este vivo o (False) en el caso de que este muerto. 
        return self.vida > 0
    
    def morir(self):
        #El personaje muere y su vida baja a 0
        self.vida = 0
    
    
    def daño(self, enemigo):
       return  self.fuerza - enemigo.defensa   


    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print("Has realizado", daño," puntos de daño", " al enemigo", enemigo.nombre)
        print("La vida actual del enemigo es:", enemigo.vida)
        
        if mi_enemigo.EstaVivo():
            print("La vida de ", mi_enemigo.nombre, " es de: ", mi_enemigo.vida)
            
            
            
            
#Da al personaje atributos. vida, fuerza, defensa, inteligencia.          
mi_personaje = Personaje("Marpehc", 100, 5, 10, 50)
mi_enemigo = Personaje("Delas", 40, 1, 2, 10)
print(mi_personaje.vida)

mi_personaje.atacar(mi_enemigo)
######

 
