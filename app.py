import streamlit as st
import member_C  # Make sure member_C.py is in the same folder

# ------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------
st.set_page_config(
    page_title="TikTok Shop Impulse Buying Study",
    layout="wide"
)

# ------------------------------------------------------------
# Main title
# ------------------------------------------------------------
st.title("📊 Determinants of Students' Impulse Buying Behavior on TikTok Shop")

# ------------------------------------------------------------
# Sidebar for page navigation
# ------------------------------------------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to page:",
    ["Main Page", "Member A", "Member B", "Member C", "Member D"]
)

# ------------------------------------------------------------
# Page content based on selection
# ------------------------------------------------------------
if page == "Main Page":
    st.subheader("Project Overview")
    st.write("""
    This Streamlit dashboard presents a scientific visualization study on students' impulse buying behavior on TikTok Shop.
    It explores how factors such as **trust, motivation, product presentation, promotions, and discovery** influence impulse buying.
    """)
    
    st.write("Use the sidebar to navigate to each group member's page for more specific analysis.")
    
elif page == "Member C":
    # Call your member_C.py page function
    try:
        member_C.app()
    except Exception as e:
        st.error(f"Error loading Member C page: {e}")

else:
    st.subheader(page)
    st.write("This page is under construction. Please check back later.")
