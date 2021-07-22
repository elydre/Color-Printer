from ColorPrint import *

colorprint("coucou",Colors.noir)
colorprint("coucou",Colors.rouge)
colorprint("coucou",Colors.vert)
colorprint("coucou",Colors.jaune)
colorprint("coucou",Colors.bleu)
colorprint("coucou",Colors.magenta)
colorprint("coucou",Colors.cyan)
colorprint("coucou",Colors.blanc)

print("")

colorprint("coucou",Colors.none,Background.noir)
colorprint("coucou",Colors.none,Background.rouge)
colorprint("coucou",Colors.none,Background.vert)
colorprint("coucou",Colors.none,Background.jaune)
colorprint("coucou",Colors.none,Background.bleu)
colorprint("coucou",Colors.none,Background.magenta)
colorprint("coucou",Colors.none,Background.cyan)
colorprint("coucou",Colors.noir,Background.blanc)

print("")

colorprint("coucou",Colors.none,Background.none,False,False)
colorprint("coucou",Colors.none,Background.none,True,False)
colorprint("coucou",Colors.none,Background.none,False,True)
colorprint("coucou",Colors.none,Background.none,True,True)