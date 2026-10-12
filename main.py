from dic import data

import function

country = input("Country name: ")
print(function.totaldeaths(country))


alzheimer = input("Do you want total number of people died from Alzheimer: ")
print(function.Alzheimer(alzheimer))


parkinson = input("Do you want total number of people died from Parkinson: ")
print(function.Parkinson(parkinson))

nutritional_deficiencies = input("Do you want total number of people died from Nutritional deficiencies: ")
print(function.Nutritional_deficiencies(nutritional_deficiencies))

malaria = input("Do you want total number of people died from Malaria: ")
print(function.Malaria(malaria))

drowning = input("Do you want total number of people died from Drowning: ")
print(function.Drowning(drowning))


mini = int(input("Year: "))
maxi = int(input("Year: "))
print(function.Years(mini,maxi))