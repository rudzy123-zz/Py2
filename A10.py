#Rudolf T Musika
#CIS 1400
#Chapter 10 Assignment

def main():
    #Select the golfer count so you can have a number of people playing
    golferCount = int(input("Enter the number of golfers: "))

    #open the existing golfers.data.txt file to have the data placed into
    outputFile = open("golfers.data.txt","w")

    #read lines from input from key board
    #and write the line to output
    index = 0
    for index in range (golferCount):
        line = getInstructionName()
        outputFile.write(line+"\n")
        index+=1
    print("Data written to golfers.txt")
    #Append a line of text to outputFile
    outputFile.close()

def getInstructionName():
    nameScore = input("Enter the name of a golfer a space and their score: ")
    return nameScore

main()
