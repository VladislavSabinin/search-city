import urllib.request
print("Download JP.zip")
print("Process...")
destination = 'JP.zip'
url = 'http://download.geonames.org/export/dump/JP.zip'
urllib.request.urlretrieve(url, destination)
print("Done.")
