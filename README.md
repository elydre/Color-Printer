# Installation
Téléchargez le repository, ColorPrint.py correspond au module et le fichier exemple.py permet d’avoir un aperçut de ses possibilités.
# Utilisation

## syntaxe:
```py
colorprint(text, color, code)
```
- text: texte à afficher
- color: couleur du texte (nom anglais ou code hex)
- code: "b" gras, "u" souligné, "k" désactivé saut de ligne (peut être combiné)

## exemple:

```py
colorprint("coucou", "red")
colorprint("coucou", "green", "b")
colorprint("coucou", "white", "bk")
colorprint("coucou", "#666600")
```
<img src="demo.png">