def readSheet(): #Read the answerSheet.txt
    answerDictionary = {}
    with open("CMSC12Project/answerSheet.txt", "r") as readhandle:
        for line in readhandle:
            line = "".join(line.split("\n"))
            key, words = line.split(":")
            wordList = words.split(",")
            answerDictionary[key] = wordList
    return answerDictionary

#answerDictionary = {
# "Section Of One's Life": ['Chapter', 'Period', 'Phase', 'Stage'], 
# 'Topic Of Discussion': ['Issue', 'Matter', 'Subject', 'Point'], 
# 'Parts Of A Car, Informally': ['Dash', 'Shock', 'Tank', 'Wheel'], 
# 'Color Homophones': ['Blew', 'Choral', 'Read', 'Rows']
# }

