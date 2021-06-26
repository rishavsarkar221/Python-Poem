with open('./Poem.txt', "r") as poem:
    words = {}
    
    maxValue = []
    eachWord = []
    maxTimesAppearing = []

    for word in poem:
        split = word.split(" ")

        #Checks if that word exists in the list
        for j in split:
            if j in words:
                # If word exists in list then it adds the times repeating by 1
                words[j] += 1
            else:
                # If doesn't exists then it makes the times repeating 1
                words[j] = 1

    # Loops through all the words
    for count in words:
        # Appends each words
        maxValue.append(words[count])
        
        #Makes an object and adds the value "count" in "word" and adds the value "words[count]" (Meaning the times repeating) in "times"
        eachWord.append({"word": count, "times": words[count]})

    #Gets the index of the most time repeating
    maxValueIndex = maxValue.index(max(maxValue))

    # To check the "word" which is repeated most
    for a in eachWord:
        #If a["times"] is equal to max times repeating then it appends that word
        if a["times"] == max(maxValue):
            maxTimesAppearing.append(a["word"])

    #Prints
    print(f'{maxTimesAppearing} appeared most times\nCount: {maxValue[maxValueIndex]}')


    #OVERRRRRR!
