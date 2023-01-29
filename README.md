# depot_cours_test_2

Deuxième dépot du projet car soucis sur le premier. Mon projet va être découpé en etapes. Cela va provoquer de la duplication de code. Mais comme je fait le projet en pyhton, il y a des soucis au niveau de  _parameterized_  et des  _imports_  donc je dois faire comme cela.

Tout les tests ont été réalisé selon le principe de TDD. On peut voir avec les commits que j'ai :
	- Coder les tests. Qui revenaient au rouge car les méthodes associés n'était pas codé.
	- Puis j'implémentais les méthodes et vérifiais que les tests devenaient verts.

Et enfin dans un dernier temps j'ai réussi a lier mon code et mes tests au monde réel.
Ce projet montre donc l'intérêt du code avec la méthode TDD pour éviter au maximum la dette technique et le code legacy.

## [](https://github.com/PierreGoupil13/depot_cours_test_2#etape-1)Etape 1

Tout d'abord je code le test qui vérifie les différentes étapes. Ceux-ci sont retourné rouge car rien n'est encore implémenté. Puis j'implémente ce qui est nécéssaire pour que ceux-ci deviennent vert. Enfin je re-test et en fonction du retour je re-implémente ou bien j'avance.

Il y a 3 tests : - Un premier qui vérifie que l'on renvoie bien un miroir. - Un deuxième qui vérifie que 'Bien dit' est retourné après le mot si celui-ci est un palindrome.  _Il est bien retourné sur une autre ligne mais avec Unittest je n'ai pas réussi a précisément vérifié cela._  - Enfin un troisième vérifie que 'Bonjour' et 'Au revoir' sont retournés après le mot en miroir.

## Etape 2
Tout d'abord je code le test qui vérifie les différentes étapes. Ceux-ci sont retourné rouge car rien n'est encore implémenté. Puis j'implémente ce qui est nécéssaire pour que ceux-ci deviennent vert. Enfin je re-test et en fonction du retour je re-implémente ou bien j'avance.

Les tests vérifie les mêmes retours que ceux de l'étapes 1. On introduit en revanche une notion de langue.

## Etape 3
Tout d'abord je code le test qui vérifie les différentes étapes. Ceux-ci sont retourné rouge car rien n'est encore implémenté. Puis j'implémente ce qui est nécéssaire pour que ceux-ci deviennent vert. Enfin je re-test et en fonction du retour je re-implémente ou bien j'avance.

Les tests vérifie les mêmes retours que ceux de l'étapes 1 et 2. On introduit en revanche une notion de périodes de la journées.

## Etape 4
Cette étapes a été faites en TDD mais plus compliqué a bien prouvé au niveau des tests. J'ai du adapter les tests a la période de la journée auquel j'ai codé. Aussi à la langue de mon système.

Les tests vérifie les mêmes retours que ceux de l'étapes 1 et 2. On introduit en revanche la connexion au système pour la langue, la période de la journée et l'input de l'utilisateur par la console.
