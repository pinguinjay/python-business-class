word1 = input()
word2 = input()
dist = int(input())
paragraph = input()
def check_legal(word1,word2,dist, paragraph) : #檢查是否合法
    legal = True
    if len(word1) <1 or len(word2)<1 :
        legal = False
    if dist >1000 or dist <0 :
        legal = False
    if  len(paragraph) >10000 :
        legal = False     
    return legal

def find_word(word,paragraph) : #找字的位置
    positions = []
    start = 0
    while start < len(paragraph):
        position = paragraph.find(word, start)
        if position == -1: #找不到
            break
        else :
            positions.append(position) #找到就記錄起來
            start = position + len(word) 
    return positions

def find_strings (word1,word2,dist, paragraph) :
    word1_posit = find_word(word1,paragraph)
    word2_posit = find_word(word2,paragraph)
    result = [] #存放結果句子
    for word1_index in word1_posit :
        for word2_index in word2_posit :
            if  abs(word2_index - (word1_index + len(word1))) <dist or abs(word1_index - (word2_index + len(word2)))<dist: #長度在d以內
                if word2_index >word1_index :
                    first = word1_index
                    second = word2_index
                    string = [first , second+len(word2)]
                    result.append(string)
                if word1_index >word2_index :
                    first = word2_index
                    second = word1_index
                    string = [first , second+len(word1)]
                    result.append(string)
        if len(result) ==0 :
            pass
    return sorted(result, key=lambda sublist: sublist[0])               
               
def find_2words(word1, word2, dist, paragraph) :
    legal = check_legal(word1,word2,dist, paragraph) 
    if legal == False :
        print("ILLEGAL_INPUT")

    else :
        result = find_strings (word1,word2,dist, paragraph)
        if  len(result) ==0 :
            print("^^NOT_FOUND^^")
        else:
            for result_pair in result :
                #print(result_pair)
                print ( paragraph[result_pair[0] : result_pair[1]], end = "\n")
 
find_2words(word1, word2, dist, paragraph) 
