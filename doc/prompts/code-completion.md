---
title: "Code Completion"
description: "Simple code completion with GitHub Copilot"
category: prompts
platforms: [copilot, copilot-chat]
aliases:
  - /doc/prompts/code-completion
---

## Code Completion

### Description

One of the simplest uses of GitHub Copilot is code completion. Code completion enhances developer productivity by offering potential code snippets as the developer is typing. For example, imagine defining a function in C#. As you input the code below, GitHub Copilot will suggest potential code that could be used inside the function, such as the following code.

#### Example

##### Input Code

```C#
public static double calculateSum(a, b) {
    // Enter your code here
}
```

##### Result Suggested by Copilot

```C#
public static double calculateSum(double a, double b) {
  // Enter your code here
  double sum = a + b;
  return sum;
}
```

### Exerecise

- **Exercise 1**: Complete the `calculateSum(a, b)` function by utilizing GitHub Copilot's suggestions. Explore how different prompts or partial code inputs influence the suggestions made by Copilot.

### Checklist for Further Learning

- Did your code output resemble the sample code provided?
- Is the outputted code robust? Is error handling considered? If not, how could you improve the code?
- What prompts or context can you add to write more precise code?
