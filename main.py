# Main application
# Modularization with Function

def extract_data():
    data = {
        'date': '03 June 2023',
        'time': '00:13:22 WIB',
        'magnitude': 3.7,
        'depth': '10 km',
        'location': {
            'latitude': '2.32 LS',
            'longitude': '140.56 BT',

        },
        'epicenter': 'Pusat gempa berada di laut 31 km BaratLaut Kota Jayapura',
        'range': 'Dirasakan(Skala MMI): II - III KotaJayapura'
    }
    return data


def display_data(data):
    print('The latest Earthquake based on BMKG official website:')
    for key, value in data.items():
        if type(value) == dict:
            print(f"    {key}:")
            for x, y in value.items():
                print(f"        {x}: {y}")
            continue
        print(f"    {key}: {value}")


if __name__ == '__main__':
    print('Main Application')
    result = extract_data()
    display_data(result)
