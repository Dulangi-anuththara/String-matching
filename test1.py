f1=open("text.txt")
f2=open("pattern.txt")


text=f1.readline()
pattern=f2.readline()

n=len(text)
m=len(pattern)

array=[]

for i in range(n):
	
	t=i
	for j in range(m):
		
		#Check for wild card
		if(pattern[j]!="_"):
			#Break out of inner loop if mismatch
			if(pattern[j]!=text[t]):
			
				break
			
							
		array.append(text[t])
		t=t+1
		if(j==m-1):
				
				for x in array:
					print(x,end='')

				print()	
	array.clear()

	
		

