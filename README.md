OVERVIEW
================================================================================
readme for scada_sentry.py

Will watch for high/low on pin, send email, flash relay. Designed to connect to audio signal from islanded SCADA enviroment
and send out notifications whan alarm is annunciated. This is done to allow for secure SCADA notifications to off-site personell
without compomising air-gapped enviroment.

File contains notes as well as common commands used. 

TODO
--------------------------------------------------------------------------------
To maintain a true air gap you would need:
1. PLC (Arduino) watching for audio signal to go HIGH; then
2. PLC closes relay to turn on light; then
3. Pi watches for light with photo detector; then
4. Pi sends notification emails and interacts with the Internet.

CONTRIBUTORS
--------------------------------------------------------------------------------
	BRITTANY WILLIAMS (BWILLIAMS@PROVO.ORG)
	21 JAN 2021
	PROJECT START - FILE SCADA_V1.0

CONFIGURATION FILES
================================================================================
.GITIGNORE
--------------------------------------------------------------------------------	
**/logs	Double asterisks are used to match directories anywhere in the repository
*.log	An asterisk matches zero or more characters.
logs/	Using a slash points out that the pattern is a directory. The whole content of any directory with its files and subdirectories in the repository which matches that name will be ignored by Git.
[SOURCE](https://www.w3docs.com/learn-git/gitignore.html)

GIT
--------------------------------------------------------------------------------
`git add --all`
`git status`
`git commit -am "add README.md"`
`git log README.MD`
`git log -p scada_sentry.py`

Get the file back to the way it was:

`git checkout 5fd772a292c019a7cf3012b1156685280d4a7d2d scada_sentry.py`

The file will be restored and you can now commit this change.
`git commit -am 'restore previous version'`

`git remote add origin git@github.com:GitHubUSERNAME/scada_sentry.git`
`git push -u origin master`
`git push origin master`
`git push origin <branch-name>`

AUTOSTART ON BOOT
================================================================================
[source](https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/)

Create A Unit File
`sudo nano /lib/systemd/system/scada_sentry.service`

Copy and paste contents into Unit File
 
```
    [Unit]
    Description=SCADA Sentry Service
    After=multi-user.target

    [Service]
    Type=idle
    ExecStart=/usr/bin/python /home/pi/Voltage.py/scada_sentry.py
    WorkingDirectory=/home/pi
    User=pi

    [Install]
    WantedBy=multi-user.target
```

`ExecStart=/usr/bin/python /home/pi/Voltage.py/scada_sentry.py > /home/pi/Voltage.py/scada_sentry.log 2>&1`

`sudo chmod 644 /lib/systemd/system/scada_sentry.service`

Configure systemd
--------------------------------------------------------------------------------
`sudo systemctl daemon-reload`

`sudo systemctl enable scada_sentry.service`

`sudo reboot`

Check status of your service
--------------------------------------------------------------------------------
`sudo systemctl status scada_sentry.service`


MARKDOWN CHEATSHEET
================================================================================

# Heading H1
## Heading H2
### Heading H3
#### Heading H4
##### Heading H5
###### Heading H6

_italics_
**bold**
**_bold and italics_**
~~strikethrough~~

1. item1	First ordered list item
2. item2	Second ordered list item
⋅⋅1. Item	Ordered sub-list item
* Item		Unordered list item
⋅⋅* Item	Unordered sub-list item

[text link](https://duckduckgo.com)
[text link with title](https://duckduckgo.com "DDG Home")

`code`

``` Code blocks ```

	Code blocks
	can also be
	added using
	spaces.

> Blockquotes
> Blockquotes
>> Nested blockquotes
> Blockquotes

---	horizontal rule
*** horizontal rule
___ horizontal rule
