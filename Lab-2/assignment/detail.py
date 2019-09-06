
studDetails = {
    50: {
        "name": "Adarsh",
        "age": 20,
        "section": "A"
    },
    51: {
        "name": "aaa",
        "age": 20,
        "section": "A"
    },
    52: {
        "name": "aab",
        "age": 21,
        "section": "B"
    },
    56: {
        "name": "abb",
        "age": 21,
        "section": "C"
    },
    57: {
        "name": "bbb",
        "age": 20,
        "section": "A"
    }

}

for a in studDetails:
    if a % 2 == 0:
        print(a, " : ", studDetails[a])
