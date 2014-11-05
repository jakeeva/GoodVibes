#Song XML info getter

#import relevant modules
import csv
import time
import xml.etree.ElementTree as etree
import urllib.request
import time


#open artist CSV
f = open("artistTest.csv")

#create CSV reader object
reader = csv.reader(f)

#loop through reader object and grab artist names
allArtists = []
for artist in reader:
    allArtists.append(artist[0])

xmlCount = 0
#loop through all artist names
for artist in allArtists:
    artist = artist.replace(" ","%20")
    #build relevant query for each artist
    query = "http://developer.echonest.com/api/v4/song/search?api_key=H0QIAQ1LC7ELW8V75&format=xml&artist="+artist+"&bucket=audio_summary&results=100"

    #write XML output
    response = urllib.request.urlopen(query)
    tree = etree.parse(response)
    artist = artist.replace("%20"," ")
    tree.write(artist+".xml", "UTF-8")
    xmlCount += 1
    time.sleep(3)
    print(str(xmlCount)+"\t"+artist)
    
    
    
