import streamlit as st
from calculos import calcular_risco_total
from relatorio import gerar_pdf_relatorio

st.set_page_config(page_title="SPDA - Análise de Risco", layout="centered")

st.markdown("## ⚡ Analisador de Risco SPDA (NBR 5419)")
st.markdown("Preencha os dados da estrutura abaixo para avaliar a necessidade de proteção contra descargas atmosféricas.")

# Layout com duas colunas
col1, col2 = st.columns(2)

with st.form("formulario_spda"):
    with col1:
        tipo_estrutura = st.selectbox("🏢 Tipo da Estrutura", ["Residencial", "Hospital", "Escola", "Indústria", "Comercial", "Outro"])
        area = st.number_input("📐 Área da Edificação (m²)", min_value=10.0)
        tipo_solo = st.selectbox("🧱 Tipo de Solo", ["Alta Resistividade", "Baixa Resistividade"])
    with col2:
        numero_pessoas = st.number_input("👥 Número Médio de Pessoas", min_value=0)
        isoceraunico = st.number_input("🌩️ Número de Tempestades por Ano (N_g)", min_value=0.0)

    enviar = st.form_submit_button("🚀 Calcular Risco")

if enviar:
    dados = {
        "tipo_estrutura": tipo_estrutura,
        "area": area,
        "numero_pessoas": numero_pessoas,
        "isoceraunico": isoceraunico,
        "tipo_solo": tipo_solo
    }

    resultado = calcular_risco_total(dados)

    with st.expander("📊 Resultado Detalhado", expanded=True):
        st.markdown("### Resultado da Análise")
        st.write(f"**Tipo da Estrutura:** {tipo_estrutura}")
        st.write(f"**Área:** {area} m²")
        st.write(f"**Número de Pessoas:** {numero_pessoas}")
        st.write(f"**Isoceraunico (N_g):** {isoceraunico}")
        st.write(f"**Risco Total (R):** {resultado['R_total']:.2e}")
        st.write(f"**Risco Tolerável (R_T):** {resultado['R_toleravel']:.1e}")

        if resultado["necessita_spda"]:
            st.error("⚠️ SPDA OBRIGATÓRIO: o risco excede o tolerável.")
        else:
            st.success("✅ SPDA NÃO OBRIGATÓRIO: risco dentro do tolerável.")

        pdf_bytes = gerar_pdf_relatorio(dados, resultado)
        st.download_button("📥 Baixar Relatório em PDF", data=pdf_bytes, file_name="relatorio_spda.pdf", mime="application/pdf")

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido por Marcelo Guerra | Projeto SPDA ⚙️")