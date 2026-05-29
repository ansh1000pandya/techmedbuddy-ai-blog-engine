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

from app.pipelines.blog_pipeline import (
    generate_blog
)

from app.services.tutorial_orchestrator import (
    generate_tutorial
)

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

Machine Learning Basics

Statistics for Biology Students
"""
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

            full_topic = topic

            blog = generate_blog(
                full_topic
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

    else:

        with st.spinner(
            "Generating Long-Form Tutorial..."
        ):

            tutorial, html_path = generate_tutorial(
                tutorial_topic
            )

        # =================================================
        # SUCCESS
        # ================================================= #

        st.success(
            "Tutorial Generated Successfully!"
        )

        st.success(
            f"HTML Tutorial Exported Successfully:\n{html_path}"
        )

        # =================================================
        # DISPLAY TUTORIAL
        # ================================================= #

        st.markdown("---")

        st.subheader(
            "📘 Tutorial"
        )

        st.markdown(
            tutorial,
            unsafe_allow_html=True
        )

        # =================================================
        # DOWNLOAD BUTTON
        # ================================================= #

        with open(

            html_path,

            "r",

            encoding="utf-8"

        ) as html_file:

            html_content = html_file.read()

        st.download_button(

            label="⬇️ Download Tutorial HTML",

            data=html_content,

            file_name="tutorial_output.html",

            mime="text/html"
        )

# =========================================================
# FOOTER
# ========================================================= #

st.markdown("---")

st.caption(
    "Powered by TechMedBuddy AI Engine"
)