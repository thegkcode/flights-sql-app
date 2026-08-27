import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px

db = DB()

st.sidebar.title("Flights Analytics")

user_option = st.sidebar.selectbox('Menu', ['Select One', 'Check Flights', 'Analytics'])

if user_option == 'Check Flights':
    st.title('Check Flights')

    col1, col2 = st.columns(2)
    city = db.fetch_city_names()

    with col1:
        source = st.selectbox('Source', sorted(city))
    with col2:
        destination = st.selectbox('Destination', sorted(city))

    if st.button('Search'):
        results = db.fetch_all_flights(source, destination)
        if len(results)==0:
            'No flight exist between these two cities'
        else:
            st.dataframe(results)

elif user_option == 'Analytics':
    airline, frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        )
    )

    st.header("Pie Chart")
    st.plotly_chart(fig)

    city, frequency1 = db.busy_airport()
    fig = px.bar(
        x=city,
        y=frequency1
    )

    st.header("Bar Chart")
    my_config = {"show_link": False, "displayModeBar": True}
    st.plotly_chart(fig, config=my_config)

    date, count = db.daily_frequency()
    fig = px.line(
        x=date,
        y=count
    )

    st.header("Line Chart")
    my_config = {"show_link": False, "displayModeBar": True}
    st.plotly_chart(fig, config=my_config)

else:
    st.title('Tell us about the projects')