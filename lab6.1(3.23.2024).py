## Total Function

def program1():
    country  = input("Enter The Name of a Country: ")

    infile = open ('/Users/kadiyala/Documents/Exchrate.txt', 'r')
    for line in infile:
        line = line.rstrip()
        data = line.split(',')
        if data[0] == country:
            foundFlag = True
            print("Lab 6.1 Answer:")
            print("Currency:", data[1])
            print("Exchange Rate: ", data[2])
            break
    if (not foundFlag):
        print(f"Lab 6.1 Answer: {country} is not in the file.")
        
program1()

def program2():
    infile = open ('/Users/kadiyala/Documents/Exchrate.txt', 'r')
    countryList = []
    for line in infile:
        countryList.append(line.rstrip())
    infile.close()
    for i in range (len(countryList)):
        countryList[i] = countryList[i].split(',')
    countryList.sort(key=lambda x: x[2])
    for i in range(3):
        print (countryList[i][0])

print("\n")
program2()

def program3():
    country1 = input("Enter First Country: ")
    country2 = input("Enter Second Country: ")
    amount = eval(input("Enter Amount Of Money TO Convert: "))
    infile = open ('/Users/kadiyala/Documents/Exchrate.txt', 'r')
    countryList = []
    for line in infile:
        countryList.append(line.rstrip())
    infile.close()
    d = {}
    for i in range (len(countryList)):
        countryList[i] = countryList[i].split(',')
        d[countryList[i][0]] = (countryList[i][1], eval(countryList[i][2]))
    ##print("{0} {1}s from {2} equals {3:,.2f} {4}s from {5}."), format(amount, d[country1][0].lower(), country1, amount *(d[country2][1] / d[country1][1]), d[country2][0].lower(), country2))
    print("{0} {1}s from {2} equals {3:.2f} {4} from {5}".format(amount, d[country1][0].lower(), country1, amount * d[country2][1] / d[country1][1], d[country2][0].lower(), country2))

print("\n")
program3()
        
