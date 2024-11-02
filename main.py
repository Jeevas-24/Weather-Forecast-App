import streamlit as st
import plotly.express as px
from backend import get_data

# Widget Parts inlcuding title, text_input, slider, select box
st.title('Weather Forecast for the next days')
place = st.text_input('Place:')
days = st.slider('Forecast days:', min_value=1, max_value=5,
                 help='Select the number of forecasted days')
option = st.selectbox('Select data to view', ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {place}')

if place:
    filtered_data = get_data(place, days)
    if option == 'Temperature':
        temperatures = [dict['main']['temp'] for dict in filtered_data]
        date = [dict['dt_txt'] for dict in filtered_data]
        # Graph part for temperature
        figure = px.line(x=date, y=temperatures,
                         labels={'x': 'Dates', 'y': 'Temperature (C)'})
        st.plotly_chart(figure)

    if option == 'Sky':
        sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
        images = {'Rain': 'images/rain.png', 'Clear': 'images/clear.png',
                  'Clouds': 'images/cloud.png', 'Snow': 'images/snow.png'}
        images_path = [images[conditions] for conditions in sky_conditions]
        columns = st.columns(5)
        for index, item in enumerate(images_path):
            with columns[index % 5]:
                text_1 = item.split('/')[1]
                text_1 = text_1.split('.')[0]
                st.image(item, width=115, caption=text_1)


