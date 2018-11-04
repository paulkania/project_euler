>>> def compute(): ###user defined function
	ans=0 		###define initial variables (dont be afraid to have an x AND a y
	x=1	
	y=2
	while x<=4000000:
		if x%2==0:
			ans+=x		###using += is sexier than ans=ans+x (both work, confirmed)
		x,y=y,x+y###for simultaneous updating (rather than dominoe updating). or you can add a dummy variable to avoid a dominoe (q=x+y;x=y;y=q)
	return(str(ans))		###not just just return(ans)??A:__both work,confirmed.

>>> if __name__ == "__main__":		###why.
	print(compute())
4613732 #right!

#so here i had to cop out again. the main loss i had was not understanding the x,y relationship.
#i was trying to do it with only two variables (x,zum) rather than 3 [x,y,ans] as seen below.
x=2
zum=0
while x<50:
	x=(x-1)+(x-2)
	if x >= 200:
		break
	elif x%2 ==0:
		zum=zum+x
	elif x%2 !=0:
		continue
