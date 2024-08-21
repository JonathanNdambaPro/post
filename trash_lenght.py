text = """
Mettre son modèle ML en production, attendre sans jamais le réentraîner, voir que pour faire des prévisions de stock, il a en output des lettres 🤡



L'IA est pas mal à la mode, on fait nos petites inférences, on met le tout dans un docker et puis c'est parti !
Au début tout se passe bien, ensuite le modèle se dégrade sauf qu'on n'avait rien prévu et d'ailleurs on ne l'avait même pas monitoré....


Comment aurait-on pu faire pour gérer ça ?

Pas le choix, on doit tester en production, mais avec une bonne stratégie de déploiement 👇
⚫Shadow Deployment : Deux modèles en simultané, avec un champion qui est exposé à l'audience et un challenger qui lui ne l'est pas, celui qui a le meilleur score prend la place de champion
📊A/B Testing : Cette fois nos deux modèles sont exposés au trafic mais pas au même, il faut impérativement que les échantillons du champion et du challenger soient distincts et aléatoires
🐥Canary release : Ressemble à l'A/B test sauf qu'il n'y a pas d'aléatoire et que le challenger est obligatoirement exposé à une plus petite partie du trafic, c'est une sécurité pour éviter de finir comme CrowdStrike



Dans l'industrie la méthode la plus utilisée est l'A/B testing pour le moment mais la méthode Bandit est prometteuse. Sinon toi tu faisais comment ? Dis-moi tout en commentaire !
"""

lenght_text = len(text)

print(lenght_text)
