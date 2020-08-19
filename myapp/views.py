from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
import datetime
# Create your views here.

def main(request):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=수출입",headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text, "html.parser")
    articles = html.select("ul.type01 > li")
    time = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    
    newslist=[]
    print("갱신시각:", time)

    for ar in articles:
        title = ar.select_one("a._sp_each_title").text  #title
        source = ar.select_one("span._sp_each_source").text #요약
        link = ar.select_one("a").attrs['href'] #하이퍼링크 
        update = ar.select_one("dd.txt_inline").text.split(" ")
        dic ={'title':title,'source':source,'link':link,'update':update}
        newslist.append(dic)
        
        print(dic)

    if request.method=="POST":
        default_news=request.POST['sel_chart']
        if default_news == '수출입':
            raw = requests.get("https://search.naver.com/search.naver?where=news&query="+default_news,headers={'User-Agent':'Mozilla/5.0'})
            html = BeautifulSoup(raw.text, "html.parser")
            articles = html.select("ul.type01 > li")
            time = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    
            newslist=[]
            print("갱신시각:", time)

            for ar in articles:
                title = ar.select_one("a._sp_each_title").text  #title
                source = ar.select_one("span._sp_each_source").text #요약
                link = ar.select_one("a").attrs['href'] #하이퍼링크 
                update = ar.select_one("dd.txt_inline").text.split(" ")
                dic ={'title':title,'source':source,'link':link,'update':update}
                newslist.append(dic)
        
                print(dic)
            return render(request,'main.html',{'newslist':newslist,'time':time,'default_news':default_news})
        else :
            raw = requests.get("https://search.naver.com/search.naver?where=news&query="+default_news,headers={'User-Agent':'Mozilla/5.0'})
            html = BeautifulSoup(raw.text, "html.parser")
            articles = html.select("ul.type01 > li")
            time = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    
            newslist=[]
            print("갱신시각:", time)

            for ar in articles:
                title = ar.select_one("a._sp_each_title").text  #title
                source = ar.select_one("span._sp_each_source").text #요약
                link = ar.select_one("a").attrs['href'] #하이퍼링크 
                update = ar.select_one("dd.txt_inline").text.split(" ")
                dic ={'title':title,'source':source,'link':link,'update':update}
                newslist.append(dic)
        
                print(dic)
            return render(request,'main.html',{'newslist':newslist,'time':time,'default_news':default_news})
        
    else :
        return render(request,'main.html',{'newslist':newslist,'time':time})


def news(request):
    if request.method=="POST":
        news_search = request.POST['news_search']
        raw = requests.get("https://search.naver.com/search.naver?where=news&query="+news_search,headers={'User-Agent':'Mozilla/5.0'})
        html = BeautifulSoup(raw.text, "html.parser")
        articles = html.select("ul.type01 > li")
        time = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    
        newslist=[]
        print("갱신시각:", time)

        for ar in articles:
            title = ar.select_one("a._sp_each_title").text  #title
            source = ar.select_one("span._sp_each_source").text #요약
            link = ar.select_one("a").attrs['href'] #하이퍼링크 
            update = ar.select_one("dd.txt_inline").text.split(" ")
            dic ={'title':title,'source':source,'link':link,'update':update}
            newslist.append(dic)
        
            print(dic)
        return render(request,'main.html',{'newslist':newslist,'time':time})
    else :
        return render(request,'main.html')

def main1(request):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=수출입",headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text, "html.parser")
    articles = html.select("ul.type01 > li")
    time = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    
    newslist=[]
    print("갱신시각:", time)

    for ar in articles:
        title = ar.select_one("a._sp_each_title").text  #title
        source = ar.select_one("span._sp_each_source").text #요약
        link = ar.select_one("a").attrs['href'] #하이퍼링크 
        update = ar.select_one("dd.txt_inline").text.split(" ")
        dic ={'title':title,'source':source,'link':link,'update':update}
        newslist.append(dic)
        
        print(dic)

    if request.method=="POST":
        default_news=request.POST['sel_chart']
        if default_news == '수출입':
            raw = requests.get("https://search.naver.com/search.naver?where=news&query="+default_news,headers={'User-Agent':'Mozilla/5.0'})
            html = BeautifulSoup(raw.text, "html.parser")
            articles = html.select("ul.type01 > li")
            time = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    
            newslist=[]
            print("갱신시각:", time)

            for ar in articles:
                title = ar.select_one("a._sp_each_title").text  #title
                source = ar.select_one("span._sp_each_source").text #요약
                link = ar.select_one("a").attrs['href'] #하이퍼링크 
                update = ar.select_one("dd.txt_inline").text.split(" ")
                dic ={'title':title,'source':source,'link':link,'update':update}
                newslist.append(dic)
        
                print(dic)
            return render(request,'main1.html',{'newslist':newslist,'time':time,'default_news':default_news})
        else :
            raw = requests.get("https://search.naver.com/search.naver?where=news&query="+default_news,headers={'User-Agent':'Mozilla/5.0'})
            html = BeautifulSoup(raw.text, "html.parser")
            articles = html.select("ul.type01 > li")
            time = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    
            newslist=[]
            print("갱신시각:", time)

            for ar in articles:
                title = ar.select_one("a._sp_each_title").text  #title
                source = ar.select_one("span._sp_each_source").text #요약
                link = ar.select_one("a").attrs['href'] #하이퍼링크 
                update = ar.select_one("dd.txt_inline").text.split(" ")
                dic ={'title':title,'source':source,'link':link,'update':update}
                newslist.append(dic)
        
                print(dic)
            return render(request,'main1.html',{'newslist':newslist,'time':time,'default_news':default_news})
        
    else :
        return render(request,'main1.html',{'newslist':newslist,'time':time})


def news1(request):
    if request.method=="POST":
        news_search = request.POST['news_search']
        raw = requests.get("https://search.naver.com/search.naver?where=news&query="+news_search,headers={'User-Agent':'Mozilla/5.0'})
        html = BeautifulSoup(raw.text, "html.parser")
        articles = html.select("ul.type01 > li")
        time = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    
        newslist=[]
        print("갱신시각:", time)

        for ar in articles:
            title = ar.select_one("a._sp_each_title").text  #title
            source = ar.select_one("span._sp_each_source").text #요약
            link = ar.select_one("a").attrs['href'] #하이퍼링크 
            update = ar.select_one("dd.txt_inline").text.split(" ")
            dic ={'title':title,'source':source,'link':link,'update':update}
            newslist.append(dic)
        
            print(dic)
        return render(request,'main1.html',{'newslist':newslist,'time':time})
    else :
        return render(request,'main1.html')
