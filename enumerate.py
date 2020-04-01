########### enumerate() function: adds a counter to an iterable OBJECT ##########


# for tuples
greek_letters = ("alpha", "beta", "delta")

print(list(enumerate(greek_letters)))



# for lists
greek_letters = ["alpha", "beta", "delta"]

print(list(enumerate(greek_letters)))



# for dictionaries
days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}

print(list(enumerate(days)))