from typing import List, Dict

def solve_3sat(clauses: List[List[int]], nb_vars: int) -> Dict[int, bool] | None:
    """
    Tente de trouver une affectation satisfaisant toutes les clauses,
    sachant que chaque clause contient exactement 3 littéraux.
    """
    assignment = {}

    def backtrack(var_index: int) -> bool:
        if var_index > nb_vars:
            return check_all_clauses(assignment, clauses)

        for val in [True, False]:
            assignment[var_index] = val
            if backtrack(var_index + 1):
                return True
        return False

    def check_all_clauses(assign: Dict[int, bool], cls: List[List[int]]) -> bool:
        for clause in cls:
            satisfied = False
            for literal in clause:
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
