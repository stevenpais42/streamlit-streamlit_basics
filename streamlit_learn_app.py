import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

#Display texts with Streamlit
st.write("Hello ,let's learn how to build a streamlit app together")

st.title ("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

#Display an image

st.image("i_love_streamlit.jpg")

#Input widgets

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)

st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

#Display progress and status with Streamlit

st.balloons()

st.subheader("Progress bar")
st.progress(10)

st.subheader("Wait for the execution")
with st.spinner('Wait for it...'):    
    time.sleep(10)

st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)


import streamlit as st
import pandas as pd
import numpy as np
df= pd.DataFrame(    np.random.randn(10, 2),    columns=['x', 'y'])
st.line_chart(df)

import streamlit as st
import datetime

st.title("Form for the Users")
st.write("Here, you can answer to some questions in this form.")

user_id = st.text_input("ID", value="Your ID", max_chars=7)
info = st.text_area("Share some information about you", "Put information here",
                    help='You can write about your hobbies or family')
age = st.number_input("Age", min_value=18, max_value=100, step=1)

smoke = st.checkbox("Do you smoke?")
genre = st.radio("Which movie genre do you like?",
                 options=['horror', 'adventure', 'romantic'])
weight = st.slider("Choose your weight", min_value=40., max_value=150., step=0.5)
physical_form = st.selectbox("Select level of your physical condition",
                             options=["Bad", "Normal", "Good"])
colors = st.multiselect('What are your favorite colors',
                        options=['Green', 'Yellow', 'Red', 'Blue', 'Pink'])
image = st.file_uploader("Upload your photo", type=['jpg', 'png'])

col1, col2 = st.columns(2)
with col1:
    st.image("https://static.streamlit.io/examples/cat.jpg", width=300)
    st.button("Like cats")
with col2:
    st.image("https://static.streamlit.io/examples/dog.jpg", width=355)
    st.button("Like dogs")

submit = st.button("Submit")

if submit:
    st.write("You submitted the form")

click = st.sidebar.button('Click me!')
if click:
    st.sidebar.write("You clicked the button")