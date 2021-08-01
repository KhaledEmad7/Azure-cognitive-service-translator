

# About the app
This app uses **Azure cognitive service** and **Python3** To translate a text form any desired language to any choosen list of languages.

# Quick start 
- ## Installation
    - First install **python3** from [here](https://www.python.org/downloads/)
    - Then install **requests** from terminal:\
    `pip install requests`
    - Then install **uuid** from terminal:\
    `pip install uuid`
    - Now open the code and add your subscription key in line 4
    - Also add your Region in line 9

- ## Start the app
	First you need to start the app by running:\
	`python3 translate.js`\
	Or you can simply use a python IDE and run the translate.py file from it\
  Now simply enter the text matching the language in **params>from**.
    
- ## Inside the app   
   ```
   params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['ar', 'de', 'fr']
    }
   ```
    1- in **params>from** you can change the language of the input text\
    2- in **params>to** you can add as many languages as you want to translate the text into it\
    Here is the [list](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/language-support) of languages to choose from
