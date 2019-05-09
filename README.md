# gitWhisper
> Get the newest emails from code repository results github by tags filtering (Python3 based)


## Instalation

Install python3 and pip3

<pre> sudo apt install python3 </pre>
<pre> sudo apt install python3-pip</pre>

Install the dependencies via pip:

<pre> pip3 install -r requirements.txt </pre>

#### Important

Add you github cookie sessions 
<pre>

_headers_get = {
    "Cookie": "_ga=GA1.2.XXXX.XXXX; _octo=GH1.1.XXXXX.XXXXX; tz=XXX%XX; has_recent_activity=1; _gid=GA1.2.XXX.XXX; _device_id=XXX; user_session=XX-XXX; __Host-user_session_same_site=XXX-X; logged_in=yes; dotcom_user=XXXX; _gh_sess=XXXX%3D%3D--XXX ",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
}
</pre>

Change DB Config (mysql)
<pre>
host="xxxx.xxxx.us-east-1.rds.amazonaws.com"
port=3306
dbname="xxxxx"
user="xxxxx"
password="xxxxxx"
</pre>

Add "Example schema table" in your database
<pre>
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
</pre>

Add Telegram API and Group ID (Optional)
<pre>
telegram_on = True
TOKEN = 'xxxxx:xxxx-xxx'
mi_canal = xxxxxx
</pre>

## Usage
<pre>usage: python3 gitwhisper.py  </pre>
<pre>usage: python3 gitwhisper.py tag1,tag2,tag3 </pre>


## Example
<pre>
python3 gitWhisper.py vodafone,telefonica,orange


  ____ _ _ __        ___     _
 / ___(_) |\ \      / / |__ (_)___ _ __   ___ _ __
| |  _| | __\ \ /\ / /| '_ \| / __| '_ \ / _ \ '__|
| |_| | | |_ \ V  V / | | | | \__ \ |_) |  __/ |
 \____|_|\__| \_/\_/  |_| |_|_|___/ .__/ \___|_|
                                  |_|

vodafone
telefonica
orange
Tag: vodafone
-------
[T-Mobile* Mozilla/* (compatible; MSIE *.*; Windows CE; *)]
Parent=Pocket PC

[Vodafone* Mozilla/* (compatible; MSIE *.*; Windows CE; *)*]
Parent=Pocket PC

['slurp@inktomi.com', 'slurp@inktomi.com', 'vertical-crawl-support@yahoo-inc.com', 'crawler@exactseek.com', 'nhnbot@naver.com', 'bot@bot.bot', 'info@domaincrawler.com', 'lorkyll@444.net', 'support@meta-spinner.de', 'AlgoFeedback@miva.com', 'crawl@kyluka.com', 'andreas.heidoetting@thomson-webcast.net', 'crawler@pdfind.com', 'admin@google.com', 'shelob@gmx.net', 'tspyyp@tom.com', 'tspyyp@tom.com', 'crawler@www.fi', 'crawler@ah-ha.com', 'gazz@nttr.co.jp', 'knight@zook.in', 'noc@opendns.com', 'support@blogpulse.com', 'crawler_admin@podtech.net', 'support@tumblr.com', 'graeme@inclue.com', 'leehyun@cs.toronto.edu', 'gue@cis.uni-muenchen.de', 'sitemonitor@dnsvr.com', 'BecomeBot@exava.com', 'Exabot@exava.com', 'info@netcraft.com']
https://raw.githubusercontent.com/pauldyatlov/GOG_TowerDefence/20eb2c7bd111af9bf621d50adbe0985c58e89f0e/GOG_TowerDefence/Build/30-03_Data/Mono/etc/mono/browscap.ini
-------
[T-Mobile* Mozilla/* (compatible; MSIE *.*; Windows CE; *)]
Parent=Pocket PC

[Vodafone* Mozilla/* (compatible; MSIE *.*; Windows CE; *)*]
Parent=Pocket PC

['slurp@inktomi.com', 'slurp@inktomi.com', 'vertical-crawl-support@yahoo-inc.com', 'crawler@exactseek.com', 'nhnbot@naver.com', 'bot@bot.bot', 'info@domaincrawler.com', 'lorkyll@444.net', 'support@meta-spinner.de', 'AlgoFeedback@miva.com', 'crawl@kyluka.com', 'andreas.heidoetting@thomson-webcast.net', 'crawler@pdfind.com', 'admin@google.com', 'shelob@gmx.net', 'tspyyp@tom.com', 'tspyyp@tom.com', 'crawler@www.fi', 'crawler@ah-ha.com', 'gazz@nttr.co.jp', 'knight@zook.in', 'noc@opendns.com', 'support@blogpulse.com', 'crawler_admin@podtech.net', 'support@tumblr.com', 'graeme@inclue.com', 'leehyun@cs.toronto.edu', 'gue@cis.uni-muenchen.de', 'sitemonitor@dnsvr.com', 'BecomeBot@exava.com', 'Exabot@exava.com', 'info@netcraft.com']
https://raw.githubusercontent.com/WeiChengTseng/DL_final_project/347aaacc2ec3f79191bad82d4a2bed06d3f2a8c5/env/Soccer.app/Contents/MonoBleedingEdge/etc/mono/browscap.ini
