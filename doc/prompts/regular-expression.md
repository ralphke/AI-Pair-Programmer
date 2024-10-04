---
title: "Regular Expression"
description: "Generating regular expression patterns with GitHub Copilot"
category: prompts
platforms: [copilot, copilot-chat]
aliases:
  - /doc/prompts/regular-expression
---

## Regular Expression

> With the recent improvements, LLMs do now have the ability to properly represent complex regular expressions.
> As usual, a human should test out the generated patterns. 

### Description

GitHub Copilot can create a regular expression patterns. Below, we'll explain how to use regular expressions to search or extract strings. Two examples illustrate how GitHub Copilot can generate regular expressions through both input-output pattern and natural language pattern.

#### Example

##### Input and Output Pattern

###### Sample Code

First, by writing the input and output, GitHub Copilot can create the regular expression pattern:

```python
import re

# Write a regular expression
# - Input: "Write a Regular Expression"
# - Output: ["W", "R", "E"]

regex 
```

###### Sample Result

```python
import re
# Write a regular expression
# - Input: "Write a Regular Expression"
# - Output: ["W", "R", "E"]

regex = r"[A-Z]"
matched = re.findall(regex, "Write a Regular Expression")
print(matched)
```

##### Natural Language Pattern

Second, by providing what you want to achieve with the regular expression in natural language:

###### Sample Code

```python
import re
# Write a regular expression
# - "I have 2 cars and 3 cats" like string, extract only the numbers to make an array

sentence
```

###### Sample Result

```python
import re
# Write a regular expression
# - "I have 2 cars and 3 cats" like string, extract only the numbers to make an array

sentence = "I have 2 cars and 3 cats"
regex = r"\d+"
matched = re.findall(regex, sentence)
```

### Exercise

- **Exercise 1**: Extract only the lowercase letters from the string "I have 2 cars and 3 cats."

### Checklist for Further Learning

- Are the regular expression patterns extracting the exact matches from the given strings?
- Currently, LLMs like GitHub Copilot might not have the ability to properly represent all complex regular expressions. What would you do if you want to represent a complex regular expression? How would you leverage GitHub Copilot to support and assist you in building it?
