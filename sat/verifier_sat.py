from typing import List, Dict

def verify_sat_solution(clauses: List[List[int]], assignment: Dict[int, bool]) -> bool:
    """
    Vérifie si l'affectation 'assignment' satisfait toutes les clauses de la formule.
    :param clauses: liste de clauses (format identique à solve_sat).
    :param assignment: dictionnaire { var_index -> bool } 
    :return: True si l'affectation satisfait la formule, False sinon
    """
    if assignment == {}: return False
    for clause in clauses:
        satisfied = False
        for literal in clause:
            if literal > 0 and assignment[abs(literal)] is True:
                satisfied = True
                break
            if literal < 0 and assignment[abs(literal)] is False:
                satisfied = True
                break
        if not satisfied:
            return False
    return True
