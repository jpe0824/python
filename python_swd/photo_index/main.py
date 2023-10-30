import os
import exifread
import reverse_geocoder as rg

def traverse_directory(path):
    for entry in os.scandir(path):
        if entry.is_dir():
            traverse_directory(entry.path)
        elif entry.is_file():
            if entry.name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                process_image(entry.path)

def process_image(path):
    with open(path, 'rb') as f:
        tags = exifread.process_file(f)
        timestamp = tags.get('Image DateTime')
        lat_ref = tags.get('GPS GPSLatitudeRef')
        lat = tags.get('GPS GPSLatitude')
        lon_ref = tags.get('GPS GPSLongitudeRef')
        lon = tags.get('GPS GPSLongitude')
        if lat and lon:
            location = get_location(lat, lon, lat_ref, lon_ref)
        else:
            location = None
        dir_path = os.path.dirname(path)
        generate_html(dir_path, path, timestamp, location)

def dms_to_dd(dms, ref):
    degrees, minutes, seconds = dms.values
    if isinstance(seconds, exifread.utils.Ratio):
        seconds = seconds.num / seconds.den
    dd = (degrees) + (minutes)/60 + (seconds)/3600
    if ref in ['S', 'W']:
        dd *= -1
    return dd

def get_location(lat, lon, lat_ref, lon_ref):
    lat_dd = dms_to_dd(lat, lat_ref)
    lon_dd = dms_to_dd(lon, lon_ref)

    results = rg.search((lat_dd, lon_dd))

    location = f"{results[0]['name']}, {results[0]['admin1']}, {results[0]['cc']}"
    return location

def generate_html(dir_path, image_path, timestamp = None, location = None):
    relative_image_path = os.path.relpath(image_path, dir_path)

    html_file_path = os.path.join(dir_path, "index.html")
    if not os.path.exists(html_file_path):
        with open(html_file_path, 'w') as f:
            f.write('<html>\n<head>\n<title>Image Index</title>\n</head>\n<body>\n')

            for entry in os.listdir(dir_path):
                if os.path.isdir(os.path.join(dir_path, entry)):
                    f.write('<a href="' + entry + '/index.html">' + entry + '</a>\n')
            f.write('<h1>' + os.path.basename(image_path) + '</h1>\n')
            f.write('<img src="' + relative_image_path + '" alt="Image">\n')
            f.write('<p>' + os.path.basename(image_path) + '</p>\n')
            if timestamp:
                f.write('<p>' + str(timestamp) + '</p>\n')
            if location:
                f.write('<p>' + location + '</p>\n')
            f.write('</body>\n</html>')
    else:
        with open(html_file_path, 'a') as f:
            f.write('<h1>' + os.path.basename(image_path) + '</h1>\n')
            f.write('<img src="' + relative_image_path + '" alt="Image">\n')
            f.write('<p>' + os.path.basename(image_path) + '</p>\n')
            if timestamp:
                f.write('<p>' + str(timestamp) + '</p>\n')
            if location:
                f.write('<p>' + location + '</p>\n')

if __name__ == '__main__':
    traverse_directory('.\Pictures')