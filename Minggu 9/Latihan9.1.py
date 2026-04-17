import re

def jancok(a,b):
    if sorted(re.sub(r"\W+", "", a.lower())) == sorted(re.sub(r"\W+", "", b.lower())):
        print(f"{a}, {b} ini Anagram")
    else:
        print("Bukan anagram")

jancok("mata", "atma")
jancok("mata", "tama")
jancok("mata" , "maat")
jancok("mata" , "taam")