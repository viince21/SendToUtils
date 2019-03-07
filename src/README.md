# Send To Utils
Utilities for SendTo from Explorer Right Click

## Preparation
1. Locate SendTo folder.
```
C:\Users\<user name>\AppData\Roaming\Microsoft\Windows\SendTo
```
2. Create a batch script in SendTo folder. Arg1 is the file/folder path, passed by SendTo.
```
@echo off
set "Python="<path to>\python.exe""
set "Script="<path to>\<file name>.py""
set "Arg1=%1"
set Statement=%Command% %Script% %Arg1%
%Statement%
pause
```

## How to use
1. Right click the file in explorer.
2. Select **Send to**.
3. Select the batch script.
