import streamlit as st

def apply_style():

    st.markdown('''
    <style>
        # style for team card boxes
                .card {
                    background: #fff;
                    border-radius: 10px;
                    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
                    margin_bottom: 10px;
                }
                .center {
                    text-align: center;
                }
                .center_div {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    flex-wrap: wrap;
                    flex-direction: column;
                    height: 100%;
                    width: 100%;
                }

                /* reduce top padding of the page */
                .css-18e3th9 { padding-top: 0rem; }
    </style>
    ''',
    unsafe_allow_html=True)