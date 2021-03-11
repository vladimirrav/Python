episode = "Episode 7 : Le pouvoir de l'eau (data)"

print(episode)
print("-" * len(episode))

import random

ValeurDuDe = random.randint(1,2)

if ValeurDuDe == 2:
  print("[" + str(ValeurDuDe) + "]", "Argonautes, direction le tourbillon")
else:
  print("[" + str(ValeurDuDe) + "]", "Argonautes, votre voyage durera encore 10 jours")