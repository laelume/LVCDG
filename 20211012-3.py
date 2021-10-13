Clock.bpm = 70
#Scale.default = "harmonicMinor"
Scale.default = "indian"
#lullaby for jigglypuff

ri >> ripple([(1,3,6),(2,4,6),(1,4,7),(0,4,8)],dur=4,amplify=0.6)
gl >> glass([(1,3,6),(2,4,6),(1,4,7),(0,4,8)],dur=16,sus=20)

p3 >> charm([14,15,16,10,15,13], dur=[2,1,1,4,1,1], room=5, swell=3, vib=1, amplify=0.7)

p2 >> nylon([7, 0, _, 4, _], dur=1, pan=P[-1, 1], blur=1, bend=var([0.5,1],5), amplify=0.25)
p1 >> pluck([1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,6.5,6,5.5,5,4.5,4,3.5,3,2.5,2,1.5,1],dur=1/16,room=5,pan=[-0.5,0.5],amplify=0.2,amp=var([1,0],[80,200])).every(5,'stutter')
b2 >> varsaw([0,-1,-2,-3, _], oct=3, dur=4, amplify=1)
a0 >> ambi([0,-3,-6],dur=[5,6,4],amplify=0.5,pan=PSine(15))
a1 >> play('v---X--[------]', amplify=0.7).every(8,'reverse')
s2 >> play(' o   oooo',sample=var([1,4],4),amplify=0.3,cut=1)