# LP Compiler – Mini Compilateur de Programmation Linéaire

Ce projet est un mini-compilateur pédagogique conçu pour illustrer les étapes classiques d’un compilateur appliqué à la résolution de problèmes de programmation linéaire (LP). Le compilateur prend en charge un problème LP comportant trois variables inconnues (`x1`, `x2`, `x3`) et intègre toutes les phases principales du processus de compilation ::

- **Lexing** : Découpage du texte source en tokens à l’aide d’expressions régulières.
- **Parsing** : Construction d’un arbre de syntaxe abstraite (AST) à partir des tokens.
- **Visitors** : Parcours de l’AST via le pattern Visitor, avec notamment un visiteur qui reformate le problème pour le rendre lisible (Pretty Printer).
- **Solver** : Extraction des coefficients linéaires pour un problème à 3 variables et retour d’une solution fictive.
- **Compilation** : Coordination de toutes ces étapes dans un module central.

> **Attention :** La solution retournée par le solveur est fictive. Ce projet sert de base pour comprendre la chaîne de compilation et peut être amélioré (par exemple, via l’implémentation d’un algorithme du simplexe ou l’intégration avec un solveur externe).

---

## Table des Matières

- [Fonctionnalités](#fonctionnalités)
- [Structure du Projet](#structure-du-projet)
- [Description des Modules](#description-des-modules)
  - [`__init__.py`](#__initpy)
  - [`ast.py`](#astpy)
  - [`lexer.py`](#lexerpy)
  - [`parser.py`](#parserpy)
  - [`visitors.py`](#visitorspy)
  - [`solver.py`](#solverpy)
  - [`compiler.py`](#compilerpy)
  - [`main.py`](#mainpy)
  - [`input.txt`](#inputtxt)
- [Installation et Utilisation](#installation-et-utilisation)
- [Améliorations Futures](#améliorations-futures)
- [Licence](#licence)

---

## Fonctionnalités

- **Analyse Lexicale :**  
  Le module `lexer.py` découpe le texte source en tokens (mots-clés, opérateurs, nombres, identifiants, etc.) grâce à des expressions régulières.

- **Analyse Syntaxique :**  
  Le module `parser.py` construit un arbre de syntaxe abstraite (AST) en vérifiant la validité du problème LP (un objectif suivi de contraintes).

- **Arbre de Syntaxe Abstraite (AST) :**  
  Le module `ast.py` définit les classes qui modélisent le problème LP, telles que `LPProblem`, `Objective`, `Constraint`, `BinOp`, `Num` et `Var`.

- **Pattern Visitor :**  
  Le module `visitors.py` contient une classe de base (`NodeVisitor`) et un visiteur spécifique, le `PrettyPrinterVisitor`, qui parcourt l’AST et affiche le problème sous une forme lisible.

- **Solveur Minimaliste :**  
  Le module `solver.py` extrait les coefficients d’expressions linéaires pour trois variables (`x1`, `x2`, `x3`) et renvoie une solution fictive.

- **Compilation :**  
  Le module `compiler.py` orchestre l’ensemble des étapes (lexing, parsing, affichage via le pretty printer et résolution) et fournit une interface simple pour compiler un problème LP.

- **Point d’Entrée :**  
  Le fichier `main.py` lit le fichier d’entrée (par exemple, `input.txt`), lance le compilateur et affiche le problème formaté ainsi que la solution.

---
## Description des Modules

### `__init__.py`
Ce fichier indique à Python que `proj_1` est un package. Il peut contenir des informations sur la version du projet et facilite les importations relatives dans l’ensemble du code.

### `ast.py`
Dans ce module, nous définissons les classes qui représentent l’arbre de syntaxe abstraite du problème LP. On y trouve la classe `LPProblem` (qui regroupe l’objectif et les contraintes), `Objective` (pour l’objectif, avec sa direction et son expression), `Constraint` (pour modéliser les contraintes via des opérateurs relationnels), ainsi que les classes `BinOp`, `Num` et `Var` pour représenter les opérations, les nombres et les variables dans les expressions.

### `lexer.py`
Le module du lexer analyse le texte source en utilisant des expressions régulières pour découper le contenu en tokens. Chaque token identifié possède un type (par exemple, `MAX`, `ID`, `NUMBER`, etc.) et une valeur correspondant à la chaîne de caractères reconnue. Les espaces et les commentaires sont ignorés afin de simplifier l’analyse syntaxique.

### `parser.py`
Ce module transforme la liste de tokens fournie par le lexer en un arbre de syntaxe abstraite. Le parseur utilise une approche récursive descendante pour analyser l’objectif (commençant par `max:` ou `min:`) ainsi que les contraintes associées (qui suivent un format de type `expr relop expr;`). En cas d’erreur de syntaxe, le parseur lève une exception descriptive.

### `visitors.py`
Ce module implémente le pattern Visitor pour parcourir l’AST. Il propose une classe de base `NodeVisitor` qui permet de définir des méthodes spécifiques pour chaque type de nœud, ainsi que la classe `PrettyPrinterVisitor` qui réécrit le problème LP de façon formatée et lisible, en affichant l’objectif et les contraintes avec une indentation appropriée.

### `solver.py`
Le solveur minimaliste extrait les coefficients des expressions linéaires du problème LP pour trois variables (`x1`, `x2`, `x3`). Bien que cette version ne calcule pas réellement la solution optimale, elle montre comment construire les matrices de coefficients. La solution retournée est fictive et sert à illustrer le processus global. Ce module peut être amélioré pour intégrer un véritable algorithme de résolution ou l’utilisation d’un solveur externe.

### `compiler.py`
Ce module central coordonne l’ensemble des étapes du compilateur. Il crée d’abord une instance du lexer pour tokeniser le texte, puis utilise le parseur pour construire l’AST. Le PrettyPrinterVisitor est ensuite appelé pour afficher le problème LP de manière lisible, et enfin le solveur est invoqué pour obtenir (fictivement) la solution. Ce fichier sert de façade à toutes les fonctionnalités du compilateur.

### `main.py`
Le point d’entrée du programme. Ce script lit un fichier d’entrée (par exemple, `input.txt`), initialise le compilateur (`LPCompiler`), lance la compilation du problème LP et affiche le problème formaté ainsi que la solution obtenue (fictive dans cette version).

### `input.txt`
Ce fichier contient un exemple de problème LP rédigé dans la syntaxe attendue. Par exemple :

Exemple LP

max: x1 + 2x2 - x3 + 10; x1 >= 0; x2 >= 0; x3 >= 0; x1 + x2 + x3 >= 20; x2 - 3x3 <= 5;



Il sert à tester et démontrer l’ensemble du processus, de l’analyse lexicale à la phase de résolution.

---

## Installation et Utilisation

### Prérequis
- Python 3.x doit être installé sur votre machine.

### Installation
1. Clonez le dépôt GitHub sur votre machine.
2. Vérifiez que la structure du dossier est conforme à celle présentée ci-dessus.

### Exécution
Placez-vous dans le répertoire parent de `proj_1` et lancez la commande suivante :

 python3 -m proj_1.main proj_1/input.txt

# LP Compiler – Mini Compilateur de Programmation Linéaire

Ce projet est un mini-compilateur pédagogique conçu pour illustrer les étapes classiques d’un compilateur appliqué à la résolution de problèmes de programmation linéaire (LP). Le compilateur prend en charge un problème LP comportant trois variables inconnues (`x1`, `x2`, `x3`) et intègre toutes les phases principales du processus de compilation.

---

## Améliorations Futures

- **Gestion Dynamique des Variables :**  
  Adapter le solveur pour traiter dynamiquement un nombre illimité de variables au lieu de trois fixes.

- **Intégration d’un Vrai Solveur :**  
  Remplacer la solution fictive par un algorithme réel (ex. simplexe) ou intégrer une bibliothèque externe comme PuLP, OR-Tools ou `scipy.optimize.linprog`.

- **Optimisation du Lexer et Parser :**  
  Utiliser des outils générateurs de lexers/parseurs (par exemple, PLY ou rply) pour améliorer la robustesse et les performances.

- **Vérifications Sémantiques :**  
  Implémenter un module de vérification pour assurer la linéarité des expressions et détecter les erreurs d’utilisation (comme la multiplication de deux variables).

- **Interface Utilisateur :**  
  Enrichir la ligne de commande avec des options supplémentaires (affichage détaillé, export de fichiers, etc.) et fournir une meilleure documentation.

---

## Licence

Ce projet est distribué sous licence MIT. Vous êtes libre de l’utiliser, le modifier et contribuer à son amélioration.

---

## Conclusion

Le mini-compilateur LP présenté ici constitue une base solide pour comprendre les différentes phases de la compilation appliquées à des problèmes de programmation linéaire. Conçu pour travailler avec trois variables (`x1`, `x2`, `x3`), il offre une architecture modulaire et évolutive qui peut être améliorée et adaptée en fonction de vos besoins pédagogiques ou professionnels.

Bonne exploration et bonnes expérimentations !

        
