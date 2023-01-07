import streamlit as st
import plotly.express as px
from backend import get_data

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

if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            t = [dict["main"]["temp"] / 10 for dict in filtered_data]
            d = [dict["dt_txt"] for dict in filtered_data]
             # Create a temperature plot
            figure = px.line(x=d, y=t, labels={"x": "Date",
                                       "y": "Temepertaure (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png", "Rain":"images/rain.png", "Snow":"images/snow.png" }
            image_paths = [images[condition] for condition in sky_conditions]
            print(image_paths)
            st.image(image_paths,  width=115)

    except KeyError:
        st.write("That place does not exists.")