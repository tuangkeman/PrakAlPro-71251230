import re

def jamcikk(a):
    return re.sub(r"\s+", " ", a).strip()

kalimat ="saya            tidak          suka        memancing          ikan"

print(jamcikk(kalimat))