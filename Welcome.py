import streamlit as st


st.set_page_config(
    page_title="The Gap Project",
    page_icon="👑",
)
    
st.title("The Gap Project")    
st.subheader("Analyzing Video Marketing Campaign Performance in the Transportation and Robotics Industries")

# Divider with an emoji
st.write("---")

# Introduction with emphasis and note
st.write("""
Welcome to the **Gap Project**! In this project, we're diving into a key question:

### Is there a gap in the performance of marketing campaigns in the Transportation and Robotics industries when the campaigns only use videos as marketing content?

**Note:** For privacy reasons, we've changed the names of the industries, values and other sensitive information in this project. However, the methodology and the data proportions remains the same, and our goal is to showcase the analysis structure and approach.
""")

st.write("---")

# Divider with an emoji
st.markdown("##  Approach")

st.write("""
For this demonstration, we'll focus on two key analyses. However, it's important to note that the actual project was more extensive, involving additional steps such as data collection and cleaning, handeling outliers, univariate analysis, other multivariate analyses, and more. For the sake of brevity in this demo, we're highlighting just two analyses:
""")

st.markdown("""
1. **Client Satisfaction Comparison:** Are clients more satisfied with the performance of transportation campaigns compared to robotics?
2. **Performance Influences:** Are the differences in performance inherent to industry characteristics, or is there more to consider?
""")

st.write("---")


# Visual divider
st.markdown("## Conclusion")

# Conclusion with call-to-action
st.write("""
By systematically addressing these aspects, we'll be able to determine if there's a significant performance gap between the Transportation and Robotics industries when it comes to video-only marketing campaigns.

Let's get started and dive into the analysis!
""")


# Footer with link
st.markdown("""
---
*Project by: [Joseph Sclar](https://joseph-sclar.webflow.io/)*
""")
st.markdown("""

*Original project was done for: [Criteo](https://criteo.com)*
""")
