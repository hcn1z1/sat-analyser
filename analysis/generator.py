# analysis/generator.py

import random
from typing import List

def generate_random_sat_instance(nb_vars: int, nb_clauses: int, clause_size_min: int = 1, clause_size_max: int = 3) -> List[List[int]]:
    """
    Génère aléatoirement 'nb_clauses' clauses, chacune de taille aléatoire
    (entre clause_size_min et clause_size_max), sur 'nb_vars' variables.
    Les littéraux sont +/- i selon la variable.
    """
    clauses = []
    for _ in range(nb_clauses):
        size = random.randint(clause_size_min, clause_size_max)
        clause = []
        for _ in range(size):
            var = random.randint(1, nb_vars)
            # Choisir aléatoirement si c'est x_i ou ¬x_i
            sign = random.choice([1, -1])
            clause.append(sign * var)
        clauses.append(clause)
    return clauses

def generate_random_3sat_instance(nb_vars: int, nb_clauses: int) -> List[List[int]]:
    """
    Génère aléatoirement 'nb_clauses' clauses, chacune de taille 3.
    """
    clauses = []
    for _ in range(nb_clauses):
        # 3 littéraux différents
        clause = []
        used_vars = set()
        while len(clause) < 3:
            var = random.randint(1, nb_vars)
            if var not in used_vars:
                used_vars.add(var)
                sign = random.choice([1, -1])
                clause.append(sign * var)
        clauses.append(clause)
    return clauses
