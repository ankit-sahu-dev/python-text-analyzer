paragraph = input("Enter a paragraph: ")
print(F"Total characters: {len(paragraph)}")
words = paragraph.split()
print(F"Total words: {len(words)}")

longest_word = words[0]
for word in words:
    if len(longest_word) < len(word):
        longest_word = word
        

print(F"Longest word: {longest_word}")

def vowel_count(paragraph):
    vowels_count= 0
    for word in paragraph:
        if word == "a" or word == "i" or word == "o" or word == "e" or word == "u":
            vowels_count += 1
    return vowels_count
            
print(F"Total vowels: {vowel_count(paragraph)}")

word_count = {}
for word in words:
     
    if word in word_count:
         word_count[word] += 1
    else:
        word_count[word] = 1
        
for word, count in word_count.items():
    print(F"{word}: {count}")
    
max_count = 0
most_common = ""

for word, count in word_count.items():
    if count > max_count:
        max_count = count
        most_common = word
        
print(F"Most common word: {most_common} and  its count: {max_count}")
    