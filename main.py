import time

import streamlit as st

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

def generate_response():
    response = """
    loren ipsum dolor sit amet, consectetur adipiscing elit. 
    Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    """

    for token in response.split(" "):
        time.sleep(0.1)  # Simulate delay
        yield token + " "

    return f"Echo: {user_input}"

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
    with st.chat_message("ai"):
        response_generator = generate_response()
        response = st.write_stream(response_generator)


    st.session_state.messages.append({"role": "ai", "content": response})
    
    # st.chat_message("ai").markdown(ai_response)