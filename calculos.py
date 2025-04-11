def calcular_risco_total(dados):
    R_A = dados["numero_pessoas"] * dados["isoceraunico"] * 1e-6  # Exemplo simples
    R_total = R_A
    resultado = {
        "R_total": R_total,
        "R_toleravel": 1e-5,
        "necessita_spda": R_total > 1e-5
    }
    return resultado