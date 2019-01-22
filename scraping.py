from bs4 import BeautifulSoup
import requests
import csv


### get the text of the website with get function of requests module
source = requests.get('http://coreyms.com/category/development/git').text

# make the text source in html format with BeautifulSoup class
soup = BeautifulSoup(source, 'lxml')

# creating a csv file 'coryWebsiteScraping.csv' with write mode
csv_file = open('coryWebsiteScraping.csv', 'w')

# setting the pointer in the file and creating the column name
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

# find the article from webpage
for article in soup.find_all('article'):

    #print(article.prettify())

    # get the headline of each article
    headline = article.h2.a.text
    print(headline)

    # get the text of article with div & tag search
    summary = article.find('div', class_='entry-content').p.text
    print(summary)




    # Using try-except block to handle error is the data isn't there or missing.
    try:
        # get the video link from iframe and process the id of the video
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        # prepare the youtube link with the id from iframe
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    # writing the date in the csv file
    csv_writer.writerow([headline, summary, yt_link])

# closing the csv file with best practise
csv_file.close()
