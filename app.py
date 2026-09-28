'''
import streamlit as st
import ollama
st.title("Freindly AI Bot")
st.write("Ask me anything!")
question =st.text_input("Enter your question:")
if st.button("ASK AI"):
    response=ollama.chat(
        model="llama3.2",
        message=[
            {
                "role":"system";
                "content":""" 
                You are a friendly and funny AI assisant Explain things in simple language.Be helping and encouraging."""
            },
            {
                "role":"usre"
                "content":question
            }

        ]
    )
    answer=response["message"]["content"]
    st.write("AI Response")
    st.write(answer)
'''



import streamlit as st
import ollama

# CSS Styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #74ebd5, #ACB6E5);
}

h1 {
    text-align: center;
    color: #ffffff;
    font-family: Arial, sans-serif;
}

.stTextInput > div > div > input {
    background-color: white;
    color: black;
    border: 2px solid #4A90E2;
    border-radius: 10px;
    padding: 10px;
}

.stButton > button {
    width: 100%;
    background-color: #4A90E2;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px;
    font-size: 18px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #357ABD;
}

.response-box {
    background-color: white;
    color: black;
    padding: 15px;
    border-radius: 10px;
    margin-top: 15px;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# App Title
st.title("🤖 Friendly AI Bot")
st.write("Ask me anything!")

# User Input
question = st.text_input("Enter your question:")

# Button
if st.button("ASK AI"):
    if question:
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are a friendly and funny AI assistant.
                    Explain things in simple language.
                    Be helpful and encouraging.
                    """
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        answer = response["message"]["content"]

        st.markdown(
            f'<div class="response-box"><h3>AI Response</h3><p>{answer}</p></div>',
            unsafe_allow_html=True
        )

    else:
        st.warning("Please enter a question!")
