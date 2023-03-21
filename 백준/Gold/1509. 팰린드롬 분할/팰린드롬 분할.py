characters = list(input())

# memo[i] : i번째 문자로 시작하는 palindrome 길이들
memo = [[] for i in range(len(characters))]

def FindPalindrome(i, l=characters, memo=memo):
  # i 번째 문자가 중심인 palindrome 찾기
  s = i
  e = i
  p_len = 1
  while s > -1 and e < len(l):
    if l[s] == l[e]:
      memo[s].append(p_len)
      s -= 1
      e += 1
      p_len += 2 
    else:
      break
  # i 번째 문자와 i+1번째 문자 사이가 중심인 palindrome 찾기
  s = i
  e = i+1
  p_len = 2
  while s > -1 and e < len(l):
    if l[s] == l[e]:
      memo[s].append(p_len)
      s -= 1
      e += 1
      p_len += 2
    else:
      break

for i in range(len(characters)):
  FindPalindrome(i)

min_n = [i for i in range(len(characters)+1)]
for i, l in enumerate(memo):
  for p_len in l:
    min_n[i+p_len] = min(min_n[i+p_len], min_n[i]+1)
print(min_n[-1])