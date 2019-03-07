# Send To Utils
Utilities for SendTo from Explorer Right Click

## Preparation
1. Locate SendTo folder.
```
C:\Users\<user name>\AppData\Roaming\Microsoft\Windows\SendTo
```
2. Create a batch script in SendTo folder.
```
@echo off
set "Python="<path to>\python.exe""
set "Script="<path to>\<file name>.py""
set "Arg1=%1"
set Statement=%Command% %Script% %Arg1%
%Statement%
pause
```
3. Right click the file in explorer.
4. Select **Send to**.
5. Select the batch script.
