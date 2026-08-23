import streamlit as st
import requests

st.set_page_config(page_title="Math Solver AI", page_icon="🧮")

st.title("🧮 Class 1-12 Math Solver AI")

pass_code = st.text_input("Enter Pro Pass Code (Leave blank for Free Trial):", type="password")

question = st.text_area("अपना गणित का सवाल यहाँ लिखें:")

if st.button("Solve"):
    if pass_code == "MYPRO123" or pass_code == "":  
        if question:
            headers = {
                "Authorization": "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", 
                "Content-Type": "application/json"
            }
            data = {
                "model": "llama-3.3-70b-versatile",
                "messages": [
                    {"role": "system", "content": "You are a K-12 math solver. Solve class 1 to 12 math problems step-by-step in simple language."},
                    {"role": "user", "content": question}
                ]
            }
            
            response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=data, headers=headers)
            
            if response.status_code == 200:
                result = response.json()['choices'][0]['message']['content']
                st.success("उत्तर:")
                st.write(result)
            else:
                st.error("API में कुछ समस्या है, Key चेक करें।")
        else:
            st.warning("कृपया कोई सवाल लिखें!")
    else:
        st.error("गलत प्रो पास कोड! सही एक्सेस के लिए संपर्क करें।")
