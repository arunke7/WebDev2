
# This creates the page for displaying data visualizations.

import streamlit as st
import json
import pandas as pd
import altair as alt
infile=open("data.json")
data=json.load(infile)
infile.close()
coffeedata=pd.DataFrame(data["data_points"])

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Coffee Data",
    page_icon="📈",
)

# PAGE TITLE
st.title("Data Visualizations 📈")


# PART 1: GRAPHS FROM data.json
# --- YOUR CODE GOES HERE ---
st.subheader("Coffee Around the World")
st.bar_chart(data=coffeedata,x="Coffee Type", y="Number of Countries Most Popular")



st.subheader("Coffee Chains Across the U.S.")
numshops=st.slider("Select Number of Shops to Display", min_value=1, max_value=5)
coffeeshop=(data["coffee_shops"][:numshops])
vega_lite_chart= {
    "mark": {"type": "bar"},
    "encoding":{
    "x":{
        "field":"US_Locations",
        "type":"quantitative",
        "title":"Number of U.S. Locations"
    },
    "y":{
        "field":"Coffee_Chain",
        "type":"nominal",
        "title":"Coffee Chain",
        "sort":"-x"
        
    }
    }

    }
st.vega_lite_chart(data=coffeeshop, spec=vega_lite_chart, use_container_width=True)