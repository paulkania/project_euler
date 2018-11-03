>>> z=0
>>> for x in range(1000):
	if x%5==0 or x%3==0:
		z=z+x
>>> z
233168 #correct.
#hangups included 1) trying an if elif thread ('or' is much more suitable, 
	#if/elif stops the loop after an if has been proved true for the first time.
		#2) using a for loop (inherently iterative) is much cleaner than a while loop. though i could/will try now.
>>> z=0
>>> x=0
>>> i = int(input("enter the range you want"))
enter the range you want1000

>>> type(i)
<class 'int'> #showing it is an integer, not a str.

>>> while x<i:
	x=x+1
	if x%5==0 or x%3==0:
		z=z+x-i
>>> z
-232832
##obviously wrong, because the 1000 is subtracted on each iteration.
##thinking i must need a user-defined function which give me the oppurtunity to subtract the int(input('range:') only once)
#ugly.
#edit1 idea didn't work (add 'ans' variable which is ans=z-i because i created the 'ans' variable before the loop, so z 
#was defined as 0, not 234168. and adding a ans

#edit2 I got it, but it's not super pretty, pretty patchy in fact. the following.
#i avoided iteration by 'back-indenting' so that ans=z-i occurs not in the loop, only once the loop has finished, which is naive.
VVV
>>> x=0
>>> z=0
>>> ans=0
>>> i = int(input("enter the range you want:  "))
enter the range you want:  1000
while x<i:
	x=x+1
	if x%5==0 or x%3==0:
		z=z+x
	ans=z-i
>>> ans
233168
>>> z
234168
>>> i
1000
VVV
