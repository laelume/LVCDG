Clock.bpm = 65
Scale.default = "locrian"
Master.amplify = 0.1

b1 >> jbass([0, _, -4, -5], dur=4, amplify=0.6)

b1 >> jbass([0, 2, 0, -3, -4, -5], dur=[4, 0.5, 2.5, 0.5, 2.5, 2.5])

p1 >> ambi([0,7,14,12,7,4,2,0], slide=0.3, slidedelay=0.3, blur=3, spin=1, room=5, amplify=0.4).stop()

p2 >> space([7,6,5,4,3,2,1,0,6,5,4,3,2,1,0,5,4,3,2,1,0,4,3,2,1,0,3,2,1,0,11,9,11,13,12,13], swell=4,dur=1/19,vib=5, vibdepth=0.05, pan=PSine(43.7), amplify=0.6).every(1,'mirror')

p3 >> blip([0,7,4,0,4,7,4,7], dur=2, echo=4/5, shape=0.5, decay=4, pan=0.8, room=5, amplify=0.05)

p4 >> pluck(a,swell=2,dur=1/16,vib=10,vibdepth=0.1,pan=PSine(200),amplify=0.32).every(1,'mirror').stop()


a=[0,-1,-2,2,3,7,6,5,4,5,4,3,-1]
ka >> karp(a,slide=0.5,dur=1/2,echo=0.7,room=6,amplify=0.4)

bd >> play("x     x   x ", amplify=0.7)
sn >> play("        o   ", room=4, amplify=0.5)
h2 >> play('[[---] [--  ---]  ]',amplify=0.5)
ph >> play('[++] +  ',amplify=0.8)
ps >> play('   /               ',room=4,amplify=0.5)
pc >> play(':           ',amplify=0.9)

c=[-7,-14,-7]
vs >> varsaw(c,dur=16,sus=20,pan=[-0.5,0.5],amplify=0.3)
b=[7,8,7,9,8,9,11,9,11,13,12,13,15,13,15,17,16,17,20,19,18]
bl >> blip(b,dur=12,pan=PSine(20),room=20,amplify=0.3).every(4,'stutter')