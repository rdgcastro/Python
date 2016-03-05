# Dicitonary methods

months_dictionary = {1: "January", 2: "February", 3: "March",
                     4: "April", 5: "May", 6: "June", 7: "July",
                     8: "August", 9: "September", 10: "October",
                     11: "November", 12: "December"}

print("The dictionary items are:")
print(months_dictionary.items())

print("\nThe dictionary keys are:")
print(months_dictionary.keys())

print("The dictionary values are:")
print(months_dictionary.values())

print("\nUsing a for loop to get dictionary items:")

for key in months_dictionary.keys():
    print("months_dictionary [", key, "] = ", months_dictionary[key])
