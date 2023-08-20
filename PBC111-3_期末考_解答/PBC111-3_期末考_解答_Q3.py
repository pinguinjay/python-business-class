# 讀入英文單詞及英文段落
word1, word2 = input().split()
paragraph = input()

# 給定標點符號
sentence_sep = '.!?'
delimeters = ',;'

# 計算句子數量
sentence_cnt = 0
for sep in sentence_sep:
    sentence_cnt += paragraph.count(sep)

# 移除非句子分隔符號的標點符號
for deli in delimeters:
    while deli in paragraph:
        paragraph = paragraph.replace(deli, ' ')

# 先把句子切開
sentences = paragraph.split('.')
for sep in '!?':
    for part in sentences:
        if sep in part:
            sentences.remove(part)
            for item in part.split(sep):
                sentences.append(item)

# 計算兩個英文單詞同時出現的句子數
target_cnt = 0
for sentence in sentences:
    sentence = ' ' + sentence + ' '
    if ' ' + word1 + ' ' in sentence and ' ' + word2 + ' ' in sentence:
        target_cnt += 1

# 印出結果
print(sentence_cnt, target_cnt)