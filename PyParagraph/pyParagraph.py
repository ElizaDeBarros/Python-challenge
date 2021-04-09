import os
sentences = []
characters = []

# open text file
file_path = os.path.join('raw_data','paragraph_2.txt')
with open(file_path,'r') as f:
    # reads contents of text file
    contents = f.read()

    # count the number of characters
    count_characters = 0
    for i in range(len(contents)):
        characters = contents[i].split()
        count_characters = count_characters + len(characters)

    # returns a list with all the lines in string
    contents = contents.splitlines()
    total_lines = len(contents)

    #count sentences
    count_sentences = 0
    for i in range(len(contents)):
        if contents[i] != "":
            count_sentences = count_sentences + 1

    count_word = 0
    for i in range(total_lines):
        sentences = contents[i].split()
        count_word = count_word + len(sentences)

print("Paragraph Analysis")
print("-------------------")
print("Approximate Word Count: " + str(count_word))
print("Approximate Sentence Count: " + str(count_sentences))
print("Average Letter Count: " + str(round((count_characters / count_word),1)))
print("Average Sentence Length: " + str(round((count_word / count_sentences),1)))


