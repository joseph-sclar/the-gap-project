import streamlit as st
import pandas as pd
import numpy as np

import seaborn as sns
import altair as alt
import plotly.express as px


import plotly.figure_factory as ff



st.title("Analysis 1")  


# Set pastel color palette
sns.set_palette("pastel")

# Streamlit app

st.header("**Are Clients More Satisfied with the Performance of Transportation Campaigns Compared to Robotics?**")
st.write("In order to determine whether clients are more satisfied with the performance of transportation campaigns compared to robotics, we will explore the data using two key metrics as proxies: the change in spend from 2022 to 2023 and the churn rate. By analyzing the budget reductions and audience retention rates for both sectors, we aim to understand the relative stability and client satisfaction associated with each campaign type.")

churn_data = pd.read_csv("data/churn_data.csv")


# Tabs for different plots
tab1, tab2 = st.tabs(["Budget Analysis",   "Churn Analysis" ])



with tab1:
    # Melt the data to have year as a variable
    melted_data = churn_data.melt(id_vars='industry', var_name='year', value_name='median_spend')

    # Set the maximum y-axis value
    max_y_value = 10000

    # Define color scale
    color_scale = alt.Scale(
        domain=['2022 median spend', '2023 median spend'],
        range=['lightblue', 'salmon']
    )

    # Create a bar chart
    chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('industry:N', title='Industry'),
        y=alt.Y('median_spend:Q', title='Median Spend', axis=alt.Axis(format='$,.0f'), scale=alt.Scale(domain=[0, max_y_value])),
        color=alt.Color('year:N', scale=color_scale, title='Year'),
        xOffset='year:N'
    ).properties(
        title='Median Spend by Industry and Year',
        width=alt.Step(100),
        height=750 
    ).configure_axis(
        labelAngle=0
    )

    st.altair_chart(chart, use_container_width=True)

           
with tab2:
    st.subheader("Churn Rate")
    st.write("Churn is defined as the percentage of customers who had an active campaign in 2022, but not in 2023.")

    colors = ['salmon', 'lightblue']

    col1, col2 = st.columns(2)

    # Plot for the first industry
    industry1 = churn_data.loc[0, 'industry']
    churned_rate1 = churn_data.loc[0, 'churned']
    non_churned_rate1 = 1 - churned_rate1
    labels1 = ['Churned', 'Non-Churned']
    sizes1 = [churned_rate1, non_churned_rate1]
    pie_data1 = pd.DataFrame({
        'Status': labels1,
        'Rate': sizes1
    })
    fig1 = px.pie(pie_data1, names='Status', values='Rate', title=industry1, hole=0.3,  width=350, height=350)
    fig1.update_traces(marker=dict(colors=colors))

    # Plot for the second industry
    industry2 = churn_data.loc[1, 'industry']
    churned_rate2 = churn_data.loc[1, 'churned']
    non_churned_rate2 = 1 - churned_rate2
    labels2 = ['Churned', 'Non-Churned']
    sizes2 = [churned_rate2, non_churned_rate2]
    pie_data2 = pd.DataFrame({
        'Status': labels2,
        'Rate': sizes2
    })
    fig2 = px.pie(pie_data2, names='Status', values='Rate', title=industry2, hole=0.3,  width=350, height=350)
    fig2.update_traces(marker=dict(colors=colors))

    # Display charts in columns
    with col1:
        st.plotly_chart(fig1)
    with col2:
        st.plotly_chart(fig2) 
        

st.write("--------------------------------------")
    
st.subheader("Analysis 1 Key Learnings:")
st.write("- Transportation campaigns, Despite a larger budget cut, transportation campaigns retained their audience better, exhibiting a lower churn rate. This suggests a higher level of client satisfaction with the performance of these campaigns.")
st.write("- Although robotics campaigns experienced a smaller budget reduction, they struggled more with audience retention, with a higher churn rate. This indicates lower client satisfaction compared to transportation campaigns.")
st.write("- Overall, transportation campaigns appear slightly more stable, but the significant budget cuts raise concerns about their future performance and continued client satisfaction.")

st.write("--------------------------------------")