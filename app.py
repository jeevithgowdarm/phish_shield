import json
import random
import streamlit as st
from phishing_detector import is_phishing

st.set_page_config(page_title="Phish Shield", page_icon="🛡️")

st.title("🛡️ Phish Shield")
facts = [
    "Phishing attacks cause over $2 billion in losses every year.",
    "Always check the sender's email before clicking a link.",
    "Real banks never ask for login info by email.",
    "Hover over links to preview where they really go.",
    "Shortened URLs can hide malicious destinations."
]

st.info(f"💡 Did you know? {random.choice(facts)}")
st.subheader("Protect Yourself from Fake Links")

url = st.text_input("🔗 Paste the suspicious link below:")

if st.button("Check Link"):
    if url:
        result = is_phishing(url)
        if result:
            st.error("🚨 This link is likely a phishing/scam site!")
        else:
            st.success("✅ This link looks safe.")
    else:
        st.warning("⚠️ Please enter a URL.")

# Awareness section
st.markdown("---")
st.markdown("### 📚 Learn About Phishing")
st.image("images/scam_vs_real.png", caption="Example: Real vs. Fake Email")
st.markdown("🔗 [Read more on Phishing.org](https://www.phishing.org)")

# Quiz placeholder
st.markdown("---")
st.markdown("### 🧠 Phishing Awareness Quiz")

# Load questions from JSON file
with open("quiz/phishing_quiz.json", "r") as f:
    quiz_data = json.load(f)

score = 0

for i, q in enumerate(quiz_data):
    st.markdown(f"**Q{i+1}: {q['question']}**")
    user_answer = st.radio("Choose one:", q["options"], key=i)

    if st.button(f"Submit Answer {i+1}", key=f"btn{i}"):
        if user_answer == q["answer"]:
            st.success("✅ Correct!")
            score += 1
        else:
            st.error(f"❌ Wrong. Correct answer: {q['answer']}")

    # Show final score only if any answers were submitted
if st.button("Show Final Score"):
    st.success(f"🎯 You scored {score} out of {len(quiz_data)}")


st.markdown("---")
st.info("Note: This quiz does not store your total score yet. Score tracking feature coming soon.")
st.markdown("---")
st.markdown("### 🔍 Real-Time Link Scanner")

user_url = st.text_input("Enter a URL to check if it's suspicious")

if user_url:
    suspicious_keywords = ["login", "verify", "update", "secure", "account", "banking"]
    if any(word in user_url.lower() for word in suspicious_keywords):
        st.error("⚠️ Warning: This URL may be suspicious.")
    else:
        st.success("✅ This URL looks safe (based on basic keyword check).")


