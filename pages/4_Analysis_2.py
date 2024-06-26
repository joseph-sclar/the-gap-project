import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



import plotly.figure_factory as ff

st.title("Analysis 2")





data = pd.read_csv("data/data_anonymized.csv")



st.header("**Are the Differences in Performance Inherent to Industry Characteristics or Is There More?**")
st.write("In this analysis we are comparing key performance metrics between video marketing campaigns in transportation and robotics. We are using image campaigns as a benchmark, so we can evaluate the effectiveness of video campaigns relative to their image-based counterparts.")
st.write("By calculating the ratio of these metrics (Image Campaigns / Video Campaigns), we can determine which campaign type performs better.")
st.write("This approach helps us understand if performance differences are due to the type of campaign or the industry. Similar ratios across industries suggest the campaign type is the main factor, while differing ratios indicate industry context is also important.")

metrics = ['Summary', 'CTR', 'CR', 'AOV', 'CPC', 'CPO', 'ROI' ]

metric = st.selectbox("Select Metric to Plot", metrics)


if metric == 'Summary':
    
# Plotting
    st.subheader("Ratio Difference Comparison of Metrics")
    st.write("Here we can see a plot comparing the performance of Image Campaigns to Video Campaigns in the Robotics and Transportation industries. Bars that are closer to each other suggest that the type of campaign is the main factor influencing performance, while bars that are further apart indicate that the industry has a bigger impact.")
    st.write("The ratios are calculated using the formula:")
    st.latex(r'\text{Ratio} = \frac{\text{Metric Image Campaigns}}{\text{Metric Video Campaigns}}')
    
    
    
    ratios_df = pd.read_csv("data/ratios.csv")
    
    ratios_melted = pd.melt(ratios_df, id_vars='industry', var_name='metric', value_name='ratio')
    
    fig, ax = plt.subplots(figsize=(12, 8))

    sns.barplot(
        x='metric', 
        y='ratio', 
        hue='industry', 
        ci=None,
        data=ratios_melted,
        edgecolor='.2', 
        linewidth=1.5, 
        saturation=1,
        palette='pastel',  
        ax=ax
    )

    # Enhancing plot titles and labels for clarity
    ax.set_title('Metric Ratios by Industry (Log Scale)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Ratio (Log Scale)', fontsize=12)
    ax.set_xlabel('Metric', fontsize=12)
    ax.tick_params(axis='x', rotation=45) 
    ax.legend(title='Industry', frameon=True, shadow=True)

    # Set log scale for y-axis
    ax.set_yscale('log')

    st.pyplot(fig)
    
    st.write("The plot above shows the ratios of key performance metrics between Image Campaigns and Video Campaigns in the Robotics and Transportation industries. A ratio above 1 indicates that Image Campaigns outperform Video Campaigns in that metric, while a ratio below 1 suggests the opposite. The log scale helps visualize the differences more clearly.")
    st.write("Deep dive into the metrics:")
    
    tabs = ["CTR", "CR", "AOV", "CPC", "CPO", "ROI"]
    
    metric_def = [
        "**Click-Through Rate (CTR)**: measures the percentage of users who clicked on an ad after seeing it. A higher CTR indicates better engagement with the ad.",
        "**Conversion Rate (CR)**: measures the percentage of users who completed a desired action after clicking on an ad. A higher CR indicates better conversion efficiency.",
        "**Average Order Value (AOV)**: measures the average value of orders placed by customers. A higher AOV indicates higher purchase value.",
        "**Cost Per Click (CPC)**: measures the cost of each click on an ad. A lower CPC indicates more cost-effective clicks.",
        "**Cost Per Order (CPO)**: measures the cost of acquiring a customer. A lower CPO indicates more cost-effective customer acquisition.",
        "**Return on Investment (ROI)**: measures the profitability of a marketing campaign. A higher ROI indicates better returns on investment."
    ]
    
    content = [
        "The difference is consistent across both industries, suggesting that the inherent characteristics of Image Campaigns make them more engaging, rather than industry-specific factors.",
        "The vast difference suggests that Image Campaigns are exceptionally more effective in driving conversions in the Transportation industry. This performance gap likely reflects industry-specific factors, such as customer behavior and purchasing patterns in the Transportation sector.",
        "The similarity in AOV ratios indicates that the type of campaign (Image vs. Video) does not significantly affect the average order value within either industry. This metric's performance can be explained by the inherent characteristics of the industry, as both industries show negligible differences.",
        "The higher CPC for Image Campaigns suggests that clicks are more expensive for Image Campaigns, irrespective of the industry. This performance gap is largely due to the type of campaign rather than industry-specific factors.",
        "The lower CPO ratio indicates that Image Campaigns are more cost-effective in driving orders. The more pronounced difference in Transportation suggests that this industry benefits more from Image Campaigns, reflecting both the campaign type and industry-specific cost dynamics.",
        "The high ROI ratios indicate that Image Campaigns provide better returns. The exceptionally high ROI in Transportation suggests that industry-specific factors, such as higher profit margins or more effective marketing strategies, contribute to this performance gap."
    ]

    # Create tabs
    for i, tab in enumerate(st.tabs(tabs)):
        with tab:
            st.write(metric_def[i])
            st.write(content[i])
    
