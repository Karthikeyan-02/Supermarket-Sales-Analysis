import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import streamlit as st
from io import StringIO
import seaborn as sns

st.title("Supermarket Sales Visualizer")
df = pd.read_csv("C:\Streamlitfiles\supermarket_sales.csv")
st.header("Sales Data Analysis")

#Show dataset
if st.button("Show Dataset"):
    st.dataframe(df)

#Show data info
if st.button("Show Dataset Info"):
    # Create a buffer to capture info
    buffer = StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()
    st.text("DataFrame Info:")
    st.text(info_str)

#Show Dataset isnull
if st.button("Show Missing counts"):
    missing_df = pd.DataFrame(df.isnull().sum(), columns=["Missing Count"])
    st.dataframe(missing_df)

#Show Dataset shape
if st.button("Show Dataset Shape"):
    st.text(df.shape)

#Show Selected Columns
if "show_selector" not in st.session_state:
    st.session_state.show_selector = False

if st.button("Select Columns"):
    st.session_state.show_selector = True

if st.session_state.show_selector:
    selected = st.multiselect("Now select columns to display", df.columns, key="column_select")
    if selected:
        st.dataframe(df[selected]) 

#Show Value Counts
if "showselector" not in st.session_state:
    st.session_state.showselector = False

if st.button("Show Value Counts"):
    st.session_state.showselector = True

if st.session_state.showselector:
    select_col = st.selectbox("Select one column", df.columns, key="sel_one_column")
    if select_col:
        value_count = df[select_col].value_counts()
        st.dataframe(value_count)   

st.header("Data Visualization")

#lineplot visual
if "showselector1" not in st.session_state:
    st.session_state.showselector1 = False

if st.button("Show Lineplot", key="Lineplot"):
    st.session_state.showselector1 = True

if st.session_state.showselector1:
    select_col1 = st.selectbox("Select X-axis column (Category)", df.columns, key="col1")
    select_col2 = st.selectbox("Select Y-axis column (numeric)", df.columns, key="col2")
    if st.button("Show Chart", key="lineplot1"):
        grouped = df.groupby(select_col1)[select_col2].sum()
        plt.figure(figsize=(10, 5))
        plt.plot(grouped, color='red', linestyle='--', marker='o')
        plt.xticks(rotation=45)
        plt.title(f"{select_col2} by {select_col1}")
        plt.xlabel(select_col1)
        plt.ylabel(select_col2)
        plt.show()

    # Display in Streamlit
        st.pyplot(plt)
    
#Barplot visual
if "showselector2" not in st.session_state:
    st.session_state.showselector2 = False

if st.button("Show Barplot", key="Barplot"):
    st.session_state.showselector2 = True

if st.session_state.showselector2:
    select_col3 = st.selectbox("Select First Groupby category", df.columns, key="col3")
    select_col4 = st.selectbox("Select Second Groupby category(X-axis)", df.columns, key="col4")
    select_col5 = st.selectbox("Select numeric(Y-axis)", df.columns, key="col5")
    if st.button("Show Chart", key="Barplot1"):
        for i in df[select_col3].unique():
            temp = df[df[select_col3] == i]
            result = temp.groupby(select_col4)[select_col5].sum().sort_values()
            result.plot(kind='barh', color = 'skyblue', edgecolor = 'black')
            plt.title(f"{i}-{select_col4} groupby {select_col5}")
            plt.xlabel(select_col5, fontsize=12)
            plt.ylabel(select_col4, fontsize=12)
            plt.grid(axis = "x")
            plt.tight_layout()
            plt.show()

            # Display in Streamlit
            st.pyplot(plt)

#Boxplot
if "showselector3" not in st.session_state:
    st.session_state.showselector3 = False

if st.button("Show Boxplot", key="boxplot"):
    st.session_state.showselector3 = True

