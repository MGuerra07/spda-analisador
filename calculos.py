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
    area_m2 = dados["area"]
    altura = dados["altura"]
    A_base = area_m2
    fator_altura = altura * (area_m2 ** 0.5)
    A_eq = A_base + fator_altura
    A_eq_km2 = A_eq / 1e6

    N_d = 3
    P_h = 0.1

    R_A = N_g * A_eq_km2 * N_d * P_h
    nivel = determinar_nivel_protecao(R_A)

    resultado = {
        "R_total": R_A,
        "R_toleravel": 1e-5,
        "nivel_protecao": nivel,
        "necessita_spda": R_A > 1e-5
    }
    return resultado