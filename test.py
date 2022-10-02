
from app import write



r = write(query="love").encode('utf-8')
print(r)
#resp = requests.post("https://paste.rs/", r)
    #r = resp.text
print(r)
r = r.replace('/n', '<br>')
 