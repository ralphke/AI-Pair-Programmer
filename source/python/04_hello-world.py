
# Initial strings
msg = "Hello World"
word = "Universe"

# Count the number of letters in each string
num_letters_msg = len(msg)
num_letters_word = len(word)

# Count the number of "l" letters in each string
num_l_msg = msg.count('l')
num_l_word = word.count('l')

# Count the number of unique letters in each string
unique_letters_msg = len(set(msg))
unique_letters_word = len(set(word))

# Print the results in one line
print(f"msg: {num_letters_msg} letters, {num_l_msg} 'l' letters, {unique_letters_msg} unique letters; word: {num_letters_word} letters, {num_l_word} 'l' letters, {unique_letters_word} unique letters")

# Replace the word "World" with "Universe"
modified_msg = msg.replace("World", "Universe")

# Print the modified message
print(modified_msg)
# 5. Replace the word "World" with "Universe"
msg_replaced = msg.replace("World", "Universe")

# 6. Print the result
print(f"Replaced message: {msg_replaced}")
####
# Bonus: validate if text exists in the string.
def word_exists(word, text):
    return word in text
switch = {
    True: lambda: print("The Word '{}' exists in Text".format(word)),
    False: lambda: print("The Word '{}' exists not in Text".format(word)),
}

switch[word_exists('Universe', msg_replaced)]()
###
