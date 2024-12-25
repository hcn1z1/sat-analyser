# sat/utils_sat.py

from typing import List

def read_instance_from_file(filename: str):
    """
    Lit un fichier contenant la description d'une instance SAT et retourne 
    la liste de clauses et le nombre de variables.
    
    Format d'exemple (libre à vous de le définir / adapter) :
    La première ligne contient : <nb_vars> <nb_clauses>
    Les lignes suivantes décrivent les clauses :
       littéral1 littéral2 ... littéralK 0
    
    Où chaque littéral est un entier : i (pour x_i) ou -i (pour ¬x_i).
    Le '0' en fin de ligne sert juste de séparateur de fin de clause.
    
    Ex :
        3 3
        1 -2 0
        -1 3 0
        2 3 0
        
    Correspond à F = (x1 ∨ ¬x2) ∧ (¬x1 ∨ x3) ∧ (x2 ∨ x3) avec 3 variables, 3 clauses.
    
    :param filename: nom du fichier d'entrée
    :return: (clauses, nb_vars)
             clauses est une liste de listes d'entiers
             nb_vars est le nombre de variables
    """
    clauses = []
    nb_vars = 0
    with open(filename, 'r') as f:
        # Lire la première ligne : nb_vars, nb_clauses
        first_line = f.readline().strip()
        parts = first_line.split()
        nb_vars = int(parts[0])
        nb_clauses = int(parts[1])

        # Pour chaque clause, lire la ligne suivante
        for _ in range(nb_clauses):
            line = f.readline().strip()
            parts = line.split()
            
            clause = []
            for literal_str in parts:
                lit = int(literal_str)
                if lit == 0:
                    # le '0' marque la fin de la clause
                    break
                clause.append(lit)
            clauses.append(clause)

    return clauses, nb_vars


def write_instance_to_file(filename: str, clauses: List[List[int]], nb_vars: int):
    """
    Écrit une instance SAT dans un fichier, dans le même format que read_instance_from_file.
    
    :param filename: nom du fichier de sortie
    :param clauses: liste de clauses
    :param nb_vars: nombre de variables
    :return: None
    """
    with open(filename, 'w') as f:
        # Écrire nb_vars et le nombre de clauses
        f.write(f"{nb_vars} {len(clauses)}\n")
        
        # Écrire les clauses
        for clause in clauses:
            # On joint les littéraux, puis on ajoute un '0' en fin de clause
            # Ex : "1 -2 0"
            clause_str = " ".join(map(str, clause)) + " 0\n"
            f.write(clause_str)


def print_clauses(clauses: List[List[int]]):
    """
    Affiche la formule sous forme de clauses lisibles.
    Par exemple, (x1 ∨ ¬x2) ...
    """
    formula_str = []
    for clause in clauses:
        lits_str = []
        for lit in clause:
            if lit > 0:
                lits_str.append(f"x{lit}")
            else:
                lits_str.append(f"¬x{-lit}")
        formula_str.append("(" + " ∨ ".join(lits_str) + ")")
    print(" ∧ ".join(formula_str))
