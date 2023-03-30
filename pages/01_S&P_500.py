import streamlit as st
import plotly.express as px
from syp import *

st.title('Indice bursatil del S&P 500')
st.markdown('***')

st.subheader('Top 10 Empresas u Organizacion')
st.markdown('_Puede elegir entre **VALOR DE CRECIMIENTO PROMEDIO("mean_total)** y **PROMEDIO PORCENTUAL DE CRECIMIENTO(growth)**_')
select1=st.selectbox('Mean_Total / Growth',['mean_total','growth'])
top=top_ten(select1)
fig=px.line(close_anual[close_anual.index.isin(top)].transpose())
st.plotly_chart(fig,use_container_width=True)  

st.subheader('Crecimiento promedio por año')

select = st.selectbox(label='Metricas',options=anual_syp.columns)
data=value_extreme(anual_syp,select) 
fig = px.bar(data, x=data.index,y=data[select] )
st.plotly_chart(fig,use_container_width=True)
st.markdown('***')


cre=creci_porcentaje(anual_syp)

st.header('Porcentaje de crecimiento año a año')
fig =px.bar(cre[1])
st.plotly_chart(fig,use_container_width=True)
st.markdown(f'* Promedio porcentual anual de crecimiento: {cre[0]} %')

st.markdown('***')
st.header('Filtrar por año')

st.markdown('_podremos observar años a año y mes a mes el crecimiento porcentual_')
anio = st.slider('Año',2000,2023)
syp=syp
month=ratio_month(anio,syp)
r_month= creci_porcentaje(month)
st.markdown(f'* Crecimiento promedio porcentual mensual de : {r_month[0]}')
fig =px.bar(r_month[1])
st.plotly_chart(fig,use_container_width=True)
st.markdown('## Datos agrupados por años')
st.markdown('***')
st.table(anual_syp)
