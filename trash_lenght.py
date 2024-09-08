text = """
Le data modeling, c'est comme le papier toilette : mieux vaut ne pas oublier de s'en servir.
Oui oui, au début on décide de s'en passer, il faut aller vite et délivrer, puis on se rend compte qu'on ne comprend plus rien à la structure de notre data warehouse. Puis vient le moment où on paie un cabinet de conseil plusieurs millions pour rattraper cette immondice.
Pourtant, il existe plusieurs méthodes pour échapper à ce type de problème 👇
3ᵉ forme normale : L'une des méthodes les plus anciennes et les plus utilisées pour les OLTP. L'idée ici est de supprimer la redondance de données, supprimer les anomalies et réduire la volumétrie des données. En contrepartie, on augmente la complexité des requêtes.
Kimball : Ou star schema, les tables de faits et de dimensions facilitent l'accès aux données avec des requêtes simples et intuitives. On a plus de redondance de données et on doit gérer le slowly changing dimension.
One Big Table : Tout dans une seule table. En termes d'accessibilité, on ne peut pas faire mieux, mais au niveau de la redondance et de la volumétrie de données, on est mal, et pour les modifications de données, bonne chance.
Dans la majorité des cas, plusieurs solutions doivent être utilisées : une solution OLTP avec une 3ème forme normale et une autre avec Kimball/OBT. Sinon, tu fais comment toi ? Dis-moi tout en commentaire !
"""
lenght_text = len(text)

print(lenght_text)
