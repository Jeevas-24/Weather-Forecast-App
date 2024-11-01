import streamlit as st
import plotly.express as px

# Widget Parts
st.title('Weather Forecast for the next days')
place = st.text_input('Place:')
days = st.slider('Forecast days:', min_value=1, max_value=5,
                 help='Select the number of forecasted days')
option = st.selectbox('Select data to view', ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {place}')


# Function to return the days from Ui
def get_days(day):
    dates = ['24-1-11', '24-2-11', '24-3-11']
    temperature = [19, 37, 52]
    temperature = [day * i for i in temperature]
    return dates, temperature


d, t = get_days(days)
# Graph part
figure = px.line(x=d, y=t, labels={'x': 'Dates', 'y': 'Temperature (C)'})
st.plotly_chart(figure)
