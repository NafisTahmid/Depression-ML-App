# Loading Core Packages
import streamlit as st

# Loading EDA Packages
import pandas as pd
import sklearn

# Load Data Visualization Package
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px


# Load Data

# @st.cache_resource
def load_data(data):
    df = pd.read_csv(data)
    return df

def run_eda_app():
    st.subheader("From Exploratory Data Analysis")
    # df = pd.read_csv("data/diabetes_data_upload.csv")
    df = load_data("data/thesis_dataset_updated.csv")
    df_encoded = load_data("data/depression_cleaned_data.csv")
    freq_df = load_data("data/depression_age_data.csv")
    df_cleaned = load_data("data/depression_cleaned_data.csv")
    # st.dataframe(df)


    submenu = st.sidebar.selectbox("Submenu", ["Descriptive", "Plots"])
    if submenu == "Descriptive":
        st.dataframe(df)
        # st.dataframe(df_encoded)

        with st.expander("Data Types"):
            st.dataframe(df.dtypes)

        with st.expander("Descriptive Summary"):
            st.dataframe(df_encoded.describe())

        with st.expander("Class Distribution"):
            st.dataframe(df[ '26. At present are you suffering from any kind of depression?'].value_counts())

        with st.expander("Gender Distribution"):
            st.dataframe(df['1. What is your Gender? '].value_counts())

    elif submenu == "Plots":
        st.subheader("Plots")

        # Layouts
        col1, col2 = st.columns([2,1])

        with col1:
            with st.expander("Dist Plot of Gender"):
                # Using Seaborn
                # fig = plt.figure()
                # sns.countplot(df, x='Gender')
                # st.pyplot(fig)

                gen_df = df['1. What is your Gender? '].value_counts().to_frame()
                gen_df = gen_df.reset_index()
                gen_df.columns = ['Gender Type', 'Counts']
                # st.dataframe(gen_df)

                p1 = px.pie(gen_df, names='Gender Type', values='Counts')
                st.plotly_chart(p1, use_container_width=True)

            with st.expander("Dist Plot of Class"):
                fig = plt.figure()
                sns.countplot(data=df, x='26. At present are you suffering from any kind of depression?')
                st.pyplot(fig)

        with col2:
            with st.expander("Gender Distribution"):
                st.dataframe(gen_df)

            with st.expander("Class Distribution:"):
                st.dataframe(df['26. At present are you suffering from any kind of depression?'].value_counts())

        with st.expander("Frequency Distribution"):
            # st.dataframe(freq_df)
            p2 = px.bar(freq_df, x='2._what_is_your_age?', y='count')
            st.plotly_chart(p2)

        # Outlier Detection
        with st.expander("Outlier Detection Plot"):
            fig = plt.figure()
            sns.boxplot(data = df_cleaned, x='2._what_is_your_age?')
            st.pyplot(fig)

            p3 = px.box(df_cleaned, x='2._what_is_your_age?', color='1._what_is_your_gender?_')
            st.plotly_chart(p3)

        # Correlation
        with st.expander("Correlation Plot"):
            corr_matrix = df_encoded.corr()
            fig = plt.figure(figsize=(20,10))
            sns.heatmap(corr_matrix, annot=True)
            st.pyplot(fig)

            # p4 = px.imshow(corr_matrix)
            # st.plotly_chart(p4)