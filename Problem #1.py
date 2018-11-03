>>> z=0
>>> for x in range(1000):
	if x%5==0 or x%3==0:
		z=z+x
>>> z
233168
#correct.
#hangups included 1) trying an if elif thread ('or' is much more suitable, 
	#if/elif stops the loop after an if has been proved true for the first time.
		#2) using a for loop (inherently iterative) is much cleaner than a while loop. though i could/will try now.
>>> z=0
>>> x=0
>>> i = int(input("enter the range you want"))
enter the range you want1000

>>> type(i)
<class 'int'> #showing it is an integer, not a str.

>>> while x<1000:
	x=x+1
	if x%5==0 or x%3==0:
		z=z+x-i
>>> z
-232832
##obviously wrong, because the 1000 is subtracted on each iteration.
##thinking i must need a user-defined function which give me the oppurtunity to subtract the int(input('range:') only once)
#ugly.
