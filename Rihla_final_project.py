# I installed streamlit in the terminal
# I worked so hard on this I Hope I win
import streamlit as st
import pandas as pd
import base64

from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title = "Main menu",
        options = ["Home", "About us", "Contact Us"]

    )
if selected == "Home":
 Main_Page, GPA_Calculator = st.tabs(["Main Page", "GPA Calculator"])

 with Main_Page:
   
 
    st.title("📜 Rihla")
    st.header("From Wondering to Knowing.")

    user_name = st.text_input("What's your name?")

    if user_name:
        st.write(f"Hello {user_name}, let's help you find your dream university!")

    major_groups = [
        "Engineering",
        "Medicine & Health",
        "Sciences",
        "Business & Economics",
        "Arts & Social Sciences",
        "Education",
        "Architecture & Design",
        "Public Health & Allied",
        "Law & Sharia Studies",
        "Emerging Tech"
    ]

    group_to_submajors = {
        "Engineering": ["Electrical Engineering", "Civil Engineering", "Mechanical Engineering", "Chemical Engineering", "Petroleum Engineering", "Computer Engineering", "Cybersecurity"],
    "Medicine & Health": ["Medicine", "Dentistry", "Pharmacy", "Lab Sciences", "Physical Therapy", "Nursing", "Radiology"],
    "Sciences": ["Biology", "Physics", "Chemistry", "Mathematics", "Computer Science", "Geology", "Forensics", "GIS"],
    "Business & Economics": ["Business Administration", "Accounting", "Finance", "Marketing", "Economics", "Management Information Systems", "Operations/Supply Chain"],
    "Arts & Social Sciences": ["Arabic", "English", "French", "History", "Philosophy", "Communication", "Law", "Sociology"],
    "Education": ["Education - Math", "Education - Science", "Education - Languages", "Pedagogy", "Psychology"],
    "Architecture & Design": ["Architecture", "Interior Architecture", "Visual Design"],
    "Public Health & Allied": ["Public Health", "Community Health", "Audiology", "Occupational Therapy"],
    "Law & Sharia Studies": ["Law", "Islamic Finance", "Sharia", "Arbitration", "Quranic Studies"],
    "Emerging Tech": ["Data Science", "Artificial Intelligence", "Cybersecurity", "GIS"]
    }

    submajor_to_universities = {
        "Electrical Engineering": ["Kuwait University", "Australian University", "AUM", "Abdullah Al-Salem University", "GUST"],
    "Civil Engineering": ["Kuwait University", "Australian University", "AUM", "Abdullah Al-Salem University"],
    "Mechanical Engineering": ["Kuwait University", "Australian University", "AUM", "Abdullah Al-Salem University"],
    "Chemical Engineering": ["Kuwait University", "Abdullah Al-Salem University"],
    "Petroleum Engineering": ["Kuwait University"],
    "Computer Engineering": ["Kuwait University", "AUM", "Abdullah Al-Salem University"],
    "Cybersecurity": ["Box Hill College Kuwait (Diploma)", "Abdullah Al-Salem University"],
    "Medicine": ["Kuwait University"],
    "Dentistry": ["Kuwait University"],
    "Pharmacy": ["Kuwait University"],
    "Medical Laboratory Sciences": ["Kuwait University"],
    "Physical Therapy": ["Kuwait University"],
    "Nursing": ["College of Nursing"],
    "Radiologic Sciences": ["Kuwait University"],
    "Biology": ["Kuwait University"],
    "Physics": ["Kuwait University"],
    "Chemistry": ["Kuwait University"],
    "Mathematics": ["Kuwait University", "Abdullah Al-Salem University"],
    "Computer Science": ["Kuwait University", "GUST", "AUM", "Abdullah Al-Salem University"],
    "Geology": ["Kuwait University"],
    "Forensic Science": ["Kuwait University"],
    "GIS": ["Kuwait University"],
    "Business Administration": ["Kuwait University", "AUM", "GUST", "AU", "Abdullah Al-Salem University"],
    "Accounting": ["Kuwait University", "AUM", "GUST", "AU", "Abdullah Al-Salem University"],
    "Finance": ["Kuwait University", "AUM", "GUST", "Abdullah Al-Salem University"],
    "Marketing": ["Kuwait University", "AUM", "GUST"],
    "Economics": ["Kuwait University", "Abdullah Al-Salem University"],
    "Management Information Systems": ["Kuwait University", "Abdullah Al-Salem University"],
    "Supply Chain Management": ["Kuwait University"],
    "Arabic Language and Literature": ["Kuwait University"],
    "English Language and Literature": ["Kuwait University", "GUST"],
    "French Language": ["Kuwait University"],
    "History": ["Kuwait University"],
    "Philosophy": ["Kuwait University"],
    "Mass Communication": ["Kuwait University", "GUST"],
    "Law": ["Kuwait University"],
    "Sociology": ["Kuwait University"],
    "Education - Mathematics": ["Kuwait University"],
    "Education - Science": ["Kuwait University"],
    "Education - Languages": ["Kuwait University"],
    "Pedagogy": ["Kuwait University"],
    "Psychology": ["Kuwait University"],
    "Architecture": ["Kuwait University", "Abdullah Al-Salem University"],
    "Interior Design": ["Kuwait University"],
    "Visual Communication Design": ["Kuwait University"],
    "Public Health": ["Kuwait University"],
    "Community Health": ["Kuwait University"],
    "Audiology": ["Kuwait University"],
    "Occupational Therapy": ["Kuwait University"],
    "Islamic Finance": ["Kuwait University"],
    "Sharia and Islamic Studies": ["Kuwait University"],
    "Arbitration": ["Kuwait University"],
    "Quranic Studies": ["Kuwait University"],
    "Data Science": ["Kuwait University", "AUM", "Abdullah Al-Salem University"],
    "Artificial Intelligence": ["AUM", "Abdullah Al-Salem University"]
}

    universities_to_link = {
        "Kuwait University" : ["https://www.ku.edu.kw/"],
    "GUST" : ["https://www.gust.edu.kw/home"],
    "Abdullah Al-Salem University" : ["https://aasu.edu.kw/"],
    "AUM" : ["https://www.aum.edu.kw/"],
    "Australian University" : ["https://www.au.edu.kw/"],
    "Box Hill College Kuwait (Diploma)" : ["https://bhck.edu.kw/"]

    }

    universities_to_coords = {
        "Kuwait University": {"lat": 29.2769, "lon": 47.9323},
    "Australian College of Kuwait": {"lat": 29.2526, "lon": 48.0226},
    "GUST": {"lat": 29.2455, "lon": 48.0198},
    "Abdullah Al Salem University": {"lat": 29.2772, "lon": 47.9361},
    "American University of Kuwait": {"lat": 29.3334, "lon": 48.0724},
    "Arab Open University": {"lat": 29.2740, "lon": 47.9337},
    "Kuwait College of Science and Technology": {"lat": 29.3776, "lon": 47.8374},
    "American University of the Middle East": {"lat": 29.1730, "lon": 48.1238},
    "Box Hill College Kuwait": {"lat": 29.1506, "lon": 48.1212}
    }
