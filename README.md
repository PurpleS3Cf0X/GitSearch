# GitSearch
Python Script to search the git for topics

The python script has been tested and requires no API and it is basic scraping

## Requirement(s):
Packages:
1. Regex :: Use Command => pip install regex
2. BeautifulSoup :: Use Command =>  pip install beautifulsoup4
3. Requests :: Use Command =>  pip install requests
4. Click :: Use Command =>  pip install click


## For Help:
Use Command => python3 gitSearch.py --help

![image](https://user-images.githubusercontent.com/19497281/156170713-450748bd-dd09-4403-9df7-af2ce3c6ca9c.png)


## Searching for Topic:
Note: Only one single string/Keyword can be searched 

Use Command => python3 gitSearch.py -t [Keyword]  Example: python3 gitSearch.py -t ukraine

![image](https://user-images.githubusercontent.com/19497281/156170095-95b452d6-85eb-43fd-b17c-2a53ec6b217b.png)

## Searching with multiple keyword(s):
Note: Keep Adding '-k' for more keywords

Use Command => Example: python3 gitSearch.py -k ukraine -k iocs

![image](https://user-images.githubusercontent.com/19497281/156171049-d9394d5d-9e27-4995-88c9-4d1e84acfca0.png)


