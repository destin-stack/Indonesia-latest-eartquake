# Main application
# Modularization with Function
from function.display_data import display_data
from function.extract_data import extract_data

if __name__ == '__main__':
    print('Main Application')
    result = extract_data()
    display_data(result)
