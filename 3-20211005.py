Scale.default= "chinese"
Clock.bpm= 20

var.pat=[14,15,14,15,16,15,16,17,16,17,18,19,20]
p1 >> prophet(var.pat, pan=PSine(13.3), dur=1/3)
p2 >> prophet(var.pat, pan=PSine(-8.8), dur=1/3)

# This is very Eno. Suck it Eno

hh >> play("x % $ ", sample=3, amp=var([1, 0], [7, 1, 14, 2]))

sn >> play("x   ", sample=var([1, 5], 16), amplify=0.6 * var([1, 0], [28, 4, 31, 1, 56, 8]))

pi >> play("2        ", sus=5, pan=1, sample=var([2, 4], 16))

pq >> keys([3,2,3,4,5,4,5,6,5,6,7,8,7,6,5,2,-1], room=20, amplify=1.5).every(7,'stutter')

b1 >> jbass([0,0,0,0,6,6,6,6,2,2,2,2,2,2,2,2], sus=1/4, dur=1/3, mod=7, room=4, amplify=0.3)

gl >> glass([0,7,14,-7,-14], pan=[1,-1], sus=12, dur=10, amplify=0.5)

dr >> varsaw(0, oct=2, dur=20, amplify=0.5)


xx >> play('V x[--] o \ ',amplify=0.6 * var([1, 0], [31, 1, 28, 4, 64, 0]))
xy >> blip([-7,-5,-4,-3,-2,4,3,2,1,6,5,4,5,4,3,2,3],dur=1/4, sus=5, amplify=1, room=8, mod=8, oct=var([5, 4], 16), pan=[-1,1]).every(17,'mirror')

xz >> space([0,4,7,11,14,11,7,4,0], amplify=0.2, dur=4, oct=2, chop=[2, 4, 8], pan=PWhite(-0.5, 0.5), amp=expvar([1, 0], [[16, 32, 64], 0]))

# random background noises, SPOOKY
ss >> play('s', dur=PWhite(2, 20) * linvar([1, 0.5], 32), rate=PWhite(-1, 0), pan=PWhite(-0.75, 0.75), sample=PRand(40), room=PWhite(0.5, 2), mix=PWhite(0.1, 0.5), amp=0.85 * expvar([0, 1, 1], 128))

# k, see y'all <3

# clapssss, fading out
cp >> play('H', sample=3, dur=0.25, echo=P[[0.125, 0], 0, 0, 0], amp=PRand([0.15, 0.25, 0.4, 0.55, 0.75, 0.8, 1, 1, 1]) * expvar([1, 0], [[3, 7, 16, 4, 8, 12, 9], 0]) * 0.75 * var([1, 0], [32, 64, 64, 32, 32, 32, 128, 64, 64, 24]) * expvar([0, 1], 256))

#        |\      _,,,---,,_
#  ZZZzz /,`.-'`'    -.  ;-;;,_
#       |,4-  ) )-,_. ,\ (  `'-'
#      '---''(_/--'  `-'\_)