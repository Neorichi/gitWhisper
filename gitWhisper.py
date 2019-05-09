# -*- coding: utf-8 -*-
import bs4, requests,re, sys
import pymysql
import datetime
import time
import json
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup
import pyfiglet


#### Global ####
#Tags to search
tags = []
#Time to waint betewen request tag
time_tag = 10
git remote add origin https://github.com/Neorichi/gitWhisper

#### Session GitHub ####
#Change the cookie for you github cookie session
_headers_get = {
    "Cookie": "_ga=GA1.2.XXXX.XXXX; _octo=GH1.1.XXXXX.XXXXX; tz=XXX%XX; has_recent_activity=1; _gid=GA1.2.XXX.XXX; _device_id=XXX; user_session=XX-XXX; __Host-user_session_same_site=XXX-X; logged_in=yes; dotcom_user=XXXX; _gh_sess=XXXX%3D%3D--XXX ",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
}

#### DB Config ####
host="xxxx.xxxx.us-east-1.rds.amazonaws.com"
port=3306
dbname="xxxxx"
user="xxxxx"
password="xxxxxx"

#Example schema table
'''
CREATE TABLE `github` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(250) COLLATE utf8_bin DEFAULT NULL,
  `url` varchar(250) COLLATE utf8_bin NOT NULL,
  `file` varchar(250) COLLATE utf8_bin NOT NULL,
  `emails` blob,
  `html` blob,
  `lines_emails` blob,
  `label` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
'''


#### Telegram Config #### [Optional]
telegram_on = False
TOKEN = 'xxxxx:xxxx-xxx'
mi_canal = xxxxxx




def addslashes(s):
    return s.replace("'", '"')

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def search_email(target_url):
    result = requests.get(
        target_url,
        headers=_headers_get
    )
    regex = r"[\w.%+-]+@(?:[a-z\d-]+\.)+[a-z]{2,4}"
    c = result.content
    emails = re.findall(regex, str(c))
    lines = re.sub("<.*?>", " ", result.text)
    regex = r"[\w.%+-]+@(?:[a-z\d-]+\.)+[a-z]{2,4}.{0,30}"
    lines = re.findall(regex, lines)
    return emails,lines


def get_github_email(page,search,conn):
    if telegram_on:
        mi_bot = telegram.Bot(token=TOKEN)
        mi_bot_updater = Updater(mi_bot.token)

    result = requests.get(
        "https://github.com/search?o=desc&p=%d&q=%s&s=indexed&type=Code" % (page, search),
        headers=_headers_get
    )
    c = result.content
    soup = bs4.BeautifulSoup(c, "html.parser")
    for div in soup.find_all("div", {"class":"code-list-item"}):
        div_flex = div.find("div", {"class":"flex-auto"})
        div_highlight = div.find("table", {"class":"highlight"})
        div_highlights = div_highlight.find_all("td", {"class":"blob-code-inner"})
        div_highlights_text = ""
        for value in div_highlights:
            div_highlights_text = div_highlights_text + cleanhtml(value.get_text().replace("\n", ""))+"\n"

        div_highlight = div_highlight.text
        title = div_flex.find_all("a")[0]
        title = title.text
        url = div_flex.find_all("a")[1]
        title_url = str(url.text)

        src = str("https://raw.githubusercontent.com"+url['href'].replace("/blob", ""))
        emails,lines = search_email(src)
        emails_json = addslashes(str(json.dumps(emails)))
        lines_json = addslashes(str(json.dumps(lines)))

        if (search in emails or len(emails)>3):
            with conn.cursor() as cur:
                exist = cur.execute('select title from github where title ="%s" LIMIT 1' % title)
                if exist==0:
                    print("-------")
                    #print("https://github.com/search?o=desc&p=%d&q=%s&s=indexed&type=Code" % (page, search))
                    print(div_highlights_text)
                    print(emails)
                    print(src)
                    if telegram_on:
                        try:
                            mi_bot.sendMessage(chat_id=mi_canal, text="--------"+datetime.datetime.now().strftime("%H:%M %d/%m/%y")+"-----"+search+"------")
                            mi_bot.sendMessage(chat_id=mi_canal, text=("%s" % (title[0:300])))
                            mi_bot.sendMessage(chat_id=mi_canal, text=("%s" % (src[0:300])))
                            mi_bot.sendMessage(chat_id=mi_canal, text=("%s" % addslashes(div_highlights_text)[0:300]))
                            mi_bot.sendMessage(chat_id=mi_canal, text=("%s" % str(emails)[0:300]))
                            mi_bot.sendMessage(chat_id=mi_canal, text=("%s" % str(lines)[0:300]))
                            if "password" in div_highlight:
                                mi_bot.sendMessage(chat_id=mi_canal, text=("Aparece la palabra password"))
                        except Exception as e:
                            pass

                    div_highlight_encoded = json.dumps(addslashes(div_highlight))
                    cur.execute("insert into github (title, url, file, emails, html,lines_emails,label) values('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (title,src,title_url,emails_json,div_highlight_encoded,lines_json,str(search)))


def main():
    ascii_banner = pyfiglet.figlet_format("GitWhisper")
    print("\n"+ascii_banner)
    conn = pymysql.connect(host, user=user,port=port,passwd=password, db=dbname)
    try:
        tags_sys = str(sys.argv[1])
        if tags_sys:
            tags.clear()
            tags_ = str(tags_sys)
            tags_ = tags_.split(",")
            for value in tags_:
                tags.append(value)

    except Exception as e:
        pass


    while True:
        for tag in tags:
            print("Tag: %s" % tag)

            # Search first page = 1
            get_github_email(1,tag,conn)
            conn.commit()
            time.sleep(time_tag)


if __name__ == "__main__":
    main()
