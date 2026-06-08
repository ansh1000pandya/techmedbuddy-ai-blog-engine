import os
import sys

import streamlit as st

# ---------------- PATH FIX ---------------- #

CURRENT_DIR = os.path.dirname(__file__)

ROOT_DIR = os.path.abspath(
    os.path.join(CURRENT_DIR, "..")
)

sys.path.append(ROOT_DIR)

# ---------------- IMPORTS ---------------- #

from app.agents.planner_agent import (
    generate_tutorial_plan
)

from app.pipelines.blog_pipeline import (
    generate_blog
)

from app.agents.tutorial_generator_agent import (
    TutorialGeneratorAgent
)

# ---------------- SESSION STATE ---------------- #

if "tutorial_plan" not in st.session_state:
    st.session_state.tutorial_plan = None

if "selected_sections" not in st.session_state:
    st.session_state.selected_sections = []

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="TechMedBuddy AI Blog Engine",
    page_icon="🧬",
    layout="wide"
)

# ---------------- HEADER ---------------- #

st.title(
    "🧬 TechMedBuddy AI Blog Generator"
)

st.markdown(
    """
Generate research-grade blogs and
long-form educational tutorials.
"""
)

# =========================================================
# BLOG UI
# ========================================================= #

st.sidebar.header(
    "⚙️ Blog Configuration"
)

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

include_faq = st.sidebar.checkbox(
    "Include FAQ Section",
    value=True
)

generate_blog_button = st.sidebar.button(
    "🚀 Generate Blog"
)

# =========================================================
# TUTORIAL UI
# ========================================================= #

st.markdown("---")

st.subheader(
    "📘 Tutorial Generation"
)

include_tutorial = st.checkbox(
    "Enable Tutorial Mode"
)

tutorial_topic = ""
tutorial_mode = "Theory + Code"

if include_tutorial:

    tutorial_topic = st.text_area(
        "Enter Tutorial Topic",
        height=200,
        placeholder="""
Examples:

Python Data Types

Functions in Python

Loops in Python

Object Oriented Programming

Bioinformatics

Clinical Informatics

Machine Learning

Data Structures
"""
    )

    tutorial_mode = st.radio(
        "Tutorial Type",
        [
            "Theory Only",
            "Theory + Code"
        ]
    )

    st.markdown("---")

    generate_outline_button = st.button(
        "🧠 Generate Tutorial Outline"
    )

    if generate_outline_button:

        if tutorial_topic.strip() == "":

            st.warning(
                "Please enter a tutorial topic first."
            )

        else:

            with st.spinner(
                "Planner Agent Creating Outline..."
            ):

                tutorial_plan = (
                    generate_tutorial_plan(
                        tutorial_topic
                    )
                )

                st.session_state.tutorial_plan = (
                    tutorial_plan
                )

    if st.session_state.tutorial_plan:

        st.markdown("---")

        st.subheader(
            "✅ Select Sections To Include"
        )

        selected_sections = []

        for section in (
            st.session_state.tutorial_plan["sections"]
        ):

            checked = st.checkbox(
                section["title"],
                value=True
            )
            st.caption(
                section["prompt"]
            )

            if checked:

                selected_sections.append(
                    section
                )

        st.session_state.selected_sections = (
            selected_sections
        )

generate_tutorial_button = st.button(
    "📘 Generate Tutorial"
)

# =========================================================
# BLOG GENERATION
# ========================================================= #

if generate_blog_button:

    if topic.strip() == "":

        st.warning(
            "Please enter a blog topic."
        )

    else:

        with st.spinner(
            "Generating Research Blog..."
        ):

            blog = generate_blog(
                topic
            )

        st.success(
            "Blog Generated Successfully!"
        )

        st.markdown("---")

        st.subheader(
            "📝 Research Blog"
        )

        st.markdown(
            blog,
            unsafe_allow_html=True
        )

# =========================================================
# TUTORIAL GENERATION
# ========================================================= #

if generate_tutorial_button:

    if tutorial_topic.strip() == "":

        st.warning(
            "Please enter a tutorial topic."
        )

    elif (
        len(st.session_state.selected_sections)
        == 0
    ):

        st.warning(
            "Please generate an outline and select at least one section."
        )

    else:

        with st.spinner(
            "Generating Long-Form Tutorial..."
        ):

            generator = (TutorialGeneratorAgent())
            tutorial = (generator.generate_tutorial(
                tutorial_title=
                st.session_state
                .tutorial_plan["tutorial_title"],
                selected_sections=
                st.session_state
                .selected_sections
            )
            )
            
                
            

        st.success(
            "Tutorial Generated Successfully!"
        )

        
        

# =========================================================
# FOOTER
# ========================================================= #

st.markdown("---")
st.subheader("📘 Tutorial")
st.markdown(tutorial, unsafe_allow_html=True)
print("\nTUTORIAL OUTPUT:")
print(type(tutorial))
print(tutorial[:])

st.caption(
    "Powered by TechMedBuddy AI Engine"
)