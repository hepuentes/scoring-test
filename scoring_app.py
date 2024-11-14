import streamlit as st

# Título de la aplicación
st.title("Sistema de Scoring para Línea de Crédito Loansi")

# Función para calcular el puntaje de crédito
def calcular_scoring(ingresos_semanales, ocupacion, referencias, calidad_referencia, historial_pago, puntaje_datacredito):
    # Puntaje por Ingresos y Estabilidad
    if ingresos_semanales > 250000:
        puntaje_ingresos = 20
    elif 150000 <= ingresos_semanales <= 250000:
        puntaje_ingresos = 15
    else:
        puntaje_ingresos = 10

    if ocupacion in ["Empleado", "Comerciante fijo", "Independiente", "Vendedor ambulante"]:
        puntaje_ocupacion = 20
    else:
        puntaje_ocupacion = 10

    # Puntaje total de ingresos y estabilidad
    puntaje_ingresos_total = puntaje_ingresos + puntaje_ocupacion

    # Puntaje por Referencias Personales
    if referencias == 2:
        puntaje_referencias = 10
    elif referencias == 1:
        puntaje_referencias = 5
    else:
        puntaje_referencias = 0

    if calidad_referencia in ["Familiar directo", "Amigo confiable"]:
        puntaje_calidad = 10
    else:
        puntaje_calidad = 5

    # Puntaje total de referencias
    puntaje_referencias_total = puntaje_referencias + puntaje_calidad

    # Puntaje por Historial de Pagos
    if historial_pago == "Buen historial completo":
        puntaje_historial = 40
    elif historial_pago == "Retrasos menores":
        puntaje_historial = 25
    elif historial_pago == "Historial único":
        puntaje_historial = 20
    else:
        puntaje_historial = 15

    # Puntaje por Datacrédito
    if puntaje_datacredito > 600:
        puntaje_datacredito_final = 30
    elif 500 <= puntaje_datacredito <= 600:
        puntaje_datacredito_final = 20
    elif 400 <= puntaje_datacredito < 500:
        puntaje_datacredito_final = 10
    else:
        puntaje_datacredito_final = 0  # Rechazo potencial

    # Puntaje total
    puntaje_total = puntaje_ingresos_total + puntaje_referencias_total + puntaje_historial + puntaje_datacredito_final

    # Calificación de Riesgo
    if puntaje_total <= 45:
        calificacion_riesgo = "Alto Riesgo - Rechazo Potencial"
    elif 46 <= puntaje_total <= 70:
        calificacion_riesgo = "Riesgo Medio - Aprobación con Condiciones"
    else:
        calificacion_riesgo = "Bajo Riesgo - Aprobación Estándar"

    return puntaje_total, calificacion_riesgo

# Entrada de datos del usuario
ingresos_semanales = st.number_input("Ingresos semanales (COP):", min_value=0, step=10000)
ocupacion = st.selectbox("Ocupación", ["Empleado", "Comerciante fijo", "Independiente", "Vendedor ambulante", "Otro"])
referencias = st.selectbox("Número de referencias personales", [0, 1, 2])
calidad_referencia = st.selectbox("Calidad de la referencia", ["Familiar directo", "Amigo confiable", "Otro"])
historial_pago = st.selectbox("Historial de pagos con Loansi", ["Buen historial completo", "Retrasos menores", "Historial único", "Nuevo cliente"])
puntaje_datacredito = st.number_input("Puntaje en Datacrédito (Si no tiene historial, ingrese 600):", min_value=0, step=50)

# Botón para calcular el puntaje
if st.button("Calcular Puntaje"):
    puntaje, riesgo = calcular_scoring(ingresos_semanales, ocupacion, referencias, calidad_referencia, historial_pago, puntaje_datacredito)
    st.write("### Resultado de Scoring")
    st.write(f"**Puntaje Total**: {puntaje}")
    st.write(f"**Calificación de Riesgo**: {riesgo}")
