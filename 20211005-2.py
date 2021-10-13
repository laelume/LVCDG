Scale.default= "minor"

p1 >> prophet([14,15,14,15,16,15,16,17,16,17,18,19,20], pan=[-1,1], dur=1/3)
p2 >> prophet([16,17,16,17,18,17,14,19,18,19,20,21,22], pan=[1,-1], dur=1/3)

hh >> play("x ---[---] %[xxx] $ ", sample=3, amp=var([1, 0], [7, 1, 14, 2]))


sn >> play("  o ![**] z ", sample=var([0, 3], 16), amplify=0.6 * var([1, 0], [28, 4, 31, 1, 56, 8]))

pi >> play("z        ", sample=3, pan=1)


b1 >> jbass([0,0,0,0,6,6,6,6,2,2,2,2,2,2,2,2], sus=1/4, dur=1/3, mod=7, room=4, amplify=0.7)

gl >> glass([0,7,14,-7,-14], pan=[1,-1], sus=12, dur=10).shuffle()

dr >> varsaw(0, oct=2, dur=20, amplify=0.4)


xx >> play('V x[--] o \ ',amplify=0.6)
xy >> blip(var([-1,-2,-5],8),dur=3,chop=var([4,5,3,7,9,13,12],8)).every(4,'stutter')

xz >> space(dur=1,chop=50)


# or z 

# idk, my Supercollider is broken :<

# oh god, my supercolllider is doing WRRRRRRRRRRROOOOOOOOOOM
# JackDriver: exception in real time: alloc failed, increase server's memory allocation (e.g. via ServerOptions)

# wobbly is probably ss player

# random background noises, SPOOKY
ss >> play('s', dur=PWhite(2, 20) * linvar([1, 0.5], 32), rate=PWhite(-1, 0), pan=PWhite(-0.75, 0.75), sample=PRand(40), room=PWhite(0.5, 2), mix=PWhite(0.1, 0.5), amp=0.85 * expvar([0, 1, 1], 128))

# clapssss, fading out
cp >> play('H', sample=3, dur=0.25, echo=P[[0.125, 0], 0, 0, 0], amp=PRand([0.15, 0.25, 0.4, 0.55, 0.75, 0.8, 1, 1, 1]) * expvar([1, 0], [[3, 7, 16, 4, 8, 12, 9], 0]) * 0.75 * var([1, 0], [32, 64, 64, 32, 32, 32, 128, 64, 64, 24]) * expvar([0, 1], 256))

#        |\      _,,,---,,_
#  ZZZzz /,`.-'`'    -.  ;-;;,_
#       |,4-  ) )-,_. ,\ (  `'-'
#      '---''(_/--'  `-'\_)