import streamlit as st
import pandas as pd
import numpy as np 

st.set_page_config(
    page_title = 'Streamlit Dashboard ',
    page_icon = '✅',
    layout = 'wide'
)

st.markdown("## Dashboard For European Union Road Safety")

# kpi 1 

kpi1, kpi2, kpi3 = st.beta_columns(3)

with kpi1:
    st.markdown("* Increase in vehicle ownership in the rich countries leads to congestions on the roads, subsequently  reducing number of accidents hence low number of deaths per million inhabitants.")
    

with kpi2:
    st.markdown("* Rich countries  have well developed transport systems hence low deaths per million inhabitants.")
    
with kpi3:
    st.markdown("* Human congestion increases traffic leading to low deaths per million inhabitants in rich countries.")
    


st.markdown("<hr/>",unsafe_allow_html=True)

st.markdown(f'<iframe src="https://public.tableau.com/views/roadsafety_16279455323520/Dashboar?:language=en-US&:showVizHome=no&:display_count=n&:origin=viz_share_link" width="1500" height="872" frameborder="0"></iframe>', unsafe_allow_html=True)

