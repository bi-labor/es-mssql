# Exercise 1: Get the starter solution

1. Open the following URL: <https://classroom.github.com/a/7F0NBJ2F>

1. Log in with your GitHub account. If you do not have one, register one now.

1. Click the _Accept this assignment_ button.

1. Wait for the Git repository to initialize.

   > Please note that your repository is private. No one has access to it, but you, and the teachers.

1. Check out the repository with your favorite tool. Work in the `c:\work\<neptun>` directory. If you do not have a favorite git tool, follow these steps:

   1. Create a folder where you will work, e.g. `c:\work\<neptun>\mssql-lab`
   1. Open a console to this location
   1. Execute the following command: `git clone <repository-url> .`
      - In the university laboratories, this should ask for your credentials. If there is no login window, the clone will likely fail. Follow the instructions at the end of this page to remove existing GitHub credentials.

1. Open the checked out folder, and type your NEPTUN code into the `neptun.txt` file. We need this to map your submission to you.

   > Open `neptun.txt` and type your NEPTUN code in the file.

1. Go to the `data` folder and extract the zip file.

1. Open the CSV files to check their contents.

## Next exercise

Read the submission guide below, then proceed with the exercises.

Next is [exercise 2](exercise2.md).

## Submitting your solution

When you are finished, submit your solution by pushing the changes to the remote Git repository.

### Verify that you submit the necessary files

1. Check if `neptun.txt` contains your Neptun code.
1. Execute `check-submission.ps1` with PowerShell to get basic feedback whether the required files are found.

### Commit and push your work

If you do not have a favorite git tool, execute the following commands in a console window in the same directory where your files are.

```bash
git add -A
git commit -m "MSSQL laboratory solutions"
git push
```

To verify that you have uploaded everything, open the repository online and check its contents.

### Remove GitHub credentials

In the university laboratories, the computer may remember your login information. To remove your credentials, follow these steps.

1. Open `Credential Manager` from the Start menu.
1. Look for GitHub tokens in the `Windows Credentials` page, and remove all of them.
   ![Remove existing GitHub access token](images/git-credential-remove.png)
