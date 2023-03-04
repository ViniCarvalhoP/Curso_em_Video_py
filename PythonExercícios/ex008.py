frase = "Curso em Vídeo Python"
#print(len(frase))
#print(len(frase.strip()))
#print(frase.replace('Python','Android'))
print(frase[0])

#frase = "Curso em Vídeo Python"
#frase.replace("Python","Android")      - ERRADO
#print(frase)
frase = "Curso em Vídeo Python"
frase = frase.replace("Python","Android")  
print(frase)

frase = "Curso em Vídeo Python"
print("Curso" in frase)

frase = "Curso em Vídeo Python"
print(frase.find("Curso"))

frase = "Curso em Vídeo Python"
print(frase.lower().find("curso"))

frase = "Curso em Vídeo Python"
print(frase.split())

frase = "Curso em Vídeo Python"
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])