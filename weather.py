import pandas as pd
import os

file_path = os.path.join(os.path.dirname(__file__), 'file.csv')
data = pd.read_csv(file_path)

'''print(data.head())
print(data.shape)
print(data.index)
print(data.columns)
print(data.dtypes)
print(data['Weather'].unique())
print(data.nunique())
print(data.count())
print(data['Weather'].value_counts())
print(data.info())'''

# Q.1) Find all the unique 'Wind Speed' values in the data
print("Answer for Q.1: ")
print(data['Wind Speed_km/h'].unique())

# Q.2) Find the number of times when the 'Weather is exactly clear'
print("\n Answer for Q.2: ")
print(data[data.Weather == 'Clear'].shape[0])

# Q.3) Find the number of times when the 'Wind speed was exactly 4km/hr'
print("\n Answer for Q.3: ")
print(data[data['Wind Speed_km/h'] == 4].shape[0])

# Q.4) Find out all the Null values in the data
print("\n Answer for Q.4: ")
print(data.isnull().sum())

# Q.5) Rename the column name 'Weather' of the dataframe to 'Weather condition'
print("\n Answer for Q.5: ")
rename = data.rename(columns={'Weather':'Weather Condition'})
print(rename)

# Q.6) What is the mean 'Visibility'?
print("\n Answer for Q.6: ")
print(round(data.Visibility_km.mean(),2))

# Q.7) What is the standard deviation of 'Pressure' in this data?
print("\n Answer for Q.7: ")
print(round(data.Press_kPa.std(),2))

# Q.8) What is the variance of 'Relative Humidity' in this data?
print("\n Answer for Q.8: ")
print(round(data['Rel Hum_%'].var(),2))

# Q.9) Find all instances when 'Snow' was recorded
print("\n Answer for Q.9: ")
print(data[data['Weather']=='Snow'])

# Q.10) Find all instances when 'Wind speed is above 24' and 'Visibility is 25'
print("\n Answer for Q.10: ")
print(data[(data['Wind Speed_km/h']>24) & (data['Visibility_km'] == 25)])