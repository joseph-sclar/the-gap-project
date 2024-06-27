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
st.markdown("## Approach")

st.write("""
For this demo, we're focusing on two main analyses from a larger project that included extensive data collection, cleaning, handling outliers, and various other analyses:
""")

st.markdown("""
1. **Client Satisfaction Comparison:** We'll compare client satisfaction levels between transportation and robotics campaigns.
2. **Performance Influences:** We'll explore whether industry-specific characteristics significantly influence campaign performance.
""")



st.write("""
Note that in the full project, we also conducted thorough data exploration, univariate and multivariate analyses, and addressed outliers among other steps. However, to keep things clear and focused in this demo, we're showcasing these two key analyses.
""")

st.write("---")

# Visual divider
st.markdown("## Conclusion")

# Conclusion with call-to-action
st.write("""
There is a clear performance gap between transporatation and robotics marketing campaigns in video campaigns, not entirely explained by industry
differences. This suggests potential for improving transporatation campaign performance.
""")


# Footer with link
st.markdown("""
---
*Project by: [Joseph Sclar](https://joseph-sclar.webflow.io/)*
""")
st.markdown("""

*Original project was done for: [Criteo](https://criteo.com)*
""")
