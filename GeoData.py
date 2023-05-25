import pandas as pd
import  random

"""
Generate sample longitude and Latitude sample data for northern Stockholm.
and put them in an excel sheet
"""
def generate_lat_long(samples):

    coordinates = []
    for _ in range(samples):
# Generate latitude within the range of 59.35 to 59.48
        latitude = random.uniform(59.35, 59.48)
        longitude = random.uniform(17.88, 18.14)
        coordinates.append((latitude, longitude))
    return coordinates


num_samples = 50 
coordinates = generate_lat_long(num_samples)

#Creating dataframe to store the coordinates
df = pd.DataFrame(coordinates, columns=['Latitude', 'Longitude'])

filePath = 'coordinates.xlsx'
df.to_excel(filePath, index=False) # excluding the index column  in the saved file
print(coordinates)
