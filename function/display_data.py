def display_data(data):
    print('The latest Earthquake based on BMKG official website:')
    for key, value in data.items():
        if type(value) == dict:
            print(f"    {key}:")
            for x, y in value.items():
                print(f"        {x}: {y}")
            continue
        print(f"    {key}: {value}")