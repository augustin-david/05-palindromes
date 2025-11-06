"""Module principal pour vérifier les palindromes."""
import unicodedata
#### Fonction secondaire


def ispalindrome(p):
    """
    Vérifie si une chaîne de caractères est un palindrome.
    """
    p = unicodedata.normalize('NFD', p.lower())
    lettres = "".join(c for c in p if c.isalnum() and unicodedata.category(c) != 'Mn')
    return lettres == lettres[::-1]


#### Fonction principale


def main():
    """
    Fonction principale pour tester ispalindrome.
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
