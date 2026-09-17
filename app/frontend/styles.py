import streamlit as st


def apply_dark_theme():

    st.markdown(
        """
        <style>

        /* =========================================
           GLOBAL APP
           ========================================= */

        .stApp {
            background: #080C12;
            color: #F8FAFC;
        }


        /* =========================================
           STREAMLIT TOP HEADER
           ========================================= */

        [data-testid="stHeader"] {
            background-color: #080C12 !important;
        }

        [data-testid="stDecoration"] {
            background-color: #080C12 !important;
        }

        [data-testid="stToolbar"] {
            background-color: #080C12 !important;
        }

        [data-testid="stHeader"] button {
            color: #FFFFFF !important;
        }


        /* =========================================
           SIDEBAR
           ========================================= */

        [data-testid="stSidebar"] {
            background-color: #0B111A !important;
        }

        [data-testid="stSidebar"] * {
            color: #F8FAFC !important;
        }


        /* =========================================
           MAIN TEXT
           ========================================= */

        h1, h2, h3, h4, h5, h6 {
            color: #F8FAFC !important;
        }

        p, label, span {
            color: #CBD5E1;
        }


        /* =========================================
           METRIC CARDS
           ========================================= */

        [data-testid="stMetric"] {
            background: #0F172A;
            border: 1px solid #1E293B;
            border-radius: 12px;
            padding: 18px;
        }

        [data-testid="stMetricValue"] {
            color: #F8FAFC !important;
        }

        [data-testid="stMetricLabel"] {
            color: #94A3B8 !important;
        }


        /* =========================================
           INPUTS
           ========================================= */

        textarea,
        input {
            background-color: #0F172A !important;
            color: #F8FAFC !important;
            border: 1px solid #334155 !important;
        }


        /* =========================================
           BUTTONS
           ========================================= */

        .stButton > button {
            background: #2563EB;
            color: white !important;
            border: none;
            border-radius: 8px;
        }

        .stButton > button:hover {
            background: #3B82F6;
        }


        /* =========================================
           FILE UPLOADER
           ========================================= */

        [data-testid="stFileUploader"] {
            background: #0F172A;
            border: 1px solid #334155;
            border-radius: 12px;
        }


        /* =========================================
           SELECTBOX / INPUT CONTAINERS
           ========================================= */

        [data-baseweb="select"] > div {
            background-color: #0F172A !important;
            color: #F8FAFC !important;
        }


        /* =========================================
           PROGRESS BAR
           ========================================= */

        [data-testid="stProgress"] > div > div {
            background-color: #2563EB;
        }


        /* =========================================
           DIVIDERS
           ========================================= */

        hr {
            border-color: #1E293B !important;
        }


        /* =========================================
           ALERTS / INFO
           ========================================= */

        [data-testid="stAlert"] {
            background-color: #0F172A;
            border: 1px solid #1E293B;
        }


        /* =========================================
           CODE / PREVIEW
           ========================================= */

        code {
            background-color: #111827 !important;
            color: #E2E8F0 !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )