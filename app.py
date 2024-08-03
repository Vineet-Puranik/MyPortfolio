from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu


st.set_page_config(page_title = "Vineet Puranik's Portfolio", page_icon=":memo:",layout = "wide")
##page_icon is an emoji & layout sets the page to wide view

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Using Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

##Creating an Option Menu
#    selected= option_menu(
#        menu_title = None,
#        options = ["", "", ""],
#        icons = ["house", "book", "envelope"],
#        menu_icon = "cast",
#        default_index=0,
#    orientation="horizontal",
    #styles={
    #    "container": {"padding": "0!important", "background-color": "#fafafa"},
    #    "icon": {"color": "orange", "font-size": "25px"}, 
    #    "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
    #    "nav-link-selected": {"background-color": "green"},
    #}
#)

local_css("style/style.css") 
##Load Assets
lottie_coding = "https://lottie.host/cd5987ee-8f0d-480b-b017-c7326f7665b2/0LRTKOcAM4.json"
img_org_form = Image.open("images/findmyorg.png")
img_website = Image.open("images/mywebsite.png")
tex_longhorns = Image.open("images/texlonghorns.png")
img_anvil = Image.open("images/imganvil.png")
enovis_img = Image.open("images/enovis.png")
obe = Image.open("images/obe.png")
calculator= Image.open("images/calculator.png")
##header section
with st.container():
    st.markdown("""
    <style>
    .custom-subheader {
        font-size: 50px; 
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<h2 class="custom-subheader">Hi, I\'m Vineet!</h2>', unsafe_allow_html=True)
    image_url = tex_longhorns  
    st.markdown("""
    <style>
    .custom-title {
        font-size: 35px; 
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns([2,3]) 
    with col1:
        st.markdown('<h2 class="custom-title">A current junior studying MIS at UT Austin!</h2>', unsafe_allow_html=True)
        #st.title("A current junior studying MIS at UT Austin!")
    with col2:
        st.image(image_url, width=80)  
    st.write("Welcome to my website! Dive into my journey of blending modern technology and design. This summer, I'm on a mission to create and launch a standout product.")
    st.markdown("[Check out my LinkedIn!](https://www.linkedin.com/in/vineet-puranik/)")

#What I Do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About me!")
        st.write("#####")
        st.write(
            """
            I'm an aspiring product manager with innovative ideas and a strong work ethic.\n
            As a student at the University of Texas at Austin, I am engaged in a variety of extracurriculars, leadership and volunteering oppurtunities, and projects
            - FindMyOrg.com
            - The Texas Rocket Engineering Laboratory
            - The Undergraduate Business Council
            - Project Advance Austin
            - The Austin Public Library
            - Citizens for Animal Protection Houston
            """
        )
        st.markdown("[Check out my Resume>](https://docs.google.com/document/d/1p1GkDCL2HJWm_qMQkU41XXNCc3-vpcQBPbZ6HF2QckQ/edit?usp=sharing)")
    with right_column:
        st_lottie(lottie_coding, height = 300, key = "coding")
## --- Projects ---
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("####")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_org_form)
    with text_column:
        st.subheader("FindMyOrg.com")
        st.write(
            """
             Just got to campus? Are you overwhelmed by the shear amount of organizations on campus?\n
             FindMyOrg is a web application that consolidates campus organizations in order to help you find your home on the 40 acres.\n
             Check out the website, and receive a curated list of organizations based on our demands.
             Explore the organizations of your dreams right from your room!
            """
        )
        st.markdown("[Explore FindMyOrg!](https://findmyorg.com/)")
    with st.container():
        image_column, text_column = st.columns((1,2))
    with image_column:
        with image_column:
            st.image(img_website)
        with text_column:
            st.subheader("My Portfolio")
            st.write(
                """
                Want to create your website! Trial and Error.\n
                Perfection take time. Use streamlit, the open-source python framework, to build and deliver an interactive data app. \n
                Follow this source code to develop a website for your  business, blog, portfolio, or any other purpose!
                """
            )
            st.markdown("[Take a look the code...](https://github.com/Vineet-Puranik/My-Projects/blob/main/app.py)")
    with st.container():
        image_column, text_column = st.columns((1,2))
    with image_column:
        with image_column:
            st.image(img_anvil)
        with text_column:
            st.subheader("My First Website")
            st.write(
                """
                In my sophomore year, I had the oppurtunity to create a website with the use of the python-based web app builder: Anvil.\n
                I experimented with an interactive google maps display, database functions, buttons, comment boxes, and images. \n
                The purpose of the website was to show the audience pictures of Oak Trees in UT's West Campus.
                """
            )
            st.markdown("[Check the website out>](https://vineetpuranik.anvil.app)") 
            st.markdown("[The Code!](https://github.com/Vineet-Puranik/My-First-Website)")
    with st.container():
        image_column, text_column = st.columns((1,2))
    with image_column:
        with image_column:
            st.image(obe)
        with text_column:
            st.subheader("Building dashboards with Microsoft PowerBI")
            st.write(
                """
                In the summer of 2024, I had the chance to refine my technical experience with Power BI.\n
                Oldcastle BuildingEnvelope delivers advanced glazing and architectural solutions, with a market cap of approximately $2 billion.\n
                As a product management intern at OBE, I worked on the architectural window lineup. To make the data-centric role of our PM's easier, I came up with a dashboard. \n
                This platform is designed to identify and compare products from OBE and its competitors based on specific performance specifications.                
                """
            )
            st.markdown("[Test the dashboard out>](https://github.com/Vineet-Puranik/My-Projects/blob/main/OBE.pbix)") 
        with st.container():
        image_column, text_column = st.columns((1,2))
    with image_column:
        with image_column:
            st.image(calculator)
        with text_column:
            st.subheader("Making a functional calculator with JavaScript, CSS, and HTML")
            st.write(
                """
                I created a calculator app to investigate how modern digital calculators are programmed!\n
                By using HTML, I was able to test the calculatoor via a local server.\n
                I added the ability to input keyboard characters as well the choice to physically click on the various buttons.           
                """
            )
            st.markdown("[Calculator Code!>](https://github.com/Vineet-Puranik/CalculatorApp)") 
#Letters of Recommendation

with st.container():
    st.write("---")
    st.header("Words from my colleagues")
    st.write("####")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(enovis_img)
    with text_column:
        st.subheader("Enovis")
        st.write(
            """
             - From June 2023 to August 2023, I had the  opportunity of working as product management intern at Enovis.\n
             - Enovis is a leading provider of advanced medical technology and orthopedic solutions, dedicated to improving patient outcomes, with a market capitalization of approximately $3.5 billion.\n
             - During my internship, I worked primarily for the Upper Extremity Team, aiming to improve the product visibility of our AltiVate Anatomic product lineup. 
            """
        )
        st.markdown("[Letter of Recommendation | Brent Lloyd - Sr. Director of Medical Education](https://drive.google.com/file/d/1b0t-rPSNoePYF4HIZ09eVnc2Y2nAmhJq/view?usp=sharing)")    

## Contact 

with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("####")

    contact_form = """
     <form action="https://formsubmit.co/vineetpuranik@gmail.com" method="POST">
        <input type = "hidden" name = "_captcha" value = "false">
        <input type="text" name="name" placeholder= "Your name" required>
        <input type="email" name="email" placeholder = "Your email" required>
        <textarea name = "message" placeholder = "Your message here" required></textarea>
        <button type="submit">Send</button>
     </form>  
     """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
