# Fonction pour fusionner deux sous-tableaux triés
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Fonction récursive pour diviser et fusionner
def merge_sort(tab, indentation=0):
    if len(tab) <= 1:
        return tab
    mid = len(tab) // 2
    left = merge_sort(tab[:mid], indentation + 1)
    right = merge_sort(tab[mid:], indentation + 1)
    merged = merge(left, right)
    return merged

# Fonction pour afficher les étapes intermédiaires
def print_steps(tab, indentation=0):
    if len(tab) == 1:
        print("    " * indentation + f"|_{tab}")
        return
    mid = len(tab) // 2
    left = tab[:mid]
    right = tab[mid:]
    print("    " * indentation + "|_Left: ", left)
    print("    " * indentation + "|_Right:", right)
    print_steps(left, indentation + 1)
    print_steps(right, indentation + 1)
        

def fusion_sort(tab):
    if len(tab) <= 1:
        return tab

    print("Tableau initial :", tab)
    print_steps(tab)
    sorted_tab = merge_sort(tab)
    print("Tableau trié final :", sorted_tab)
    return sorted_tab

fusion_sort([38, 27, 43, 3, 9, 82, 45, 88])  # Copie du tableau pour ne pas le modifier
