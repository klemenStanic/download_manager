# Download manager (MAC)

This is a personal repository.
This simple script takes the new downloaded files in the Downloads folder and
organizes them into folders, named by the file's mime type. 

Make sure to change the Downloads folder path in script and plist file.

To autorun at startup and in background, copy the `com.klemenstanic.osx.download_manager.plist` to the `~/Library/LaunchAgents/com.klemenstanic.osx.download_manager.plist` and run:

```
launchctl load ~/Library/LaunchAgents/com.klemenstanic.osx.download_manager.plist 
```