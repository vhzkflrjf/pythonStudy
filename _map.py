animals = ['사자', '코끼리', '기린', '원숭이', '바나나원숭이']

print(",".join(animals))
# >> 사자,코끼리,기린,원숭이,바나나원숭이

print("\n".join(animals))
# >> 사자
# >> 코끼리
# >> 기린
# >> 원숭이
# >> 바나나원숭이

print("/".join(animals))
# >> 사자/코끼리/기린/원숭이/바나나원숭이

a = list(map(str, range(10)))

print(a)