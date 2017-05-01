import re
import string
frequency = {}
results = []

document_text = open('fetched.json', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for word in frequency_list:
    tuple = (word, frequency[word])
    results.append(tuple)

byFreq=sorted(results, key=lambda word: word[1], reverse=True)

for (word, freq) in byFreq[:15]:
    print word, freq