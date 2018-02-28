import exifread
import os

count=0
def _convert_to_degress(value):

    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)

    return d + (m / 60.0) + (s / 3600.0)

#your directory path where images exist
dir="path for folder which has images"

#file to output the geotag of each image
file_to_write=open("(with path of file )file name ( this file is used in next stage )",'w')

#dont change anything below this line



directory = os.listdir(dir)

for files in directory:
    file_path = os.path.join(dir, files)
    count+=1
    f = open(file_path, 'rb')
    tags = exifread.process_file(f)
    lat =None
    lon=None
    for tag in tags.keys():
        if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            if tag == 'GPS GPSLatitudeRef':
                gps_latitude_ref = tags[tag]
            elif tag == 'GPS GPSLatitude':
                gps_latitude = tags[tag]
            elif tag == 'GPS GPSLongitudeRef':
                gps_longitude_ref = tags[tag]
            elif tag == 'GPS GPSLongitude':
                gps_longitude = tags[tag]

    if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
        lat = _convert_to_degress(gps_latitude)
        if gps_latitude_ref.values[0] != 'N':
            lat = 0 - lat

        lon = _convert_to_degress(gps_longitude)
        if gps_longitude_ref.values[0] != 'E':
            lon = 0 - lon
    a=str(lat)+","+str(lon)+","+str(files)+","
    file_to_write.write(a)
file_to_write.close()
print(count)


######################################################################


