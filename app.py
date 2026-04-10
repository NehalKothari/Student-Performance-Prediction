import streamlit as st
from model import load_model, predict

st.set_page_config(page_title="Student Predictor", page_icon="🎓")

# Load model
model = load_model()

# Title
st.title("🎓 Student Performance Predictor")
st.markdown("### Predict Final Marks using AI")

st.divider()

col1, col2 = st.columns(2)

with col1:
    studytime = st.selectbox("📚 Study Time", [1,2,3,4])
    failures = st.selectbox("❌ Past Failures", [0,1,2,3])
    absences = st.slider("📅 Absences", 0, 50)
    health = st.slider("💪 Health", 1, 5)

with col2:
    freetime = st.slider("🎮 Free Time", 1, 5)
    goout = st.slider("🚶 Going Out", 1, 5)
    G1 = st.slider("📝 First Test Marks", 0, 20)
    G2 = st.slider("📝 Second Test Marks", 0, 20)

st.divider()

if st.button("🚀 Predict"):
    input_data = [studytime, failures, absences,
                  health, freetime, goout,
                  G1, G2]

    result = predict(model, input_data)

    st.success(f"🎯 Predicted Marks: {result:.2f} / 20")

    if result >= 15:
        st.info("🌟 Excellent Performance")
    elif result >= 10:
        st.info("👍 Average Performance")
    else:
        st.warning("⚠️ Needs Improvement")