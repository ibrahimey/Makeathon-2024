import streamlit as st
from model import model

st.title("ElectroBotto")

with open("prompt.txt", "r") as file:
    system_prompt = file.read()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt},
                                 {"role": "assistant", "content": "Hi! I'm ElectroBotto, I'm here to find the best Mercedes-Benz electric car for you! Can you tell me a bit about yourself so I can help you better?"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Your response"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    messages = st.session_state.messages

    response = model(messages)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
