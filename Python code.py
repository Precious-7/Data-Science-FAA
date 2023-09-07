#!/usr/bin/env python
# coding: utf-8

# In[ ]:


paragraph = "#innovation #bigdata #coding #iot #computerscience #data #dataanalytics #business #engineering #robot #datascientist #art #software #automation #analytics #pythonprogramming #programmer #digitaltransformation #developer #love #instagood #fashion #art #artificialintelligence #ai #machinelearning #technology #datascience #python #deeplearning #programming #tech #robotics #innovation #bigdata #coding #iot #computerscience #data #dataanalytics #business #engineering #robot #datascientist #art #software #automation #analytics #ml #pythonprogramming #programmer #digitaltransformation #developer"


# In[ ]:





# In[2]:


def find_duplicate_words(paragraph):
    # Split the paragraph into words
    words = paragraph.split()

    # Create a dictionary to store word frequencies
    word_freq = {}

    # Iterate through the words and count their occurrences
    for word in words:
        # Convert the word to lowercase to treat words with different cases as the same
        word = word.lower()
        # Increment the word's count in the dictionary
        word_freq[word] = word_freq.get(word, 0) + 1

    # Find and return duplicate words
    duplicates = [word for word, count in word_freq.items() if count > 1]

    return duplicates

# Input paragraph
paragraph = "#innovation #bigdata #coding #iot #computerscience #data #dataanalytics #business #engineering #robot #datascientist #art #software #automation #analytics #pythonprogramming #programmer #digitaltransformation #developer #love #instagood #fashion #art #artificialintelligence #ai #machinelearning #technology #datascience #python #deeplearning #programming #tech #robotics #innovation #bigdata #coding #iot #computerscience #data #dataanalytics #business #engineering #robot #datascientist #art #software #automation #analytics #ml #pythonprogramming #programmer #digitaltransformation #developer"

# Find duplicate words
duplicate_words = find_duplicate_words(paragraph)

if duplicate_words:
    print("Duplicate words in the paragraph:", duplicate_words)
else:
    print("No duplicate words found in the paragraph.")


# In[3]:


def remove_duplicate_words(paragraph):
    # Split the paragraph into words
    words = paragraph.split()

    # Create a list to store unique words
    unique_words = []

    # Iterate through the words and add them to unique_words if not already present
    for word in words:
        # Convert the word to lowercase to treat words with different cases as the same
        word = word.lower()
        if word not in unique_words:
            unique_words.append(word)

    # Join the unique words to form a new paragraph
    new_paragraph = ' '.join(unique_words)

    return new_paragraph

# Input paragraph
paragraph = "#innovation #bigdata #coding #iot #computerscience #data #dataanalytics #business #engineering #robot #datascientist #art #software #automation #analytics #pythonprogramming #programmer #digitaltransformation #developer #love #instagood #fashion #art #artificialintelligence #ai #machinelearning #technology #datascience #python #deeplearning #programming #tech #robotics #innovation #bigdata #coding #iot #computerscience #data #dataanalytics #business #engineering #robot #datascientist #art #software #automation #analytics #ml #pythonprogramming #programmer #digitaltransformation #developer"

# Remove duplicate words
new_paragraph = remove_duplicate_words(paragraph)

# Print the paragraph without duplicate words
print("Paragraph without duplicate words:")
print(new_paragraph)


# In[ ]:





# In[ ]:





# In[ ]:




