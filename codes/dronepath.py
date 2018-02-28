import pysrt
subs = pysrt.open('path for srt file', encoding='iso-8859-1')
drone=open('file name with path for coordinates of drone from srt file','w')
drone.write(str("Latitude")+","+str("Longitude")+"\n")
for each in range(0,len(subs)):
    s=subs[each].text.split(",")
    drone.write(str(s[1])+","+str(s[0])+"\n")