word_count = {}
with open("poem.txt","r",encoding='utf-16') as f:
    for line in f:
        tokens=line.strip().split(' ') 
        count=0
        for token in tokens:
            if token in word_count:
                word_count[token]+=1
            else:
                word_count[token]=1

print(word_count)
