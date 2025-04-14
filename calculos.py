def determinar_nivel_protecao(R):
    if R > 1e-2:
        return "Excede Nível IV (Risco muito alto)"
    elif R > 1e-3:
        return "Nível IV"
    elif R > 1e-4:
        return "Nível III"
    elif R > 1e-5:
        return "Nível II"
    else:
        return "Nível I"

def calcular_risco_total(dados):
    N_g = dados["isoceraunico"]
    A_eq = dados["area"] / 1e6
    N_d = 3
    P_h = 0.1

    R_A = N_g * A_eq * N_d * P_h
    nivel = determinar_nivel_protecao(R_A)

    resultado = {
        "R_total": R_A,
        "R_toleravel": 1e-5,
        "nivel_protecao": nivel,
        "necessita_spda": R_A > 1e-5
    }
    return resultado