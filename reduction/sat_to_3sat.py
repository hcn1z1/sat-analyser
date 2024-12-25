# reduction/sat_to_3sat.py

from typing import List, Dict

def reduce_sat_to_3sat(clauses: List[List[int]], nb_vars: int):
    """
    Transforme une instance SAT en instance 3-SAT.
    :param clauses: clauses en format (ex: [ [1,2,3], [1,-2,4,5], ... ])
    :param nb_vars: nombre initial de variables
    :return: (new_clauses, new_nb_vars, mapping) 
             où 
               - new_clauses est la liste de clauses 3-SAT
               - new_nb_vars est le nouveau nombre total de variables
               - mapping (optionnel) permet de récupérer la solution d'origine 
                 depuis la solution 3-SAT si on veut reconstruire l'affectation.
    """

    new_clauses = []
    current_var_index = nb_vars  # On créera de nouvelles variables si nécessaire
    # Parcourir chaque clause, la découper en clauses de 3 littéraux max
    for clause in clauses:
        while len(clause) > 3:
            # On prend les deux premiers littéraux et un nouveau littéral
            lit1 = clause.pop(0)
            lit2 = clause.pop(0)
            current_var_index += 1
            new_lit = current_var_index  # variable fraîche
            # Créer la clause [lit1, lit2, new_lit]
            new_clauses.append([lit1, lit2, new_lit])
            clause.insert(0, -new_lit)

        # Ici, la clause a au plus 3 littéraux, on l’ajoute telle quelle
        new_clauses.append(clause)

    new_nb_vars = current_var_index
    mapping = {} 
    return new_clauses, new_nb_vars, mapping
