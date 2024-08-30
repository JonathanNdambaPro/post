text = """
Faire du code maintenable c’est essentiel, mais en python ça peut rapidement devenir un cauchemar 😱


Au debut t’apprend le best practice, tu t’améliore et tu le sais tu te dis que tu vas continuer à faire de ton mieux et ça paye !

Mais Python n’est pas fortement typé donc il manque une sécurité, mais pas grave tu vas utiliser le typing


Oh boy ! avant de te lancer dans cette aventure je vais t’éclairer sur les syntaxe le plus mystérieuse de ce type 👇


🔢Sequence : On est pas obligé de savoir si c’est une liste, un tuple ou je ne sais quoi encore, jus Sequence
🔡TypeVar : Tu ne sais pas si ton type sera un int, float ou string, ça peut même être l’un des trois, TypeVar est fait pour toi
⚙️Callable : Tout ce qui peut être appelé, donc dans 90% une fonction
👤Self : Rare mais il y a des moments ou une classe dois se retourner elle même
📝Literal : on peut avoir un ensemble de string limité desfois, alors voilà
📦Unpack : args et kwargs c’est pénible à modéliser avec le typing, enfin c’était avant le typing
✅runtime_checkable : on peut rendre facilement une classe


Bon je ne pense pas qu’on va partir sur des codes avec autant de principe, ça serait un peu overkill.

Et sinon toi tu utilise le typing ? Dis-moi tout en commentaire
"""

lenght_text = len(text)

print(lenght_text)
