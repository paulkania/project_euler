Python 3.6.3 (v3.6.3:2c5fed86e0, Oct  3 2017, 00:32:08) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
def compute():
	ans=0
	x=1
	y=2
	while x<=4000000:
		if x%2==0:
			ans+=x
		x=y
		y=x+y
	return(str(ans))

>>> ans
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    ans
NameError: name 'ans' is not defined
>>> if __name__ == "__main__":
	print(compute())

	
4194302
>>> def compute():
	ans=0
	x=1
	y=2
	while x<=4000000:
		if x%2==0:
			ans+=x
		x,y=y,x+y
	return(str(ans))

>>> if __name__ == "__main__":
	print(compute())

	
4613732
>>> 
