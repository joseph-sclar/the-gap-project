import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



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
    st.subheader("Median Spend in 2022 vs 2023")
    st.write("Highlights of the trend changes in median spending between 2022 and 2023 across industries.")
    
    col1, col2 = st.columns(2)
    with col1:
        transportation_difference = f"${churn_data.loc[0, 'median spend difference']:,.0f}"
        st.metric(label="Transportation", value=transportation_difference)
    with col2:
        robotics_difference = f"${churn_data.loc[1, 'median spend difference']:,.0f}"
        st.metric(label="Robotics", value=robotics_difference)
        
    
    
    fig, ax = plt.subplots()
    churn_data.plot(kind='bar', x='industry', y=['2022 median spend', '2023 median spend'], ax=ax)
    ax.set_title('Median Spend in 2022 vs 2023')
    ax.set_ylabel('Median Spend')
    ax.get_yaxis().set_major_formatter(
        plt.FuncFormatter(lambda x, loc: "${:,}".format(int(x)))
    )
    st.pyplot(fig)


        
with tab2:
    st.subheader("Churn Rate")
    st.write("Churn is defined as the percentage of customers who had an active campaign in 2022, but not in 2023.")

    # Create two columns
    col1, col2 = st.columns(2)

    # Plot for transportation in the first column
    with col1:
        fig1, ax1 = plt.subplots()
        industry1 = churn_data.loc[0, 'industry']
        churned_rate1 = churn_data.loc[0, 'churned']
        non_churned_rate1 = 1 - churned_rate1
        labels1 = ['Churned', 'Non-Churned']
        sizes1 = [churned_rate1, non_churned_rate1]
        ax1.pie(sizes1, labels=labels1, autopct='%1.1f%%', startangle=90)
        ax1.set_title(f'{industry1}')
        st.pyplot(fig1)

    # Plot for robotics in the second column
    with col2:
        fig2, ax2 = plt.subplots()
        industry2 = churn_data.loc[1, 'industry']
        churned_rate2 = churn_data.loc[1, 'churned']
        non_churned_rate2 = 1 - churned_rate2
        labels2 = ['Churned', 'Non-Churned']
        sizes2 = [churned_rate2, non_churned_rate2]
        ax2.pie(sizes2, labels=labels2, autopct='%1.1f%%', startangle=90)
        ax2.set_title(f'{industry2}')
        st.pyplot(fig2)     
        

st.write("--------------------------------------")
    
st.subheader("Analysis 1 Key Learnings:")
st.write("- Transportation campaigns, Despite a larger budget cut, transportation campaigns retained their audience better, exhibiting a lower churn rate. This suggests a higher level of client satisfaction with the performance of these campaigns.")
st.write("- Although robotics campaigns experienced a smaller budget reduction, they struggled more with audience retention, with a higher churn rate. This indicates lower client satisfaction compared to transportation campaigns.")
st.write("- Overall, transportation campaigns appear slightly more stable, but the significant budget cuts raise concerns about their future performance and continued client satisfaction.")

st.write("--------------------------------------")