# Get started with GitHub CLI
### Install GitHub CLI via Winget:
```console
winget install -q "GitHub CLI"
````
### Log with GitHub CLI into Github
```console
gh auth login 
````
### Load the extention for Github CLI
```console
gh extension install github/gh-copilot
````
### Configure Copilot for GH CLI
```console
gh copilot enable
````

## Use Github Copilot Command Line Interface (CLI)

Ask Copilot about specific commands and tools
```console
gh copilot explain “winget install”
```
Get suggestions
```console
gh copilot suggest “install git”
```
Setup alias for
```console
gh copilot suggest – ghcs
gh copilot explain - ghce
gh copilot alias
```
Context variables
```console
@workspace #FileName.cs
@vscode  - How to do something inside VS code
@terminal – review 
```
Add commit messages

## GitHub CoPilot for CLI configuration
```console
&"c:/Program Files/Git/gh.exe" auth login --web -h github.com   
What is your preferred protocol for Git operations on this host? **HTTPS**  
Authenticate Git with your GitHub credentials? **Yes**
First copy your one-time code: **X1Y2-Z3A4**
Press Enter to open github.com in your browser...✓ Authentication complete. 
gh config set -h github.com git_protocol https✓
Configured git protocol✓ 
Logged in as Clippy! 
```
