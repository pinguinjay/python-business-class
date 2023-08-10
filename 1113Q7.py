#輸入
path = input()
require_type, code = input().split(":") 
#function
def read_table(path):
    MAPPING_TABLE_ERROR = 0
    CNS2CHAR = dict()
    CHAR2CNS = dict() 
    with open(path,"r") as fh :#格式 cns \t uni
        for line in fh :
            parts = line.strip().split('\t')
            parts_chr = chr(int("0x" + parts[1],16))
            parts_cns = parts[0]
            #建立 CNS2CHAR 字典 
            #CNS 交換碼只能對應到1個 Unicode 字元，否則輸出 'MAPPING_TABLE_ERROR'
            if parts_cns not in CNS2CHAR : #若無cns key則加入 {[key]:value}
                CNS2CHAR[parts_cns] = parts_chr
            elif CNS2CHAR[parts_cns] !=  parts_chr : #若該cns已存在 卻無法對應到特定unicode的字元
                MAPPING_TABLE_ERROR +=1
            #建立CHAR2CNS = dict()
            #可以一個char對應多個cns，只需依序列出
            if parts_chr not in CHAR2CNS : #如果[chr] 不存在
                CHAR2CNS[parts_chr] = [parts_cns]
            else : #如果[chr] 存在
                CHAR2CNS[parts_chr].append(parts_cns) #加入cns在[chr]
                CHAR2CNS[parts_chr] = sorted(CHAR2CNS[parts_chr]) #由小到大排序
            if MAPPING_TABLE_ERROR>0 :#若有錯誤則跳出迴圈
                break
    return MAPPING_TABLE_ERROR, CNS2CHAR, CHAR2CNS
#演算
MAPPING_TABLE_ERROR, CNS2CHAR, CHAR2CNS = read_table(path)
if MAPPING_TABLE_ERROR == 0 : #如果表正確
    print(len(CNS2CHAR))
    if require_type == "CNS" : #如果要用cns查詢
        try : 
            print(CNS2CHAR[code])
        except :
            print("NO_DATA_FOUND")
    if require_type == "CHAR" : #如果要用chr查詢
        try :
            if len(CHAR2CNS[code]) ==1 : #如果該key對應到一個value
                for item in CHAR2CNS[code]:
                    print(item)                
            elif  len(CHAR2CNS[code]) ==len(set(CHAR2CNS[code])): #如果該key對應到多個value，且不重複
                for i in CHAR2CNS[code]:
                    print(i)
            else : #如果該key對應到多個value，且重複
                for i in sorted(set(CHAR2CNS[code])):
                    print(i)

        except :
            print("NO_DATA_FOUND")
else:#如果表不正確
    print("MAPPING_TABLE_ERROR")
