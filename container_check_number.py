containerNumber = input("Enter a container number: ")

if len(containerNumber) != 10:
    print("Error: Container Number Length Must Be 10")
    quit()

def placeCalculator(count, value):
    if (0 <= count and count <= 3):
        if not (65 <= ord(value) and ord(value) <= 90):
            print("Error: First four needs to be characters")
            quit()
        else:
            if value == 'A':
                return ord(value) - 55
            elif 'B' <= value and value <= 'K' : 
                return ord(value) - 54
            else:
                return ord(value) - 53
    else:
        if not (48 <= ord(value) and ord(value) <= 57):
            print("Error: Last six need to be number")
            quit()
        else:
            return ord(value) - 48

total = 0

for count, value in enumerate(containerNumber):
    result = placeCalculator(count, value) * pow(2, count)
    total = total + result

newTotal = (total // 11) * 11


print("Check digit: ", total - newTotal)