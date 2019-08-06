b1 >> sawbass(var([0,1,-2],[8,8,16]), dur=PDur(5,16), cutoff=P[1000,5000][:5], sus=1/2)

### sometimes snick and kick, sometimes hithat stuff
b2 >> play("x-", sample=2).sometimes("stutter", 4, dur=3)
b3 >> play("  I ", sample=2, hpf=(0,2000), lpf=(300,0), hpr=0.5)

