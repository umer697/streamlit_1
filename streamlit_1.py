# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 14:12:57 2024

@author: Admin
"""

import streamlit as st
import pandas as pd
import seaborn as sns

# 1 Title and subheader
st.title("Data Analysis")
st.subheader("Data Analysis using Python and Streamlit")

# 2 upload dataset

upload = st.file_uploader("Upload Your Dataset(in csv)")
if upload is not None:
    df=pd.read_csv(upload)
    
# 3 show Dataset
if upload is not None:
    if st.checkbox("3_Preview Dataset"):
        if st.button("head"):
            st.write(df.head())
        if st.button("Tail"):
            st.write(df.tail())

#4. Check DataType of Each Column
if upload is not None:
    if st.checkbox("4_DataType of Each Column"):
        st.text("DataTypes")
        st.write(df.dtypes)
        
#5. Find Shape of Our Dataset (Number of Rows And Number of Columns)
if upload is not None:
    data_shape=st.radio("5_What Dimension Do You Want To Check?",('Rows', 'Columns'))
    if data_shape=='Rows':
        st.text("Number of Rows")
        st.write(df.shape[0])
    if data_shape=='Columns':
        st.text("Number of Columns")
        st.write(df.shape[1])
        
           
        
#6. Find Null Values in The Dataset
if upload is not None:
    test=df.isnull().values.any()
    if test==True:
        if st.checkbox("Null Values in the dataset"):
            sns.heatmap(df.isnull())
            st.pyplot()
#following line removes the error in the strealit window
            st.set_option('deprecation.showPyplotGlobalUse', False)
    else:
        st.success("Congratulations!!!,No Missing Values")
        
        
#7. Find Duplicate Values in the dataset        
if upload is not None:
    test=df.duplicated().any()
    if test==True:
        st.warning("This Dataset Contains Some Duplicate Values")
        dup=st.selectbox("Do You Want to Remove Duplicate Values?", \
                         ("Select One","Yes","No"))
        if dup=="Yes":
            df.drop_duplicates()
            st.text("Duplicate Values are Removed")
        if dup=="No":
            st.text("Ok No Problem")
        
#5. Fisnd Shape of Our Dataset (Number of Rows And Number of Columns)
if upload is not None:
    data_shape=st.radio("5_What Dimension Do You Want To Check?",('Rows2', 'Columns2'))
    if data_shape=='Rows2':
        st.text("Number of Rows")
        st.write(df.shape[0])
    if data_shape=='Columns2':
        st.text("Number of Columns")
        st.write(df.shape[1])
        
# 8. Get Overall Statistics
if upload is not None:
    if st.checkbox("Summary of The Dataset"):
        st.write(df.describe(include='all'))
        
#9. About Section

if st.button("About App"):
    st.text("Built With Streamlit")
    st.text("Thanks To Streamlit")       
        
#10. By
if st.checkbox("By"):
    st.success("Umer Farooq")       
        
        
if st.button("Save DataFrame"):
    open('data_streamlit.csv', 'w').write(df.to_csv("C:\\Users\\Admin\\Desktop\\Pandas\\Streamlit\\saved_files\\file_1.csv"))

    st.text("Saved To local Drive")
        
        