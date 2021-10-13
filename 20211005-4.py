Scale.default= "wholeTone"
Clock.bpm= 50

var.pat=P[14,15,14,15,16,15,16,17,16,17,18,19,20,19,18,17,16,15]
p1 >> creep(var.pat, pan=PSine(8.88), dur=1/3,lpf=3500).every(18,'mirror')
p2 >> viola(var.pat+2, pan=PSine(-8.88), delay=0.04,dur=1/3,lpf=1400)


p3 >> gong([0,4,-7,4,0], pan=PSine(5), dur=1/2,)

hh >> play("x % $ [\\\\]", sample=3, amp=var([1, 0], [7, 1, 14, 2]))

sn >> play("x   x", sample=var([1, 5], 16), amplify=0.7 * var([1, 0], [28, 4, 31, 1, 56, 8]))

pi >> play("2        ", sus=5, pan=1, sample=var([2, 4], 16))

pq >> blip([3,2,3,4,5,4,5,6,5,6,7,8,7,6,5,2,-1],room=20,amplify=1,pan=PSine(15)).every(7,'stutter')

b1 >> jbass([0,3,0,3,6,5,6,5,4.5,4,3.5,3,2.5,2,1.5,1,0.5], sus=1/4, dur=1/3, mod=7, room=4, amplify=0.3)

gl >> glass([0,7,14,-7,-14], pan=[1,-1], sus=12, dur=10, amplify=0.5)

dr >> varsaw([0], oct=3, dur=5, amplify=0.9)

xx >> play('V x[--] o \ ',amplify=0.6 * var([1, 0], [31, 1, 28, 4, 64, 0]))
xy >> blip([-7,-5,-4,-3,-2,4,3,2,1,6,5,4,5,4,3,2,3],dur=1/4, sus=5, amplify=1, room=8, mod=8, oct=var([5, 4], 16), pan=[-1,1]).every(17,'mirror')
xz >> space([0,4,7,11,14,11,7,4,0], amplify=0.2, dur=4, oct=2, chop=[2, 4, 8], pan=PWhite(-0.5, 0.5), amp=expvar([1, 0], [[16, 32, 64], 0]))
zz >> play('--[------]--[---]----------=',amplify=2)
