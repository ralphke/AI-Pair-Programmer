---
title: "Comment to Code"
description: "Generate code from comments with GitHub Copilot"
category: prompts
platforms: [copilot, copilot-chat]
aliases:
  - /doc/prompts/comment-to-code
---

## Comment to Code Generation

### Description

GitHub Copilot is capable of generating new code based on the specific text provided by a developer. By defining conditions in the form of comments, GitHub Copilot can create code that responds to the requirements.

#### Example

Here's a way to instruct GitHub Copilot to create a function through comments:

```C#
// Function name: calculateAverage
// Function arguments: numbers (array)
// Return type of the function: number
```

Based on these comments, Copilot might suggest the following code:

```C#
public double calculateAverage(double[] numbers)
{
    // TODO: Implement the logic to calculate the average of the numbers array
    double sum = 0;
    foreach (double number in numbers)
    {
        sum += number;
    }
    double average = sum / numbers.Length;
    return average;
}
```

### Exerecise

- **Exercise 1**: Write the comments to instruct Copilot to create a function that calculates the maximum number in an array. Use the following specification:

```C#
// Function name: calculateMax
// Function arguments: numbers (array)
// Return type of the function: number
```

- **Exercise 2**: Test the generated function with different sets of numbers and verify if it returns the correct maximum value.

### Checklist for Further Learning

- Is the generated code based on the specified conditions?
- Is the functionality of the code correctly implemented?
- What is the appropriate way to write comments for more complex condition definitions?
- To give more context, try using the OS dictation functionality as well as the keyboard.
