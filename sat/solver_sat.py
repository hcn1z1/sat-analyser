from typing import List, Dict

def solve_sat(clauses: List[List[int]], nb_vars: int) -> Dict[int, bool] | None:
    """
    Tente de trouver une affectation satisfaisant toutes les clauses.
    :param clauses: liste de clauses, chaque clause étant une liste de "littéraux"
                    Représentation usuelle : +i pour x_i, -i pour ¬x_i.
                    Exemple : la clause (x1 ∨ ¬x2 ∨ x3) = [1, -2, 3]
    :param nb_vars: nombre de variables, noté n
    :return: un dictionnaire { var_index -> bool } représentant l’affectation
             (True pour vrai, False pour faux) OU None si insatisfiable.
    """
    assignment = {}  # var_index -> bool, ex: {1: True, 2: False, ...}

    def backtrack(var_index: int) -> bool:
        # Si on a affecté toutes les variables, vérifier si l’affectation satisfait ttes les clauses
        if var_index > nb_vars:
            return check_all_clauses(assignment, clauses)

        # On peut essayer True puis False, ou l’inverse
        for val in [True, False]:
            assignment[var_index] = val
            if backtrack(var_index + 1):
                return True
        return False

    def check_all_clauses(assign: Dict[int, bool], cls: List[List[int]]) -> bool:
        # Vérifier que chaque clause possède au moins un littéral vrai sous 'assign'
        for clause in cls:
            satisfied = False
            for literal in clause:
                # Littéral positif i => variable i doit être True
                # Littéral négatif -i => variable i doit être False
                if literal > 0 and assign[abs(literal)] is True:
                    satisfied = True
                    break
                if literal < 0 and assign[abs(literal)] is False:
                    satisfied = True
                    break
            if not satisfied:
                return False
        return True

    if backtrack(1):
        return assignment
    else:
        return {}
