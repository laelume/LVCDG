Clock.bpm = 65
Scale.default = "locrian"
Master.amplify = 0.1

print(Attributes)
print(SynthDefs)

b1 >> jbass([0, _, -4, -5, 4, 3, 2], dur=[4,1.5,3,3,0.5,0.5,0.5], drive=0.3, amplify=0.4)

b1 >> jbass([0, 2, 0, -3, -4, -5], dur=[4, 0.5, 2.5, 0.5, 2.5, 2.5], drive=0.4, amplify=0.3)

p1 >> ambi([0,7,14,12,7,4,2,0], slide=0.3, slidedelay=0.3, blur=3, spin=1, room=5, amplify=0.4).stop()

p2 >> space([7,6,5,4,3,2,1,0,6,5,4,3,2,1,0,5,4,3,2,1,0,4,3,2,1,0,3,2,1,0,11,9,11,13,12,13], striate=0, swell=4,dur=1/9,vib=5, vibdepth=0.05, pan=PSine(43.7), amplify=0.6).every(1,'mirror')

p3 >> blip([0,7,4,0,4,7,4,7], dur=1/3, echo=1.5, bits=2, shape=0.5, decay=6, pan=[0.8,-0.8], room=5, amplify=0.1)

p4 >> pluck(a,swell=2,dur=1/16,vib=10,vibdepth=0.1,pan=PSine(200),amplify=0.32).every(1,'mirror').stop()

p5 >> creep([0,3,-2],dur=[5,3,1,9,7,13],chop=1,amplify=0.7,echo=3,lpf=10000)

p6 >> prophet([14,16,14,_] + [16,18,16,_], dur=[2,0.5,2,8])

a=[0,-1,-2,2,3,7,6,5,4,5,4,3,-1]
ka >> karp(a,slide=0.5,dur=1/2,echo=0.7,room=6,amplify=0.4,spin=2)

bd >> play("x   x[xxx]  x  x[xxx]", amplify=0.7)
sn >> play("   o    o   ", sample=var([3,5],5), room=15, amplify=0.5)

h2 >> play('[[---] [--  ---]  ]',amplify=0.5)
ph >> play('[++] +  ',amplify=0.8)
ps >> play('   /               ',room=4,amplify=0.5)
pc >> play(':           ',amplify=0.9)
h3 >> play('[===] [===] = =  =   =    =     ',sample=2,amplify=0.3,room=20)

c=[-7,4,0,-14,-7,4,0]
vs >> varsaw(c,dur=4,sus=10,pan=[-0.5,0.5],amplify=0.5,swell=3)

b=[7,8,7,9,8,9,11,9,11,13,12,13,15,13,15,17,16,17,20,19,18]
bl >> blip(b,dur=12/7,pan=PSine(20),room=20,amplify=0.3).every(4,'stutter')

pa >> pasha([7,6,5,4,3,2,1,0,6,5,4,3,2,1,0,5,4,3,2,1,0,4,3,2,1,0,3,2,1,0,11,9,11,13,12,13],dur=4,room=50,lpf=1000,amplify=0.6).every(17,'stutter')