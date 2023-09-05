## <center> Homework Assignement

#### <center> This repository contains a Python Scrapy script. the pupose of this script is to gather information about mobile phones from a website www.productindetail.com and store the data in mongoDB local host database </center>

<hr>
</br>

## <center> Getting started </center>

#### <center> In order to start working with this program it is essential to clone this repository to your local machine. After cloning is completed you may open the project in your desired text editor or ide. </br> Firstly, you must activate virtual enviroment by simply copying path to activate.bat ```venv\Scripts\activate.bat```and imputing it to terminal. After restarting the terminal you will notice ```(venv)``` at the begining of each line.</br> Secondly, you must install libraries from ```requirements.txt``` file by inputing the following command in to terminal ```pip install -r requirements.txt```. </br>  Thirdly, download and install MongoDB in your system and run it. Upon running MongoDB, make sure that server name and port matches variables in file ```ad_scraper\ad_scraper\settings.py``` line 66 to 69</br> Finally, to start webscraping, it's a must to change your working directory to scrapy project folder ```ad_scraper``` by inputing ```cd ad_scraper``` in to the terminal. Now to run the spider you must input ```scrapy crawl phones``` in to the terminal. After scraping is complete you may find all scraped data in mongoDb client ```phone_data``` database in ```phones``` collection.