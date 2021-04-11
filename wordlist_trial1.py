import requests
r = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt', stream=True)
## source : https://public.oed.com/blog/words-from-the-21st-century/
wordlist = [
    "anthropocene",
    "twiterrati",
    "defriended",
    "retweeted",
    "hashtag",
    "youtubers",
    "podcast",
    "vlog",
    "binge-watch",
    "blu-ray",
    "selfies",
    "selfie stick",
    "photobomb",
    "flash mob",
    "crowdfunding",
    "happy slapping",
    "parkour",
    "free running",
    "Sudoku",
    "glamping",
    "galacticos",
    "paywall",
    "wags",
    "twenty20",
    "chip-and-pin",
    "click-and-collect",
    "declutter",
    "chuggers",
    "goji berries",
    "fatbergs",
    "sars",
    "norovirus",
    "e-cigarrets",
    "bromances",
    "mansplaining",
    "butters",
    "nang",
    "totes",
    "noughties",
    "grexit",
    "brexit"
]
# Enforce UTF-8 Encoding on the request
if r.encoding is None:
    r.encoding = 'utf-8'
## streams and prints the content
[ print(line) for line in r.iter_lines(decode_unicode=True) if line.lower() in wordlist ]
    
      
