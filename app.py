import streamlit as st
import requests

st.set_page_config(page_title="Class 1-12 Math Solver AI", page_icon="🧮")

st.title("🧮 Class 1-12 Math Solver AI")

pass_code = st.text_input("Enter Pro Pass Code (Leave blank for Free Trial):", type="password")
question = st.text_area("अपना गणित का सवाल यहाँ लिखें:")

if st.button("Solve"):
    if question.strip() == "":
        st.warning("कृपया पहले कोई सवाल लिखें!")
    else:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {st.secrets['GROQ_API_KEY']}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "system", "content": "You are a K-12 math solver. Solve class 1 to 12 math problems step by step in clear Hinglish/Hindi."},
                {"role": "user", "content": question}
            ]
        }
        
        try:
            with st.spinner("सवाल हल किया जा रहा है..."):
                response = requests.post(url, headers=headers, json=data)
                res_data = response.json()
                
                if response.status_code == 200:
                    answer = res_data["choices"][0]["message"]["content"]
                    st.success("### समाधान (Solution):")
                    st.write(answer)
                else:
                    st.error("API में कुछ समस्या है, Streamlit Secrets में Key चेक करें।")
        except Exception as e:
            st.error(f"एरर आया: {e}")
