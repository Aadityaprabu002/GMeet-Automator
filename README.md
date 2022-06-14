# GMeet Automator

## DESCRIPTION:
This tool is used for attending online classes in Google meet by providing the necessary inputs. The tool is used for automating the whole process. It is built on python and uses selenium. Selenium is an open source umbrella project for a range of tools and libraries aimed at supporting browser automation. It provides a playback tool for authoring functional tests across most modern web browsers, without the need to learn a test scripting language.

## Pre requisites
- You need to have browser installed
- You need to have a email without any two step authentication or extra security.
- You need to feed in that day's schedule as an input.

## INSTALLATION AND SETUP:
### Install selenium in Windows or MacOS
- Use pip to install the selenium package. Python 3 has pip available in the standard library. Using pip, you can install selenium like this:

```
pip install selenium
```
### Check your Browser's binary
- Check your browsers binary and download the appropriate browser driver
- In my case its chromium 
```
Version 1.39.122  Chromium: 102.0.5005.115 (Official Build)  (64-bit)
```
- Visit [this link](https://chromedriver.chromium.org/) for downloading chromium drivers
- Download and extract into this tool's folder

### Execution
- Provide the path of your browers's executable file
- Provide the path of your webdriver
- Feed in the inputs 
- Your schedule is ready to go!!!
- The tool automatically logs you into the google meet classroom when it starts and exits when the class is over
- Any fault in attending class, exception message will be popped on discord server and you can go and rectify it
- To change the discord server go to dicordbot.py and change the discord api webhook link to your own server's channel
 

