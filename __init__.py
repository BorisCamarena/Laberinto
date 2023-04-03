from pyamaze import maze,agent

# Crear el laberinto.

# Como en el codigo principal se espefica las dimensiones del laberinto.

m = maze(25,40)

m.CreateMaze()

# Ponemos el agente cuadrado en el laberinto.

a = agent(m,footprints=True,filled=True)

# Graficamos la trayectoria del agente.

m.tracePath({a:m.path},delay=25)
m.run()