if st.session_state.showselector3:
    select_col6 = st.selectbox("Select x-axis (categorical)", df.columns, key="col6")
    select_col7 = st.selectbox("Select y-axis (numeric)", df.columns, key="col7")

    if st.button("Show Chart", key="Boxplot1"):
        # Convert Y-axis column to numeric safely
        df[select_col7] = pd.to_numeric(df[select_col7], errors="coerce")

        # Drop rows with NaN in selected columns
        boxplot_df = df[[select_col6, select_col7]].dropna()

        # Prepare data
        grp_data = [
            boxplot_df[boxplot_df[select_col6] == i][select_col7].values
            for i in boxplot_df[select_col6].unique()
        ]

        # Plot
        plt.figure(figsize=(8, 5))
        plt.boxplot(grp_data, labels=boxplot_df[select_col6].unique())
        plt.title("Boxplot")
        plt.xlabel(select_col6)
        plt.ylabel(select_col7)
        plt.show()

        # Display in Streamlit
        st.pyplot(plt)


#Pie chart
if "showselector4" not in st.session_state:
    st.session_state.showselector4 = False

if st.button("Show Pie Plot", key="Pieplot"):
    st.session_state.showselector4 = True

if st.session_state.showselector4:
    select_col8 = st.selectbox("select x-axis(Category)",df.columns,key="col8")
    Select_col9 = st.selectbox("select y-axis(Numberic)",df.columns,key="col9")

    if st.button("Show Chart",key="Pieplot1"):
        pieplot_show = df.groupby(select_col8)[Select_col9].sum()
        max_index = pieplot_show.idxmax()
        myexplode = [0.2 if i == max_index else 0 for i in pieplot_show.index]
        plt.pie(pieplot_show, labels=pieplot_show.index, autopct='%1.1f%%', startangle = 180, explode=myexplode)
        plt.title("Pieplot Calculation")
        plt.legend()
        plt.show()
    
        # Display in Streamlit
        st.pyplot(plt)

#Business Insects
st.header("Business Insects")
st.markdown("<span style='font-size:25px;'> 1️⃣ Brench wise analysis C Brench is a highest sales in last 3 months </span>",unsafe_allow_html=True)
st.markdown("<span style='font-size:25px;'> 2️⃣ The **Product line** analysis __Food and Beverages__ is the high sales in last 3 months overall *Brench and Cities*.</span>",unsafe_allow_html=True)
st.markdown("<span style='font-size:25px;'> 3️⃣ The City wise Product line of Total sales  \n"
            "-----The Home and Lifestyle product is a high sales in Yangon City.  \n"
            "-----The Food and Beverages product is a high sales in Naypyitaw City.  \n"
            "-----The Sports and Travels product get high sales in Mandalay City</span>",unsafe_allow_html=True)
st.markdown("<span style='font-size:25px;'> 4️⃣Gross Income in City wise by Product line.<br>-----Yangon - Home and Lifestyle -> high gross income.<br>-----Yangon - Health and beauty -> low gross income.<br>-----Naypyitaw - Food and Beverages -> high gross income.<br>-----Naypyitaw - Home and Lifestyle -> low gross income.<br>-----Mandalay - Sports and Travel -> high gross income.<br>-----Mandalay - Food and Beverages -> low gross income.</span>",unsafe_allow_html=True)
st.markdown("<span style='font-size:25px;'> 5️⃣This Membership card plan is working properly last 3 months the membership growth is high with the percentage 50.8%.</span>",unsafe_allow_html=True)
#st.markdown("<span style='color:red;'>This is red text</span>", unsafe_allow_html=True)
#st.markdown("[Google](https://www.geeksforgeeks.org/python/a-beginners-guide-to-streamlit/)",unsafe_allow_html=True)
st.markdown(
    """
    <div style='background-color:#f0f0f5; padding:60px; border-radius:40px;'>
        <h4 style='color:#333;'>Styled Box with Background</h4>
        <p style='color:#333;'>This is a paragraph with custom style.</p>
    </div>
    """,
    unsafe_allow_html=True
)


import mysql.connector

# Connect to MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Karthik@0704",
        database="sales_schema"
        )
    cursor = conn.cursor()

    query = "SELECT * FROM orders"
    cursor.execute(query)
    result = cursor.fetchall()

    # Get column names
    columns = [desc[0] for desc in cursor.description]
    data = pd.DataFrame(result, columns=columns)

    st.title("MySQL Data Viewer")
    st.dataframe(data)

except Exception as e:
    st.error(f"Connection failed: {e}")




