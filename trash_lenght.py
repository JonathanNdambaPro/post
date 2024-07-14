text = """
T'as encore codé à la va-vite et tu nous as encore fait n'importe quoi 🤦🏻


Tu as un pipeline de données avec plein de formats de données différents.
Au début, c'était que des CSV, puis des XLS et des JSON. Le problème, c'est que dans la précipitation, tu as créé des classes pour chaque type de fichier, mais qui n'ont pas la même interface…
Niveau couplage, on peut difficilement faire pire…


Mais tout n'est pas fini, tu peux t'en sortir avec le pattern Adapter 👇
♻️ Réutilisation de code existant : pas besoin de tout recommencer, tu vas créer une classe qui va réutiliser ton code
🔧 Flexibilité et extensibilité : Tu pourras ajouter de nouvelles classes comme YAML par exemple très facilement
🔀 Migration simplifiée : Avec les adapters, si tu veux passer de CSV à pd.read_csv, c'est facile et à un seul endroit
📋 Standardisation de l'interface : Comme les adapters auront les mêmes méthodes, elles sont facilement interchangeables


Comme tu le vois, les design patterns sont souvent des solutions très utiles. Sinon, tu connais des design patterns ? Si oui, lesquels utilises-tu le plus ? Dis-moi tout en commentaire !
"""

lenght_text = len(text)

print(lenght_text)
