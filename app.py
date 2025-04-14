import streamlit as st
from calculos import calcular_risco_total
from relatorio import gerar_pdf_relatorio

st.set_page_config(page_title="Análise de Risco SPDA", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: #00c8c8;'>⚡ Análise de Risco - SPDA</h1>",
    unsafe_allow_html=True
)

st.image("https://via.placeholder.com/300x80.png?text=LOGO+SPDA", use_column_width=False)

st.markdown("---")
st.markdown(
    "<p style='text-align: center;'>Preencha os dados da estrutura para calcular o risco de descargas atmosféricas conforme a NBR 5419.</p>",
    unsafe_allow_html=True
)

with st.form("formulario_spda"):
    col1, col2 = st.columns(2)

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

    st.markdown("---")
    st.markdown("### 📊 Resultado da Análise")

    col1, col2 = st.columns(2)
    col1.metric("Risco Total (R)", f"{resultado['R_total']:.2e}")
    col2.metric("Risco Tolerável", f"{resultado['R_toleravel']:.1e}")

    st.info(f"🛡️ **Nível de Proteção Necessário:** {resultado['nivel_protecao']}")
    
    if resultado["necessita_spda"]:
        st.error("⚠️ SPDA OBRIGATÓRIO: o risco excede o tolerável.")
    else:
        st.success("✅ SPDA NÃO OBRIGATÓRIO: risco dentro do tolerável.")

    pdf_bytes = gerar_pdf_relatorio(dados, resultado)
    st.download_button("📥 Baixar Relatório em PDF", data=pdf_bytes, file_name="relatorio_spda.pdf", mime="application/pdf")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>Desenvolvido por Marcelo Guerra | Projeto SPDA ⚙️</p>", unsafe_allow_html=True)