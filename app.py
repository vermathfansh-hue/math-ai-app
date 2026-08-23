import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Class 1-12 Math Solver AI", page_icon="🧮")
st.title("🧮 Class 1-12 Math Solver AI")

pass_code = st.text_input("Enter Pro Pass Code (Leave blank for Free Trial):", type="password")
question = st.text_area("अपना गणित का सवाल यहाँ लिखें:")

if st.button("Solve"):
    if question.strip() == "":
        st.warning("कृपया पहले कोई सवाल लिखें!")
    else:
        try:
            api_key = st.secrets["GEMINI_API_KEY"]
            genai.configure(api_key=api_key)
            
            with st.spinner("सवाल हल किया जा रहा है..."):
                # यहाँ हमने मॉडल का नाम सीधे 'gemini-pro' सेट किया है जो Cloud/AQ वाली की के साथ काम करता है
                model = genai.GenerativeModel('gemini-pro')
                prompt = f"You are a K-12 math solver. Solve class 1 to 12 math problems step by step in clear Hinglish/Hindi. Question: {question}"
                response = model.generate_content(prompt)
                
                st.success("### समाधान (Solution):")
                st.write(response.text)
                
        except Exception as e:
            st.error(f"API में समस्या है, Secrets में GEMINI_API_KEY चेक करें! एरर: {e}")
