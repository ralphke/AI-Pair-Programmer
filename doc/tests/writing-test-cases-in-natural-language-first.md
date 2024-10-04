---
title: "Writing test cases in natural language first"
description: "Use natural language to write test cases first, and then use GitHub Copilot to generate code to improve test coverage."
category: tests
platforms: [copilot, copilot-chat]
aliases:
  - /doc/tests/writing-test-cases-in-natural-language-first
---

## Writing Test Cases in Natural Language First

### Description

When working with AI-powered code generation, like GitHub Copilot, expecting comprehensive test coverage without providing clear context to the AI is challenging. Instead of trying to write the test cases in code at that point, create natural language descriptions first. This will focus on improving the test coverage, ensuring that the generated code meets all the necessary criteria.

#### Example

Here's an example of how you can write test cases in natural language for a multiplication function. This practice ensures that you cover various scenarios and edge cases before generating the code.

```py
class TestMultiply(unittest.TestCase):
  def test_multiply(self): 
    # Tests for different cases, such as positive, negative, zero, decimal, and non-integer inputs
```

### Exercise

- **Exercise 1**: Write natural language test cases for a function that calculates the area of a triangle. Consider different input scenarios and edge cases.
- **Exercise 2**: Use GitHub Copilot to generate code from the natural language test cases you wrote in Exercise 1. Analyze the results.
- **Exercise 3**: Create a test suite using natural language for a more complex function, like a sorting algorithm. Consider various input scenarios and edge cases.

### Checklist for Further Learning

- What are the benefits of writing test cases in natural language before coding?
- How can natural language test cases improve collaboration between developers and non-technical stakeholders?
- What are the potential challenges of using this approach, and how might they be mitigated?
