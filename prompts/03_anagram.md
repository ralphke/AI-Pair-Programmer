# Coding Challenge: Anagram Checker
## Prompt
You will receive an array of strings.
Submit that array of strings, sorted from A-Z, but only supply the words that are an anagram of another word in that array.
## Sample Data
Input: [ "kiwi", "melon", "apple", "lemon" ]

Output: [ "lemon", "melon" ]

## Test Data
Validate the solution with this data [anagram.json](data\anagram.json)

## Prompt
Write a Python function that checks if two given strings are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Sample Data
Input: ("listen", "silent")

Output: True

## Input: ("hello", "billion")

Output: False

## Test Data

**Easy Sample Data:**
- Input: `("listen", "silent")`
- Output: `True`

- Input: `("hello", "billion")`
- Output: `False`

**Complex Sample Data:**
- Input: `("a gentleman", "elegant man")`
- Output: `True`

- Input: `("The eyes", "They see")`
- Output: `True`

- Input: `("Dormitory", "Dirty room")`
- Output: `True`


#### Rating for Code Result

- **Excellent**: The code correctly identifies all anagrams, handles spaces and case sensitivity, and is efficient.
- **Good**: The code correctly identifies most anagrams but may have minor inefficiencies or edge cases it doesn't handle.
- **Bad**: The code fails to identify several anagrams or has significant inefficiencies.
- **Ugly**: The code is incorrect, inefficient, and fails to handle basic cases.

### Example Rating
For the provided solution, the rating would be **Excellent** as it correctly handles all given cases, including spaces and case sensitivity, and is efficient.


### Solution
You can find the solution in the [anagram_checker.py](..\source\python\03_anagram.py) file.