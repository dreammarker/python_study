#  -*- coding: utf-8 -*-
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30];
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번 쨰 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정 류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서뒤집기
num_list.reverse()
print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호",2,True]
num_list.extend(mix_list)
print(num_list)
