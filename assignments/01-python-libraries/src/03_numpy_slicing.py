import numpy as np

ar1 = np.arange(10, 70, 10)
ar1 = ar1.reshape(2, 3)
print(ar1[0:2, 0:2])  # 모든 행에서 앞 2열만 추출
print()
print(ar1[0, :])  # 첫 번째 행 추출
