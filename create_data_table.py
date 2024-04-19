import pandas as pd

# Create the data for the tables
data = {
    'Week': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Sponsored_Google': ["32,269", "31,951", "32,143", "31,417", "31,194", "31,576", "30,951", "30,611", "30,401", "0", "0", "0"],
    'Organic_Google': ["127,876", "128,169", "125,717", "126,264", "123,871", "124,053", "126,105", "123,064", "121,637", "150,188", "148,658", "146,584"],
    'Sponsored_Bing': ["3,965", "3,984", "3,960", "3,952", "3,874", "3,932", "3,890", "3,883", "3,843", "3,815", "3,754", "3.754"],
    'Organic_Bing': ["15,805", "15,964", "15,815", "15,810", "15,633", "15,797", "15,462", "15,309", "15,499", "15,185", "15,159", "15,036"]
}

# Clean Sponsored_Google data (remove commas)
data['Sponsored_Google'] = [int(x.replace(',', '')) for x in data['Sponsored_Google']]

# Create the pandas DataFrames
df_google = pd.DataFrame(data, columns=['Week', 'Sponsored_Google', 'Organic_Google'])
df_bing = pd.DataFrame(data, columns=['Week', 'Sponsored_Bing', 'Organic_Bing'])

# Print the DataFrames as tables
print("Table 1: Weekly traffic from Google by origin of click")
print(df_google.to_string(index=False))

print("\nTable 2: Weekly traffic from Bing by origin of click")
print(df_bing.to_string(index=False))