else:
    
    st.subheader(f"{metric} Comparison Across Industries")
    
    st.write(f"Here we can see a plot comparing the performance of {metric} in the Robotics and Transportation industries for Image and Video Campaigns. The log scale is used to better visualize the differences in performance.")

    fig, ax = plt.subplots(figsize=(10, 6))

    # Creating a bar plot to compare metrics between Industry R and Industry T
    sns.barplot(
        x='campaign_type', 
        y=metric, 
        hue='industry', 
        ci=None,
        data=data,
        edgecolor='.2', 
        linewidth=1.5, 
        saturation=1,
        palette='pastel',  
        ax=ax
    )

    # Enhancing plot titles and labels for clarity
    ax.set_title(f'Comparison of {metric} Across Industries', fontsize=14, fontweight='bold')
    ax.set_ylabel(metric, fontsize=12)
    ax.set_xlabel('campaign_type', fontsize=12)
    ax.tick_params(axis='x', rotation=45) 
    ax.legend(title='Industry', frameon=True, shadow=True)

    ax.set_yscale('log')

    ax.set_ylabel(f'{metric} (log scale)', fontsize=12)

    st.pyplot(fig)



    fig, ax = plt.subplots(figsize=(10, 6))



    if metric == 'CTR':
        st.write("Robotics outperforms Transportation in CTR for both Image and Video Campaigns, indicating that ads in the Robotics industry attract more clicks than those in Transportation.")
    elif metric == 'CR':
        st.write("Robotics has a higher CR for both Image and Video Campaigns, meaning clicks in the Robotics industry are more likely to convert into actions compared to Transportation.")
    elif metric == 'AOV':
        st.write("Transportation has a significantly higher AOV for both campaign types, suggesting that purchases in the Transportation industry are of much higher value than in Robotics.")
    elif metric == 'CPC':
        st.write("Robotics benefits from a lower CPC for both Image and Video Campaigns, making it cheaper to drive clicks in the Robotics industry.")
    elif metric == 'CPO':
        st.write("Robotics shows a much lower CPO for both campaign types, indicating it is more cost-effective to acquire customers in the Robotics industry compared to Transportation.")
    elif metric == 'ROI':
        st.write("For Image Campaigns, Transportation achieves higher profitability, but Robotics performs better in terms of ROI for Video Campaigns. This indicates that Image ads are more profitable in Transportation, while Video ads yield better ROI in Robotics.")

st.write("--------------------------------------")
    
st.subheader("Analysis 2 Key Learnings:")

st.write("- The data suggests that industry-specific factors significantly impact campaign performance. Transportation campaigns show higher CR ratios and ROI compared to Robotics, indicating better conversion rates and returns. These differences highlight the need for tailored product development to optimize campaigns for each industry, ensuring strategies are aligned with the unique characteristics and behaviors of the target market within each sector.")
st.write("- Robotics generally performs better in user engagement, conversion efficiency, and cost-effectiveness across both Image and Video Campaigns. However, Transportation excels in average order value and profitability for Image Campaigns, though it struggles with Video Campaigns. This highlights that while Robotics is more effective and cost-efficient overall, Transportation can achieve higher value and profitability under certain conditions.")
    
st.write("--------------------------------------")
