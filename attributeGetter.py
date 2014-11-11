import os
import xml.etree.ElementTree as et
import csv

myFiles = os.listdir("C:\\Users\\Jake\\GT\\CX 4242\\GoodVibesWorkingFolder\\songXMLfiles")

allSongs = [["Artist","Title","Energy","Liveness","Tempo","Speechiness","Acousticness",
             "Instrumentalness","Duration","Loudness","Valence","Danceability"]]

failedSongs = [["Artist","Title"]]
failedArtists = [["Artist"]]

for i in myFiles:

    artist = i.split(".")[0]

    f = open(i)

    try:

        tree = et.parse(f)

        root = tree.getroot()

        songs = root.findall(".//song")

        for j in songs:
            try:
                title = j.find(".//title").text

                energy = j.find(".//energy").text

                liveness = j.find(".//liveness").text

                tempo = j.find(".//tempo").text

                speechiness = j.find(".//speechiness").text

                acousticness = j.find(".//acousticness").text

                instrumentalness = j.find(".//instrumentalness").text

                duration = j.find(".//duration").text

                loudness = j.find(".//loudness").text

                valence = j.find(".//valence").text

                danceability = j.find(".//danceability").text

                

            except:
                failSongs.append([artist,title])
                continue

            allSongs.append([artist,title,energy,liveness,tempo,speechiness,acousticness,instrumentalness,
                             duration,loudness,valence,danceability])
    except:
        failedArtists.append(artist)

    f.close()


f = open("songAttributes.csv",'w',newline = '')
writer = csv.writer(f)
writer.writerows(allSongs)
f.close()
        
