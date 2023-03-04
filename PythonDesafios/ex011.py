n1 = float(input("Largura da parede: "))
n2 = float(input("Altura da parede: "))
área = n1 * n2
tinta = área / 2
print ("Sua parede tem a dimensão de {}x{} e sua área é de {}m²! \n Para pintar essa parede, você precisará de {}l!".format(n1,n2,área,tinta))
