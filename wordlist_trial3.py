import requests
r = requests.get('', stream=True)
## source : https://public.oed.com/blog/words-from-the-21st-century/
wordlist=[
    "clockwork-orange", 
    "follically-challenged",
    "adulting",
    "ALS" ,
    "amyotrophic lateral sclerosis", 
    "anti-vaccine", 
    "ASD", 
    "authenticate", 
    "autism spectrum disorder",
    "blue Monday",
    "body dysmorphic disorder ",
    "bot" ,
    "burpee", 
    "cancel culture", 
    "circuit noun",
    "circuit breaker", 
    "climate action", 
    "climate change denial", 
    "clinical trial", 
    "condole", 
    "CrossFit",
    "defund", 
    "eco-anxiety", 
    "epinephrine", 
    "EpiPen",
    "femicide", 
    "foam roller", 
    "gender binary", 
    "hot mess", 
    "informed-consent",  
    "kettlebell", 
    "kill-it", 
    "kinesiology", 
    'live-tweet",
    "lock-down",
    "rosacea", 
    "Sas",
    "self-care", 
    "socially-distanced", 
    "soft-play",
    "support-bubble", 
    "Tabata",
    "toxicity", 
    "toxic masculinity", 
    "underappreciated ",
    "unmute" ,
    "young adult", 
    "zero-emission" 


]
# Enforce UTF-8 Encoding on the request
if r.encoding is None:
    r.encoding = 'utf-8'
## streams and prints the content
[ print(line) for line in r.iter_lines(decode_unicode=True) if line.lower() in wordlist ]
    
      
