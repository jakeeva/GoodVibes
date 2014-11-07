#Song XML info getter

#import relevant modules
import csv
import time
import xml.etree.ElementTree as etree
import urllib.request
import time


#open artist CSV
f = open("artists.csv")

#create CSV reader object
reader = csv.reader(f)

#loop through reader object and grab artist names
allArtists = []
for artist in reader:
    allArtists.append(artist[0])

f.close()

xmlCount = 0
failedArtists = []
#loop through all artist names
for artist in allArtists:
    artist = artist.replace(" ","%20")
    #build relevant query for each artist
    query = "http://developer.echonest.com/api/v4/song/search?api_key=H0QIAQ1LC7ELW8V75&format=xml&artist="+artist+"&bucket=audio_summary&results=100"

    #write XML output
    try:
        response = urllib.request.urlopen(query)
        tree = etree.parse(response)
        artist = artist.replace("%20"," ")
        tree.write(artist+".xml", "UTF-8")
        xmlCount += 1
    #if xml generation fails, add artist to failed artist list
    except:
        artist = artist.replace("%20"," ")
        failedArtists.append([artist])

    #wait 3 seconds between each query to avoid hitting EchoNest request limit
    time.sleep(3)

#write out failed artists csv
f = open("failedArtists.csv",'w')
writer = csv.writer(f, lineterminator = '\n')
writer.writerows(failedArtists)
f.close()
