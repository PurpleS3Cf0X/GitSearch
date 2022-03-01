import requests,re
import click
from bs4 import BeautifulSoup
import re
from lxml import html

gitTopic_url="https://github.com/topics/"
@click.command()
@click.option('--topic','-t', help='Enter a single keyword to search a topic')
@click.option('--keys','-k', type=str,help='Search entire github with a keyword or string', multiple=True)
def getMyTopics(topic,keys):
    if topic:
        click.echo(f'Searching for the topic:: {topic}')
        url=gitTopic_url+str(topic)
        res= requests.get(url)
        print(f'making request to {url}')
        if(res.status_code == 200):
            print(f'Connection Successful:: {res.status_code}')
            soup=BeautifulSoup(res.text,"html.parser")
            res=[]
            result=soup.find_all("div", {"class": "d-flex flex-items-center ml-3"})
            if result:
                for count,i in enumerate(result) :
                    count=count+1
                    href= str(i.find('a').get('href'))
                    href=href.replace("/login?return_to=","https://github.com").replace("%2F","/")
                    stars=str(i.find('span',{'id':'repo-stars-counter-star'}).get('aria-label'))
                    results=href+'  , '+stars
                    print(f' Link:{count}: {href} ===> Star(s): {stars}')
            else:
                print("Found no result(s), Please try a different topic")
        else:
            click.echo(f"Getting the followig error:: \n{res.text}")
    elif keys:
        keys="+".join(keys)
        click.echo(f"Searching for the keyword(s):: {keys}")
        url="https://github.com/search?q="+str(keys)
        res=requests.get(url)
        print(f'making request to {url}')
        if(res.status_code == 200):
            soup=BeautifulSoup(res.text,'html.parser')
            result=soup.find_all("div", {"class": "mt-n1 flex-auto"})
            
            for count,i in enumerate(result):
                count=count+1
                href=str(i.find('a').get('href'))
                href="https://github.com"+href
                star=str(i.find('a',{'class':'Link--muted'}))
                pattern="<a.*?>\n<svg.*?>\n<path.*?>\n<\/svg>\n\s+(\d+)\n\s+"
                star=re.findall(pattern, star)
                try:
                    if star ==[]:
                        star="No Stars yet"
                    else:
                        star=star.replace(" ","")
                except (AttributeError, TypeError):
                    pass
                print(f' Link:{count}: {href} ===> Star(s): {star}')
                
        else:
            click.echo(f"Getting the followig error:: \n{res.text}")
if __name__ =='__main__':
    getMyTopics()

