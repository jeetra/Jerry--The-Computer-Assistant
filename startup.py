import random
from playsound import playsound
sounds=['welcome+f1.mp3','welcome+hp.mp3','welcome+hp1.mp3','welcome+irm.mp3','welcome+irm1.mp3','welcome+poc.mp3',
        'welcome+t&m.mp3','welcome1+mi.mp3']
p=random.choice(sounds)

playsound(p)
