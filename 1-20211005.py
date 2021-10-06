




hh >> play("x ---[---] % ", sample=3, amp=var([1, 0], [7, 1, 14, 2]))


sn >> play("  o ![**] ", sample=var([0, 3], , amplify=0.6 * var([1, 0], [28, 4, 31, 1, 56, 8]))


b1 >> bass([0,0,0,0,6,6,6,6,2,2,2,2,2,2,2,2], sus=1/4, dur=1/3, mod=7, room=4, amplify=0.7).shuffle()

gl >> glass([0,7,14,-7,-14], pan=[1,-1], sus=12, dur=10).shuffle()


xx >> play('V x[--] o \ ',amplify=0.6)
xy >> blip(var([-1,-2,-5],8),dur=3,chop=var([4,5,3,7,9,13,12],8)).every(4,'stutter')



# random background noises, SPOOKY
ss >> play('s', dur=PWhite(2, 20) * linvar([1, 0.5], 32), rate=PWhite(-1, 0), pan=PWhite(-0.75, 0.75), sample=PRand(40), room=PWhite(0.5, 2), mix=PWhite(0.1, 0.5), amp=0.85)
