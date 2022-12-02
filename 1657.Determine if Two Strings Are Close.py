def closerString(word1:str,word2:str)->bool:
    count1 = Counter(word1)
    count2 = Counter(word2)
    
    keys1 = sorted(count1.keys())
    keys2 = sprted(count2.keys())
    
    values1 = sorted(count1.values())
    values2 = sorted(count2.values())
    return keys1 == keys2 and values1==values2