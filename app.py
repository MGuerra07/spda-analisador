import streamlit as st
from calculos import calcular_risco_total
from relatorio import gerar_pdf_relatorio

st.set_page_config(page_title="SPDA - Análise de Risco", layout="centered")

st.markdown("## ⚡ Analisador de Risco SPDA (NBR 5419)")
st.markdown("Preencha os dados da estrutura abaixo para calcular o risco de descargas atmosféricas.")

with st.form("formulario_spda"):
    col1, col2 = st.columns(2)

    with col1:
        tipo_estrutura = st.selectbox("🏢 Tipo da Estrutura", ["Residencial", "Hospital", "Escola", "Indústria", "Comercial", "Outro"])
        area = st.number_input("📐 Área da Edificação (m²)", min_value=10.0)
        altura = st.number_input("📏 Altura da Estrutura (m)", min_value=1.0)
        tipo_solo = st.selectbox("🧱 Tipo de Solo", ["Alta Resistividade", "Baixa Resistividade"])

    with col2:
        numero_pessoas = st.number_input("👥 Número Médio de Pessoas", min_value=0)
        isoceraunico = st.number_input("🌩️ Número de Tempestades por Ano (N_g)", min_value=0.0)

    enviar = st.form_submit_button("🚀 Calcular Risco")

if enviar:
    if isoceraunico == 0:
        st.warning("⚠️ O valor de N_g (isoceraunico) não pode ser zero.")
    else:
        dados = {
            "tipo_estrutura": tipo_estrutura,
            "area": area,
            "altura": altura,
            "numero_pessoas": numero_pessoas,
            "isoceraunico": isoceraunico,
            "tipo_solo": tipo_solo
        }

        resultado = calcular_risco_total(dados)

        with st.expander("📊 Resultado da Análise", expanded=True):
            st.metric("Risco Total (R)", f"{resultado['R_total']:.2e}")
            st.metric("Risco Tolerável", f"{resultado['R_toleravel']:.1e}")
            st.info(f"Nível de Proteção: {resultado['nivel_protecao']}")

            if resultado["necessita_spda"]:
                st.error("⚠️ SPDA OBRIGATÓRIO")
            else:
                st.success("✅ SPDA NÃO OBRIGATÓRIO")

            pdf_bytes = gerar_pdf_relatorio(dados, resultado)
            st.download_button("📥 Baixar Relatório em PDF", data=pdf_bytes, file_name="relatorio_spda.pdf", mime="application/pdf")