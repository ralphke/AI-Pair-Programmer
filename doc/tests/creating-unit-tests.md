---
title: "Creating unit tests"
description: "Create unit test with GitHub Copilot"
category: tests
platforms: [copilot, copilot-chat]
aliases:
  - /doc/tests/creating-unit-tests
---

## Creating Unit Tests


### Description

Testing is a fundamental part of the software development process, ensuring that the code meets its design and behaves as intended. The creation of unit tests, which test individual components of the system, can be both challenging and time-consuming. With GitHub Copilot, this process becomes more streamlined. Let's explore how a developer named Billy leverages GitHub Copilot to write unit tests for her application, reducing her workload and boosting her efficiency.
This pattern is also applicable to functional and API testing.

#### Example

Billy is working on a C# function that needs to be thoroughly tested. With the help of GitHub Copilot, she can quickly generate the required unit tests.

Here's a simple function she wants to test:

```C#
public static int add(int x, int y) {
  return x + y;
}
```

And here's how she might create a unit test with Copilot's assistance:

```C#
using NUnit.Framework;

[TestFixture]
public class AddTwoNumbersTests
{
    [Test]
    public void AddTwoNumbers_ReturnsSum()
    {
        // Arrange
        int x = 3;
        int y = 7;

        // Act
        int result = AddTwoNumbers(x, y);

        // Assert
        Assert.AreEqual(10, result);
    }
}
```

### Exercise

- **Exercise 1**: Create a unit test for a function that multiplies two numbers using GitHub Copilot.
- **Exercise 2**: Utilize Copilot to create a suite of tests for various edge cases, such as handling null or undefined values.
- **Exercise 3**: Reflect on your current project. Identify a part of the code that lacks testing and create unit tests for it using Copilot.

### Checklist for Further Learning

- How can you make sure you tests are comprehensive and cover all possible scenarios?
- What prompts do you add when GitHub Copilot does not cover a scenario at all?
- How is GitHub Copilot beneficial for other types of testing (E2E testing, integration testing, functional testing, etc.) and how can GitHub Copilot assist you in writing them?
