import  random
"""
Generate sample longitude and Latitude sample data for northern Stockholm.
Args:
num_samples (int): The number of samples to generate
Returns:
list: A list of tuples representing latitude and longitude cordinates
"""

def generate_latitiude():
    return round(random.uniform(59.35, 59.48), 6)

def generate_longitude():
    return round(random.uniform(17.88, 18.14), 6)
# Number of sample cordinates to generate
num_samples = 15

sample_data = []

for _ in range(num_samples):
    lat = generate_latitiude()
    lon = generate_longitude()
    sample_data.append((lat, lon))

for data_point in sample_data:
    print(f"Latitude: {data_point[0]}, Longitude: {data_point[1]}")