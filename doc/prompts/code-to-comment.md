---
title: "Code to Comment"
description: "Generating comments from code"
category: prompts
platforms: [copilot, copilot-chat]
aliases:
  - /doc/prompts/code-to-comment
---

## Code to Comment: Generating Comments from Code

### Description

GitHub Copilot can generate comments from code. When existing code lacks sufficient comments, or to assist other developers in understanding the code, GitHub Copilot can automatically generate explanations in comment form. The following sample demonstrates an algorithm to list prime numbers less than a given number. While this code does not contain comments, GitHub Copilot can create comments to describe the code's functionality.

#### Example

Here's the code without comments:

```python
def generate_primes(start=1, end=1000, max_iterations=None):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    iterations = 0
    for num in range(start, end+1):
        if max_iterations and iterations >= max_iterations:
            break
        if is_prime(num):
            primes.append(num)
            iterations += 1
    return primes
```

Here's how GitHub Copilot can add comments to explain it:

```python
# Write the description of the method here <- [Actual Prompt]
# Generates a list of prime numbers within a given range.
# Args:
#    start (int, optional): The starting number of the range (inclusive). Defaults to 1.
#    end (int, optional): The ending number of the range (inclusive). Defaults to 1000.
#    max_iterations (int, optional): The maximum number of prime numbers to generate. Defaults to None.
# Returns:
#    list: A list of prime numbers within the specified range.

def generate_primes(start=1, end=1000, max_iterations=None):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    iterations = 0
    for num in range(start, end+1):
        if max_iterations and iterations >= max_iterations:
            break
        if is_prime(num):
            primes.append(num)
            iterations += 1
    return primes
```

### Exercise

- **Exercise**: Generate appropriate comments for the code at the top of the following function:
```python
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```

### Checklist for Further Learning

- Do the generated comments adequately explain the code's functionality and algorithm?
- Are the comments helpful for other developers to understand the code?
- What do you think could be the reason for any incorrect comments that were generated?
