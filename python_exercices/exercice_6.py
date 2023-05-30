#file_name = 'C:\Users\surya\python\python_exercices\text.txt'
#my_file = open(file_name, "r")
#file_lines = my_file.readlines()
list_words = []
with open("C:/Users/surya/python/python_exercices/text.txt","r") as readfile:
    words = readfile.readlines()

    for line in words:
        words_count = line.split()
        print(len(words_count))
