---
title: "Specify how to generate test code"
description: "Specify how to generate test code, such as the test framework to use and the number of test cases to generate."
category: tests
platforms: [copilot, copilot-chat]
aliases:
  - /doc/tests/specify-test-valiation
---

## Specify How to Generate Test Code

### Description

When it comes to testing, specific instructions can be a great way to make sure you're covering all the necessary scenarios. Instead of giving vague instructions like "add unit tests," you can provide concrete details about the testing frameworks and the number of cases you want to generate. This can be helpful in utilizing tools like GitHub Copilot, where specifying "use NUnit and Moq to add unit tests, testing at least 10 variations of valid and invalid input combinations" can yield a more accurate and comprehensive result.

#### Example

If you are aiming to generate a test code using NUnit and Moq, you can provide the following prompt to GitHub Copilot:

```C#
// Using NUnit and Moq, add unit tests
// Test at least 10 variations of valid and invalid input combinations
[TestFixture]
public void validateInput() {
  // Your code here
}
```

### Exercise

- **Exercise 1**: Write a unit test using NUnit that tests a simple method with 3 different valid inputs.
- **Exercise 2**: Extend the unit test to include 3 different invalid inputs, and verify that exceptions are handled correctly.

### Checklist for Further Learning

- How can you ensure that the tests cover all the critical paths in the code?
- Can you write the test code so that the test always fails?
- What strategies can be used to maintain the tests as the codebase evolves?
