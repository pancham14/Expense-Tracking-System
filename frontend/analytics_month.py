import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://localhost:8000"


def analytics_month_tab():
    st.subheader("Expense Breakdown By Month")
    response = requests.get(f"{API_URL}/analytics/month")
    if response.status_code == 200:
        data = response.json()
    else:
        st.error("Failed to retrieve expenses")
        data = []

    df = pd.DataFrame(data)
    st.bar_chart(data=df.set_index("Month")['Total'], use_container_width=True)
    # fig = px.bar(df, x="Month", y="Total")
    # fig.update_xaxes(tickangle=0)
    # st.plotly_chart(fig)
    df['Total'] = df['Total'].map("{:.2f}".format)
    st.table(df)


