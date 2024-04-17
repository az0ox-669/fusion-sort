---

# Fonction `fusion_sort` 

La fonction `fusion_sort` est une méthode de tri qui utilise l'algorithme de tri fusion pour trier un tableau donné.

## Paramètres
- `tab` : Liste ou tableau à trier.

## Retour
- Liste triée dans l'ordre croissant.

## Fonctionnement
1. La fonction commence par vérifier si la taille du tableau est inférieure ou égale à 1. Si c'est le cas, elle retourne simplement le tableau, car un tableau d'un élément ou aucun élément est déjà considéré comme trié.

2. Si le tableau contient plus d'un élément, elle affiche d'abord le tableau initial et ses étapes intermédiaires via la fonction `print_steps`.

3. Ensuite, elle appelle la fonction `merge_sort` pour trier le tableau en utilisant l'algorithme de tri fusion.

4. Une fois le tableau trié, la fonction affiche le tableau trié final et le retourne.

## Exemple d'utilisation
```python
fusion_sort([38, 27, 43, 3, 9, 82, 45, 88])
```

---

# Fonction `merge_sort`

La fonction `merge_sort` est une fonction récursive qui divise le tableau en sous-tableaux plus petits jusqu'à ce que chaque sous-tableau ne contienne qu'un seul élément, puis fusionne ces sous-tableaux dans l'ordre trié.

## Paramètres
- `tab` : Liste ou tableau à trier.
- `indentation` : (Facultatif) Niveau d'indentation pour l'affichage.

## Retour
- Liste triée dans l'ordre croissant.

## Fonctionnement
1. Si la taille du tableau est inférieure ou égale à 1, la fonction retourne simplement le tableau, car un tableau d'un élément ou aucun élément est déjà considéré comme trié.

2. Sinon, la fonction calcule l'indice du milieu du tableau (`mid`).

3. Elle divise le tableau en deux parties, gauche (`left`) et droite (`right`), et appelle récursivement `merge_sort` sur chacune de ces parties.

4. Elle fusionne ensuite les tableaux triés `left` et `right` en appelant la fonction `merge`.

5. Enfin, elle retourne le tableau fusionné et trié.

---

# Fonction `merge`

La fonction `merge` est une fonction auxiliaire utilisée par `merge_sort` pour fusionner deux sous-tableaux triés en un seul tableau trié.

## Paramètres
- `left` : Sous-tableau gauche à fusionner.
- `right` : Sous-tableau droit à fusionner.

## Retour
- Liste fusionnée et triée dans l'ordre croissant.

## Fonctionnement
1. La fonction initialise une liste vide `result` pour stocker le résultat de la fusion.

2. Elle utilise deux indices `i` et `j` pour parcourir les sous-tableaux `left` et `right` respectivement.

3. Tant que les indices `i` et `j` sont inférieurs à la longueur de leurs sous-tableaux respectifs, elle compare les éléments correspondants des sous-tableaux et ajoute le plus petit élément à `result`.

4. Si tous les éléments du sous-tableau gauche (`left`) ont été ajoutés à `result`, elle ajoute les éléments restants du sous-tableau droit (`right`) à `result`, et vice versa.

5. Elle retourne le tableau fusionné et trié.

---

# Fonction `print_steps`

La fonction `print_steps` est une fonction auxiliaire utilisée par `fusion_sort` pour afficher les étapes intermédiaires du tri fusion.

## Paramètres
- `tab` : Liste ou tableau à afficher.
- `indentation` : (Facultatif) Niveau d'indentation pour l'affichage.

## Fonctionnement
1. Si le tableau donné ne contient qu'un seul élément, la fonction affiche simplement ce tableau avec l'indentation appropriée.

2. Sinon, la fonction divise le tableau en deux parties, gauche (`left`) et droite (`right`), et affiche ces deux parties avec leur niveau d'indentation.

3. Elle appelle récursivement `print_steps` sur les sous-tableaux gauche et droit avec un niveau d'indentation accru.

--- 

Cette documentation explique en détail le fonctionnement de chaque fonction impliquée dans le tri fusion et fournit des exemples d'utilisation pour une meilleure compréhension.
