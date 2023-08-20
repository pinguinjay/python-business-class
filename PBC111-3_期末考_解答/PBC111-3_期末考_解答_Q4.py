m, n, k = list(map(int, input().split(';')))

scores = []
for i in range(m):
    score = list(map(int, input().split(',')))
    scores.append(score)

# calculate the rating of each seller; ratings[i] is the rating of seller i
ratings = {}
for i in range(m):
    ratings[i] = sum(scores[i]) - k * (n - scores[i].count(0))

# sort the sellers in:
#   (1) descending order of their rating
#   (2) ascending order of their id
sorted_id = sorted(range(m), key = lambda x: (-ratings[x], x))

print(sorted_id[0] + 1, sorted_id[1] + 1, sorted_id[2] + 1, sep = ' ')
