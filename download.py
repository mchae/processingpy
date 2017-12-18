import requests
url = 'https://raw.githubusercontent.com/fluolabs/processingpy/master/fluopy.py'
r = requests.get(url, allow_redirects=True)
open('C:\\Users\\Minho Chae\\Documents\\Processing\\libraries\\site-packages\\fluopy.py', 'wb').write(r.content)
