def calcular_risco_total(dados):
    # Parâmetros de entrada
    N_g = dados["isoceraunico"]      # tempestades por ano
    A_eq = dados["area"] / 1e6       # área da edificação em km²
    N_d = 3                          # descargas por tempestade (valor padrão da NBR)
    P_h = 0.1                        # fator de perda humana (simplificado)

    # Cálculo de risco à vida humana (R_A)
    R_A = N_g * A_eq * N_d * P_h

    resultado = {
        "R_total": R_A,              # neste estágio, só R_A está sendo calculado
        "R_toleravel": 1e-5,         # valor tolerável para vida humana
        "necessita_spda": R_A > 1e-5
    }
    return resultado