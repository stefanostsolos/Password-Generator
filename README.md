# Password Generator
## About
Generate a password and see its strength after selecting number of words, numbers and special characters. Using ```passwordmeter, requests, secrets``` modules.
## Installation
Install the required python packages with ```pip install passwordmeter requests secrets``` 
The file that contains all english words (words.txt) is downloaded through the script using the ```requests``` module, but you can access it from https://raw.githubusercontent.com/stefanostsolos/Password-Generator/master/words.txt?token=AKO2DVZYSUG2SOVWG5ZLBM25XR442
## Usage
Specify the number of desired words, numbers and/or special characters to be randomly choosed for the password. Then the passsword is generated, followed by its strength. Password's strength is calculated using ```passwordmeter``` module.
