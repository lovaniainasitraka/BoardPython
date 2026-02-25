import random

# Création du plateau
def newBoard(n, p):
    board = []
    for i in range(n):
        board.append(random.randint(0, p))
    return board

# Affichage du plateau
def display(board, n):
    print("\nPlateau du Jeu :")

    # Affichage des pions
    for i in range(n):
        print("|", board[i], end=" ")
    print("|")

    # Affichage des indices
    for i in range(n):
        print("|", i, end=" ")
    print("|")

    print()


# Vérifie si une case est jouable (corrigée, indices 0..n-1)
def possibleSquare(board, n, i):
    if i < 1:
        return False
    if i >= n:
        return False
    if board[i] == 0:
        return False
    return True

# Sélection de la case de départ
def selectSquare(board, n):
    i = -1
    while i < 0 or i >= n or board[i] == 0 or i == 0:
        i = int(input("Choisir une case de départ : "))
        if i < 0 or i >= n or board[i] == 0 or i == 0:
            print("Case invalide.")
    return i

# Vérifie si la destination est valide (corrigée, indices 0..n-1)
def possibleDestination(board, n, i, j):
    if j < 0:
        return False
    if j >= n:
        return False
    if j >= i:
        return False
    return True

# Sélection de la destination
def selectDestination(board, n, i):
    j = -1
    while j < 0 or j >= n or j >= i:
        j = int(input("Choisir une case destination : "))
        if j < 0 or j >= n or j >= i:
            print("Destination invalide.")
    return j

# Déplacement du pion
def move(board, i, j):
    board[i] = board[i] - 1
    board[j] = board[j] + 1

# Vérifie si le joueur a perdu
def lose(board, n):
    for i in range(1, n):
        if board[i] > 0:
            return False
    return True

# Jeu principal
def jeu(n, p):
    board = newBoard(n, p)
    joueur = 1
    partie_terminee = False

    while partie_terminee == False:
        display(board, n)

        if lose(board, n):
            print("Le joueur", joueur, "a perdu !")
            partie_terminee = True
        else:
            print("Tour du joueur", joueur)
            i = selectSquare(board, n)
            j = selectDestination(board, n, i)
            move(board, i, j)

            # Changement de joueur
            if joueur == 1:
                joueur = 2
            else:
                joueur = 1

n = -1
while n <= 0:
    n = int(input("Entrez le nombre de cases du plateau : "))

p = -1
while p <= 0:
    p = int(input("Entrez le nombre maximal de pions par case : "))

jeu(n, p)