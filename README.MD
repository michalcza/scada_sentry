
**/logs	Double asterisks are used to match directories anywhere in the repository
*.log	An asterisk matches zero or more characters.
logs/	Using a slash points out that the pattern is a directory. The whole content of any directory with its files and subdirectories in the repository which matches that name will be ignored by Git.
https://www.w3docs.com/learn-git/gitignore.html

git add --all
git status
git commit -am "add README.md"
git log README.MD
git log -p snitch-sniffer.py would have actually shown the changed contents of the file, if the commit message wasn’t clear enough.

You can now get back the version of the file from the commit before. The long string of characters after the word ‘commit’ is called a hash, and is used by Git to keep track of files. In this case, the commit that needs to be restored is 5fd772a292c019a7cf3012b1156685280d4a7d2d. So typing the following will get the file back to the way it was:

git checkout 5fd772a292c019a7cf3012b1156685280d4a7d2d snitch-sniffer.py
The file will be restored and you can now commit this change.

git commit -am 'restore find function'

git remote add origin git@github.com:HarryPotter/snitch-sniffer.git
git push -u origin master
git push origin master
git push origin <branch-name>

