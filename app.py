import streamlit as st

st.set_page_config(page_title="Sample Agent Bot Voice", layout="centered")

st.markdown("# Tax Pro Agent")
st.markdown("### Powered by NMS")

# User selection for AI Agent (Male or Female)
agent_choice = st.radio("Choose Your Agent:", ("Male Agent", "Female Agent"))

# Define agent IDs
male_agent_id = "iMS7qt2kpjaFuvUgm9iY"  # Male Agent ID
female_agent_id = "np5dfEB0iRu6Vpr2zRSS"  # Female Agent ID

# Select the appropriate agent ID based on user choice
selected_agent_id = male_agent_id if agent_choice == "Male Agent" else female_agent_id

# Embed the ElevenLabs ConvAI widget using JavaScript
custom_script = f"""
    <script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>
    <elevenlabs-convai agent-id="{selected_agent_id}" style="width:100%; height:500px; display:block;"></elevenlabs-convai>
"""

st.components.v1.html(custom_script, height=500)
