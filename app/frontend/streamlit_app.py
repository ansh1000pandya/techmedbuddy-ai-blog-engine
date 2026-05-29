import streamlit as st

from app.pipelines.blog_pipeline import generate_blog


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="TechMedBuddy AI Blog Engine",
    page_icon="🧬",
    layout="wide"
)

# ---------------- HEADER ---------------- #

st.title("🧬 TechMedBuddy AI Blog Generator")
st.markdown(
    "Generate research-grade AI healthcare blogs automatically."
)

# ---------------- SIDEBAR ---------------- #

st.sidebar.header("⚙️ Blog Configuration")

topic = st.sidebar.text_input(
    "Enter Blog Topic",
    placeholder="AI in Personalized Medicine"
)

audience = st.sidebar.selectbox(
    "Target Audience",
    [
        "Researchers",
        "Medical Students",
        "Healthcare Professionals",
        "General Audience"
    ]
)

writing_style = st.sidebar.selectbox(
    "Writing Style",
    [
        "Research",
        "Professional",
        "Educational",
        "Humanized"
    ]
)

blog_length = st.sidebar.selectbox(
    "Blog Length",
    [
        "Short",
        "Medium",
        "Long"
    ]
)

include_references = st.sidebar.checkbox(
    "Include References",
    value=True
)

include_images = st.sidebar.checkbox(
    "Include Images",
    value=True
)

include_faq = st.sidebar.checkbox(
    "Include FAQ Section",
    value=True
)

generate_button = st.sidebar.button("🚀 Generate Blog")

# ---------------- MAIN GENERATION ---------------- #

if generate_button:

    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:

        with st.spinner("Generating Research Blog..."):

            full_topic = f"""
            Topic: {topic}

            Audience: {audience}

            Style: {writing_style}

            Length: {blog_length}

            Include References: {include_references}

            Include Images: {include_images}

            Include FAQ: {include_faq}
            """

            blog = generate_blog(full_topic)

        st.success("Blog Generated Successfully!")

        st.markdown("---")

        st.markdown(blog)

# ---------------- FOOTER ---------------- #

st.markdown("---")
st.caption("Powered by TechMedBuddy AI Engine")