f1=open("DNA.txt")
f2=open("Query.txt")


db_base=[]                                      #List stores the objects of database
query_base=[]                                   #List stores the objects of query
                                                           
content_db=f1.read()                            #read the content of entire DNA file
content_query=f2.read()


db_split=content_db.split('>')                  #split the database by '>'
query_split=content_query.split('>')            #split the query by '>'

#print(query_split)

for x in query_split:                          
    newlist=[]                                  #List to store description and the string
    query=""                                    #to make the string
    if (x!="") and (x!="EOF"):
        temp=x.split('\n')
        m=len(temp)
        newlist.append(temp[0])                 #store description of Query 
        for i in range(1,m):
            query=query+temp[i]                 #concatenate all the lines to one sequence

        newlist.append(query)    
        query_base.append(newlist)


for y in db_split:    
    newlist=[]
    query=""
    if (y!="") and (y!="EOF"):
        temp=y.split('\n')
        m=len(temp)
        newlist.append(temp[0])             #store description of DNA sequence 
        for i in range(1,m):
            query=query+temp[i]             #concatenate all the lines to one sequence

        newlist.append(query)    
        db_base.append(newlist)

#print(db_base)
#print(query_base)


def KMP(pat,txt):
    #preprocessing algorithm
    m=len(pat)
    n=len(txt)
    pi=[0]*m
    k=0

    for q in range(1,m):
            while k>0 and pat[k]!=pat[q]:    #if mismatch is found
                    k=pi[k-1]
            if pat[k]==pat[q]:
                    k=k+1

            pi[q]=k                         #stores the pi value of each symbol

    #print(pi)

    #Searching algorithm
    j=0
    for i in range(n):
            if(j==0) and i==(n-1):          #if no match is found
                    return 0

            while j>0 and txt[i]!=pat[j]:
                    j=pi[j-1]
            
            if txt[i]==pat[j]:
                    j=j+1

            if(j==m):                       #if match is found
                    #print(i-m+1)   
                    return (i-m+1)
            


for select_pat in query_base:
    count=0
    pat=select_pat[1]                                               #select the query string
    print(select_pat[0])
    for select_text in db_base:
        txt=select_text[1]                                          #select DNA sequence
        val=KMP(pat,txt)
        if val>0:                                                   #check if there is a match
            count=count+1                                           #Count the number of matches of query 
            print("[",select_text[0],"] at offset ",val)

    if count==0:
        print("NOT FOUND")                                          #if there is no at least one match with the DNA sequences in the database





