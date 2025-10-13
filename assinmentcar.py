1 '''import file'''
import pandas as pd

df = pd.read_csv('/content/data.csv')
display(df)

2 '''show all cars list'''
car_categories = df['Make'].unique()
print("Car Categories:")
for category in car_categories:
    print(category)

3 '''car units list vise'''

car_counts_by_make = df['Make'].value_counts()
display(car_counts_by_make)

4 '''top 5 most popular car'''

highest_popularity_cars = df.sort_values(by='Popularity', ascending=False)
display(highest_popularity_cars.head(5))

5'''which car higst selling and yers'''

highest_selling_car = df.sort_values(by='MSRP', ascending=False).head(1)
display(highest_selling_car)

6'''bmw first series cars show'''

bmw_1_series_cars = df[(df['Make'] == 'BMW') & (df['Model'].str.contains('1 Series'))]
display(bmw_1_series_cars)

7'''cars size list'''

vehicle_size_counts = df['Vehicle Size'].value_counts()

compact_cars = vehicle_size_counts.get('Compact', 0)
midsize_cars = vehicle_size_counts.get('Midsize', 0)
large_cars = vehicle_size_counts.get('Large', 0)

print(f"Number of Compact cars: {compact_cars}")
print(f"Number of Midsize cars: {midsize_cars}")
print(f"Number of Large cars: {large_cars}")

8'''manufecturing car year vise'''

cars_by_year = df['Year'].value_counts().sort_index()

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
cars_by_year.plot(kind='line')
plt.title('Number of Car Models Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Models')
plt.grid(True)
plt.show()

9'''all typs of driven'''

driven_wheels_counts = df['Driven_Wheels'].value_counts()
display(driven_wheels_counts)

10'''vehicle style'''

vehicle_styles = df['Vehicle Style'].unique()
print("Vehicle Styles:")
for style in vehicle_styles:
    print(style)

11'''highway mpg'''

highest_highway_mpg_car = df.sort_values(by='highway MPG', ascending=False).head(1)
display(highest_highway_mpg_car)

12'''**city** mpg'''

highest_city_mpg_car = df.sort_values(by='city mpg', ascending=False).head(1)
display(highest_city_mpg_car)