# these lists took forever I am glad they work
    st.divider()
    st.title("🎓 Find Your Major and University in Kuwait")

    selected_group = st.selectbox("Choose a major group:", major_groups)

    submajors = group_to_submajors[selected_group]
    selected_submajors = st.multiselect(f"Select your preferred majors in {selected_group}:", submajors)

    if st.button("Show Universities Offering These Majors"):
        if selected_submajors:
            for major in selected_submajors:
                universities = submajor_to_universities.get(major, ["No universities found"])
                st.header(f"**{major}** is offered at:")
                for uni in universities:
                    st.write(f"- {uni}")
                    link = universities_to_link.get(uni, ["No link available"])[0]
                    st.info(f"Learn more about the university through their page: {link}")
        else:
            st.warning("Please select at least one major to see university options.")

    coords_df = pd.DataFrame([
        {'University': uni, 'lat': data['lat'], 'lon': data['lon']}
        for uni, data in universities_to_coords.items()
    ])
    st.divider()
    st.title("🎓 University Locations in Kuwait")
    st.map(coords_df)
    st.warning("We would love your feedback:")
    st.feedback(options="stars", key=None, disabled=False, on_change=None, args=None, kwargs=None)
 with GPA_Calculator: 
   st.title("📱 GPA Calculator")
   Percentage = st.number_input("Enter your Highschool Percentage")
   GPA = ({Percentage*4/100})
   st.success(f"your GPA {GPA}")
   st.caption("to the nearest hundredths")

if selected == "About us":
     
  
     st.title("🧭 About Rihla")

     st.info("At Rihla, we believe every student’s journey is unique."
     " Inspired by the Arabic word for “journey,” Rihla guides you from "
      "curiosity to clarity, helping you explore, discover, and reach " 
      "the university that truly fits your dreams.")
     st.info("We help you find the Universities that offer your dream major, to make your application process easier")
     st.divider()
     st.info("🎓 Did you know? The word *'Rihla'* was used by Ibn Battuta to describe his travels across the world.")
 

if selected == "Contact Us":
     
     st.header("📩 Contact Us")
     with st.form(key="contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send")

        if submit:
            if name and email and message:
                
                st.success(f"Thank you, {name}! We have received your message and will get back to you soon.")
            else:
                st.error("Please fill out all fields before sending.")

#Congrats on getting to the end



   
