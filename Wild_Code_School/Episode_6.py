'''
Dans l'éditeur de code ci-dessous, calculez la quantité d'eau consommée depuis le début du voyage :

1. Le navire est parti avec 1000 litres d'eau.
2. 390 litres ont été consommés depuis le départ.
3. Chaque Argonaute consomme 2L par jour (il y a 50 Argonautes)
Calculez le nombre de jours restant avant que l'équipage ne soit à court d'eau.

Trouvez la bonne équation pour faire ce calcul avec Python.

Ensuite, affichez les résultats à l'aide de la fonction print
'''

episode = "Episode 6 : Du vin à boire ! (data)"

print(episode)
print("-" * len(episode))

litres_eau = 1000
litres_consommes = 390
num_argonautes = 50
jours = round((litres_consommes / 50) / 2)
jours_restant = round(((litres_eau - litres_consommes) / 50) / 2)

print(
  "Litres d'eau: " + str(litres_eau),
  "Litres consommés: " + str(litres_consommes),
  "Argonautes: " + str(num_argonautes),
  "L'eau restant: " + str(litres_eau - litres_consommes),
  "Jours: " + str(jours),
  "Jours restant: " + str(jours_restant),
  sep="\n"
)