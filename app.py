import streamlit as st
import pytz
from datetime import datetime

# Title of the app
st.title('Digital Clock with Different Time Zones')

# List of time zones
timezones = ['UTC', 'Asia/Kolkata', 'America/New_York', 'Europe/London']

# Dropdown to select time zones
selected_timezone = st.selectbox('Select Time Zone:', timezones)

# Get the current time in the selected timezone
current_time = datetime.now(pytz.timezone(selected_timezone))

# Display the current time
st.write(f'Current Time in {selected_timezone}: {current_time.strftime('%Y-%m-%d %H:%M:%S')}')