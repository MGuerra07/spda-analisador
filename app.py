import streamlit as st
from calculos import calcular_risco_total
from relatorio import gerar_pdf_relatorio

st.set_page_config(page_title="Análise de Risco SPDA", layout="centered")

st.title("⚡ Análise de Risco SPDA - NBR 5419")
st.markdown("Preencha os dados da edificação para realizar a análise de risco de descargas atmosféricas.")

with st.form("formulario_spda"):
    tipo_estrutura = st.selectbox("🏢 Tipo da Estrutura", ["Residencial", "Hospital", "Escola", "Indústria", "Comercial", "Outro"])
    area = st.number_input("📐 Área da Edificação (m²)", min_value=10.0)
    numero_pessoas = st.number_input("👥 Número Médio de Pessoas", min_value=0)
    isoceraunico = st.number_input("🌩️ Número de tempestades por ano (N_g)", min_value=0.0)
    tipo_solo = st.selectbox("🧱 Tipo de Solo", ["Alta Resistividade", "Baixa Resistividade"])
    enviar = st.form_submit_button("🔍 Calcular Risco")

if enviar:
    dados = {
        "tipo_estrutura": tipo_estrutura,
        "area": area,
        "numero_pessoas": numero_pessoas,
        "isoceraunico": isoceraunico,
        "tipo_solo": tipo_solo
    }

    resultado = calcular_risco_total(dados)

    st.subheader("📊 Resultado da Análise:")
    st.write(f"**Risco Total (R):** {resultado['R_total']:.2e}")
    st.write(f"**Risco Tolerável (R_T):** {resultado['R_toleravel']:.1e}")

    if resultado["necessita_spda"]:
        st.error("⚠️ SPDA OBRIGATÓRIO: o risco excede o tolerável.")
    else:
        st.success("✅ SPDA NÃO OBRIGATÓRIO: risco dentro do tolerável.")

    # Gera PDF e permite download
    pdf_bytes = gerar_pdf_relatorio(dados, resultado)
    st.download_button("📥 Baixar Relatório em PDF", data=pdf_bytes, file_name="relatorio_spda.pdf", mime="application/pdf")