def find_suggested_words(input_word, exclude_letters, word_length):
    exclude_letters = set(exclude_letters)
    word_object = {}

    for i in range(len(input_word)):
        if(input_word[i] == "_"):
            word_object[i+1] = ""
        else:
            word_object[i+1] = input_word[i]

    if(len(input_word) <= word_length):
        for i in range(len(input_word), word_length):
            word_object[i+1] = ""
    else:
        return {"error": "word length is greater than the length of the input word"}
    
    suggested_words = {}
    with open('unigram_freq.csv', 'r') as f:
        for line in f:
            word, freq = line.strip().split(",")
            if len(word) == word_length:
                found = True
                for i in range(0, word_length):
                    if word_object[i+1] == "" and word[i] in exclude_letters:
                        found = False
                        break                    
                    if word_object[i+1] != "" and word_object[i+1] != word[i]:
                        found = False
                        break
                if found:
                    suggested_words[freq] = word             

    suggested_words = sorted(suggested_words.items(), key=lambda x: x[0],reverse=True)
    final_suggested_words = []
    for freq, word in suggested_words:
        final_suggested_words.append(word)
    return final_suggested_words   
    