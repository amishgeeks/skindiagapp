# app.py

# Import necessary libraries
# Removed TensorFlow imports
import datetime

# Function to display the current digital clock

def display_digital_clock():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')

# Main execution
if __name__ == '__main__':
    print('Digital Clock: ', display_digital_clock())