import streamlit as st





# ---------------------- Page Configuration ----------------------
st.set_page_config(page_title="Mediwise", page_icon="🩺", layout="centered")

# ---------------------- Sidebar Navigation ----------------------
st.sidebar.title("🩺 Mediwise Navigation")
selected = st.sidebar.radio("Go to", ["🏠 Home", "📖 About", "🧪 Services", "📞 Contact"])

# ---------------------- Welcome/Home ----------------------
if selected == "🏠 Home":
    st.title("Hello, Welcome to Mediwise 👨‍⚕️")
    st.subheader("Your Intelligent Healthcare Companion")
    st.write("We provide smart and reliable tools to assist medical professionals and patients alike.")
    
    

    st.markdown("""
        #### Features:
        - Symptom Checker
        - Appointment Scheduling
        - Patient History Dashboard
        - AI-powered Health Predictions
    """)
    st.success("Explore from the navigation bar to learn more.")
    
    # data (latitude and longitude) for DSCSITSC
   
    import pandas as pd

    data = pd.DataFrame({
        'lat': [22.61888108086453],
        'lon': [88.40462144986203]
    
})

    # Create 3 columns, put the map in the middle one
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.title("📍 Our location")
        st.map(data)

# ---------------------- About ----------------------
elif selected == "📖 About":
    

    
    # ---------------------- About Section ----------------------
    st.header("About Mediwise")
    
    st.markdown("""
    **Mediwise** is a smart healthcare application aimed at enhancing **accessibility** and **efficiency** in healthcare delivery.
    
    Our platform is designed with **simplicity** and **security** in mind, supporting both **patients** and **practitioners** through:
    
    - 🤖 **AI-powered diagnostics**
    - 📁 **Medical record management**
    - 📅 **Easy scheduling systems**
    - 📡 **Remote monitoring tools**
    
    ---
    
    ## 🎨 <span style='color:red;'>Credits</span>
    ### Meet the team behind Mediwise:
    """, unsafe_allow_html=True)
    
    # ---------------------- Credits Without Images ----------------------
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background-color:#ffe6e6; padding:15px; border-radius:10px; margin-bottom:10px'>
            <h5 style='text-align:center; color:#800000;'>Arijit Chowdhury</h5>
            <p style='text-align:center;'>Data Scientist</p>
        </div>
    
        <div style='background-color:#e6f7ff; padding:15px; border-radius:10px; margin-bottom:10px'>
            <h5 style='text-align:center; color:#005580;'>Debarati Chaudhuri</h5>
            <p style='text-align:center;'>UI/UX Designer</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background-color:#fff0b3; padding:15px; border-radius:10px; margin-bottom:10px'>
            <h5 style='text-align:center; color:#806000;'>Joymalya Dey</h5>
            <p style='text-align:center;'>Backend Engineer</p>
        </div>
    
        <div style='background-color:#e6ffe6; padding:15px; border-radius:10px; margin-bottom:10px'>
            <h5 style='text-align:center; color:#006600;'>Sayan Sadhu</h5>
            <p style='text-align:center;'>AI Developer</p>
        </div>
        """, unsafe_allow_html=True)
    
    # ---------------------- Closing Line ----------------------
    st.markdown("""
    ---
    > *Empowering smarter health decisions through technology.*
    """)
    
    
    
            
    



# ---------------------- Services ----------------------
elif selected == "🧪 Services":
    st.header("Our Services")
    st.write("""
    ### 🔍 Symptom Checker
    Enter your symptoms and get smart AI-based predictions.

    ### 📅 Appointment Scheduling
    Seamless doctor-patient booking experience.

    ### 📂 Health Record Management
    Keep all health records safe and accessible.

    ### 📊 Health Analytics
    Visual dashboards and statistics for better insight.
    """)
    st.success("More coming soon...")

# ---------------------- Contact ----------------------
elif selected == "📞 Contact":
    st.header("Contact Us")
    st.write("Feel free to reach out to us for feedback, collaboration or support.")

    with st.form(key='contact_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send")

        if submit:
            st.success(f"Thanks {name}, we received your message!")
            


