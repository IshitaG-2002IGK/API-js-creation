import requests
r = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt', stream=True)
## source : https://public.oed.com/blog/words-from-the-21st-century/
wordlist = [
    "automagically",
    "bargainous",
    "big media",
    "bromance"
    "buzzkill",
    "carbon credit",
    "carbon offsetting", 
    "catastrophize", 
    "cheeseball", 
    "chillax", 
    "cool hunter",
    "cougar",
    "eggcorn",
    "flash mob",
    "flyover states",
    "frenemy"
    ]
# Enforce UTF-8 Encoding on the request
if r.encoding is None:
    r.encoding = 'utf-8'
## streams and prints the content
[ print(line) for line in r.iter_lines(decode_unicode=True) if line.lower() in wordlist ]
    
