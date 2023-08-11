import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout= "wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = "https://lottie.host/7021a9e3-9c3d-469d-ad61-f66dcd5f0d45/3aGbryrUyc.json"


with st.container():
    st.subheader("Hi, I am Anish :wave:")
    st.title("Software Developer")
    st.write("I am always eager to take on new challenges and expand my skillset. My GitHub profile serves as a testament to my passion for cloud computing and Java DSA, showcasing my ability to tackle complex problems and deliver high-quality solutions. I invite you to explore my repositories and witness firsthand my commitment to excellence in these areas.")
    st.write("[LeetCode>](https://leetcode.com/anish_891/) ")
    st.write("[Github>](https://github.com/anish891) ")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
             I’m looking to collaborate on Good Tech Skills
            🌱 I’m currently learning Java Development
            💬 Ask me about Coding...
            👯 Interested in Cloud Technologies...
            👯 Self Motivated
            ⚡ Quick learner
            💬 Ask me about Java, Python, AWS, Mysql, HTML, CSS, DSA, AI/ML
            📫 How to reach me: anishtejwai891@gmail.com
            """
            )
        st.write("[LinekdIn >](https://www.linkedin.com/in/anishtejwani/)")
    
    with right_column:
        st_lottie(lottie_coding, height = 300, key = "coding")


with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        #######
        with text_column:
            st.subheader("Notes Application")
        st.write(
            """
            This is a Flutter application that allows users to store and manage their notes. The app utilizes Firebase as the backend for storing and retrieving the notes.

            Features

            User Authentication: Users can create an account or log in with their existing credentials to access the app.
            Create Notes: Users can create new notes by providing a title and content for each note.
            View Notes: Users can view a list of all their notes, including the title and a preview of the content.
            Edit Notes: Users can edit the title and content of their existing notes.
            Delete Notes: Users can delete notes they no longer need.
            Real-time Sync: The app uses Firebase's real-time database to sync notes across multiple devices in real-time.
            Offline Support: Users can access and modify their notes even when they are offline. Changes will be synchronized with the backend once the device is online.
        """
        )
