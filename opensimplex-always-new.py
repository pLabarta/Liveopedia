from opensimplex import OpenSimplex
perlin = OpenSimplex(seed=random.randint(1,5000))
perlineada = []
for numero in range(1,99):
    perlineada.append(math.ceil(perlin.noise2d(x=numero, y=2)*10))
p1 >> blip(P[perlineada], dur=abs(P[perlineada]/4),pan=[-1,1], lpf=linvar([700,4000]))
p7 >> blip(p1.pitch+1, delay=0.5, oct=5, dur=p1.dur, pan=[-1,1]).every(2,'offadd',1)
p6 >> bass((p1.pitch), delay=0, dur=1/2, oct=4,amp=0.7)
p3 >> play('{x-u  }', dur=abs(P[perlineada]/4))
p4 >> play('(* )', dur=abs(P[perlineada]/4), delay=abs(P[perlineada]/4))
p5 >> play('X ') 
