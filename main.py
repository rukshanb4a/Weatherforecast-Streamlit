import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1,
                 max_value=5,
                 help="Select the number of "
                      "forecast days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days}"
             f" days in {place}")


def get_data(days):
    dates = ["2023-05-01", "2023-06-01", "2023-07-01"]
    temperatures = [25, 29, 22]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date",
                                   "y": "Temepertaure (C)"})
st.plotly_chart(figure)
