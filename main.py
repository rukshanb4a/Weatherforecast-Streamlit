import streamlit as st

st.title("Weather Forecaset for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1,
                 max_value=5,
                 help="Select the number of "
                      "forecast days")
option = st.selectbox("Select data to view",
                      ("Temeperature", "Sky"))
st.subheader(f"option for the next {days}"
             f" days in {place}")
