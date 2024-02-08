import urllib.request

# URL for the Haar Cascade file
url = 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml'

# Download the file
filename, headers = urllib.request.urlretrieve(url, filename='haarcascade_frontalface_default.xml')
print(f"Downloaded: {filename}")
