#CX 4242
#HW1
import time
import xml.etree.ElementTree as etree
import csv
import urllib.request

#Read csv with artists

f = open ('artistTest.csv', "r")
artistList = []
reader = csv.reader(f)
for item in reader:
    artistList.append(item[0])

profileList = []
for artist in artistList:
    print (artist)
    artist = artist.replace(" ","%20")
    try:
        url ="http://developer.echonest.com/api/v4/artist/profile?api_key=PGFLTYOE0WK7P2TN0&name="+artist+"&format=xml&bucket=familiarity&bucket=hotttnesss&bucket=reviews&bucket=genre&bucket=discovery_rank"

        response = urllib.request.urlopen(url)
        tree = etree.parse(response)
        root = tree.getroot()
        for child in root:
            tagList = []
            for tag in child:
                tagList.append(tag)
                
                
    except:
        print("error with url")

    if len(tagList)==7:
##    limit = 0
    ##    reviews = tagList[5]
    ##    reviewList=[]
    ##    for review in reviews:
    ##        aSumList = []
    ##        for x in review:
    ##            aSumList.append(x)
    ##        summary = aSumList[2]
    ##        reviewList.append(summary.text)
    ##        reviewList = reviewList[:3]
    ##            
        genres = tagList[0]
        genreList = []
        for genre in genres:
            for name in genre:
                genreList.append(name.text)
            
        name = tagList[1].text
        discovery_rank = tagList[2].text
        familiarity = tagList[3].text
        hotness = tagList[4].text
        ID = tagList[6].text
        
       
        myDict = {"name":name, "ID":ID,"familiarity":familiarity,"hotness":hotness,"discovery_rank":discovery_rank,"genres":genreList}
        print (myDict)
        profileList.append(myDict)
        time.sleep(2)
print (profileList)

##WRITE OUTPUT TO CSV
##out = open ("outFile.csv", "w", newline = "")
##csvWriter = csv.writer(out)
 
