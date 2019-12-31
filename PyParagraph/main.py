#Import objects
import os
import re

#Set the file path
#file_path = os.path.join('..','Resources','Paragraph.txt')

#initiate lists
list_words = []
list_sentences = []
list_letters = []


def calculate_total_letters():

    i = 0
    global letters
    letters = 0

    while i < len(list_sentences):

        j = 0

        list_sentence_words = list_sentences[i].split()

        while j < len(list_sentence_words):

            #list_letters = len(list_sentence_words[j])
            #print(f'{list_letters}')
            letters += len(list_sentence_words[j])

            j += 1

        i += 1

    return letters

paragraph = open('Paragraph.txt','r')

#Calculate results and print on terminal
for line in paragraph:


    #Split the paragraph into words
    list_words = line.split()
    words = len(list_words)

    #Split the paragraph into sentences and perform calculations
    list_sentences = re.split('(?<=[.!?]) +', line)
    sentence_count = len(list_sentences)
    avg_sentence_length = words/sentence_count

    #Call function to get the number of letters and calculate average
    calculate_total_letters()
    avg_letters_per_word = round(letters/words,1)

    #Print the results on the terminal
    print('---output')
    print('Paragraph Analysis')
    print('---------------------')
    print(f'Approximate Word Count: {words}')
    print(f'Approximate Sentence Count: {sentence_count}')
    print(f'Average Letter Count: {avg_letters_per_word}')
    print(f'Average Sentence Length: {avg_sentence_length}')
    print('---')

paragraph.close()
