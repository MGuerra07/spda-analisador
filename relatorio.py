from fpdf import FPDF
from io import BytesIO

def gerar_pdf_relatorio(dados, resultado):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Relatório de Análise de Risco - SPDA", ln=True)

    pdf.set_font("Arial", '', 12)
    pdf.ln(5)
    pdf.cell(0, 10, f"Tipo da Estrutura: {dados['tipo_estrutura']}", ln=True)
    pdf.cell(0, 10, f"Área: {dados['area']} m²", ln=True)
    pdf.cell(0, 10, f"Altura: {dados['altura']} m", ln=True)
    pdf.cell(0, 10, f"Número de Pessoas: {dados['numero_pessoas']}", ln=True)
    pdf.cell(0, 10, f"Tempestades por Ano (N_g): {dados['isoceraunico']}", ln=True)
    pdf.cell(0, 10, f"Tipo de Solo: {dados['tipo_solo']}", ln=True)

    pdf.ln(5)
    pdf.cell(0, 10, f"Risco Total (R): {resultado['R_total']:.2e}", ln=True)
    pdf.cell(0, 10, f"Risco Tolerável: {resultado['R_toleravel']:.1e}", ln=True)
    pdf.cell(0, 10, f"Nível de Proteção: {resultado['nivel_protecao']}", ln=True)
    status = "OBRIGATÓRIO" if resultado["necessita_spda"] else "NÃO OBRIGATÓRIO"
    pdf.cell(0, 10, f"SPDA: {status}", ln=True)

    output = BytesIO()
    pdf.output(output)
    output.seek(0)
    return output.read()