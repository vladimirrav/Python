episode = "Episode 9 : L'amour...(data)"

print(episode)
print("-" * len(episode))

#générer un chiffre aléatoire
import random

nbMilieu = random.randint(0,19)

while nbMilieu !=10:
  nbMilieu = random.randint(0,19)
  print("Le chiffre est", nbMilieu, ". Bien joué Jason! La pierre est au milieu. Les Spartiates se battent pour la pierre")