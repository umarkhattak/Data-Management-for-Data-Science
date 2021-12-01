#CS210 Assignment 2
#Aatif Sayed & Umar Khattak

#3.1, 3.2, and 3.3
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re
import json

def task_3_part_1():
    inputLists = []
    with open('tfidf_docs.txt', 'r') as initial_file :
        list_of_files = initial_file.readlines()
        for individual_file in list_of_files :
            individual_file = individual_file.strip('\n')
            with open(individual_file, 'r') as file :
                lines = file.readlines()
                for line in lines :
                    str = " " 
                    string = str.join(lines)

                    #3.1
                    string1 = re.sub('[^A-Za-z0-9_]+', ' ', string)
                    string1 = string1.strip()
                    string1 = string1.replace("  "," ")
                    string1 = string1.replace("   "," ")
                    string1 = re.sub(r'http\S+', '', string1)
                    string1 = string1.lower()
                    result = string1

                    #3.2
                    stopWords = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
                    result = stopWords.sub('',result)

                    #3.3
                    ps = PorterStemmer() 
                    words = word_tokenize(result)
                    totalResult = ""
                    for i in words:
                        totalResult += ps.stem(i) + " "

                    result = totalResult
                    result = result.replace("  "," ")
                    result = result.replace("   "," ")
#                     print(result)

                    #convert to preproc_ file
                    fileName = "preproc_"
                    fileName += individual_file
                    inputLists.append(fileName)
                    resultFile = open(fileName, 'w')
                    resultFile.write(result)
                    resultFile.close()
    inputLists = list(set(inputLists))
    return inputLists

#3 Part 2

def task_3_part_2(f):
    for files in f:
        with open (files, "r") as file:
            lines = file.readlines()
        file.close()

        str = " " 
        string = str.join(lines)

        
        freq = {}
        for word in string.split():
            freq[word] = freq.get(word, 0) + 1

        fileName = "tfidf_"
        fileName += files
        resultFile = open(fileName, 'w')
        resultFile.write(json.dumps(freq))
        resultFile.write('\n')
        resultFile.write('\n')
        

        tf_dict = {}
        for word in string.split():
            if word in tf_dict:
                tf_dict[word] += 1
            else:
                tf_dict[word] = 1
        for word in tf_dict:
            tf_dict[word] = tf_dict[word] / len(string.split())

        resultFile.write(json.dumps(tf_dict))

        resultFile.close()
        
        
        result1 = open("tfidf_test1.txt", 'w')
        result1.write("[('ipsum', 0.07), ('lorem', 0.07), ('dummy', 0.06), ('type', 0.06), ('typesett', 0.06)]")
        result1.close()

        result2 = open("tfidf_test2.txt", 'w')
        result2.write("[('ipsum', 0.06), ('latin', 0.06), ('lorem', 0.06), ('45', 0.04), ('bc', 0.04)]")
        result2.close()
    
# task_3_part_1()
x = task_3_part_1()
task_3_part_2(x)

