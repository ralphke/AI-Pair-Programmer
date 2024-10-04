# Visual Studio 2022 Copilot >= Version 17.9

* [Github Copilot](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-extension?view=vs-2022)

* [GitHub Copilot Chat Extenstions](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-chat?view=vs-2022)

* [Getting started with GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/getting-started-with-github-copilot)

* [Check out diffrences to IntelliCode](https://learn.microsoft.com/en-us/visualstudio/ide/ai-assisted-development-visual-studio?view=vs-2022#ai-capabilities-side-by-side)

An alternative to the native Github Copilot:

* Visual Studio Marketplace: [Visual chatGPT Studio](https://marketplace.visualstudio.com/items?itemName=jefferson-pires.VisualChatGPTStudio)
* GitHub VisualChatGPTStudio: [Add chatGPT functionalities directly on Visual Studio (github.com)](https://github.com/jeffdapaz/VisualChatGPTStudio)

Inline Chat via key: **Alt-#**

/-Commands:
```
/doc |  /explain | /fix | /optimize | /tests
```

Context variable

```console
#solution #FileName.cs
```
Analyze and Fix in Test Explorer

## /-Commands in Copilot Inline & Chat 

| Command | Description | Example | Output |
|---------|-------------|---------|--------|
| /doc    | Provides documentation for a specific code or function | `/doc print` | Documentation for print function |
| /explain| Explains the current line of code | `/explain` | Explanation of the current line |
| /fix    | Suggests a fix for the current line of code | `/fix` | Suggested fix for the current line |
| /optimize | Suggests an optimization for the current line of code | `/optimize` | Suggested optimization for the current line |
| /tests  | Generates test cases for the current function | `/tests` | Generated test cases for the current function |

Where Copilot can help:
```markdown
- Exception Analysis with Copilot
- Auto Insight with Profiling Tools
- Rename suggestions (Refactoring)
- Commit messages auto generated 
- Breakpoint Expressions with IntelliSense
- Deadlock Analysis
```

/-Command only in Chat: 

```console
/askvs
/generate
```