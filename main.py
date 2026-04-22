import streamlit as st

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

for message in st.session_state.messages:
    if message['role'] == 'user':
        st.chat_message("user").markdown(message['content'])
    else:
        st.chat_message("ai").markdown(message['content'])

user_input = st.chat_input("Type your message here...")

if user_input and user_input != "":
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    # Simulate AI response (replace with actual AI logic)
    ai_response = f"Echo: {user_input}"
    st.session_state.messages.append({"role": "ai", "content": ai_response})
    st.chat_message("ai").markdown(ai_response)