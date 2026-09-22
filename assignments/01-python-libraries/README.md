# 01 Python 데이터 분석 라이브러리

NumPy와 Pandas의 기본 자료구조를 실습하고, Matplotlib으로 누적 막대그래프와 산점도를 작성한 과제입니다.

## 실습 구성

| 코드 | 학습 내용 | 결과 |
| --- | --- | --- |
| [01_numpy_array.py](src/01_numpy_array.py) | 1차원·2차원 배열 생성과 자료형 | 터미널 배열 출력 |
| [02_numpy_reshape.py](src/02_numpy_reshape.py) | `arange()`와 `reshape()` | 수열과 3행 2열 배열 |
| [03_numpy_slicing.py](src/03_numpy_slicing.py) | 행·열 슬라이싱 | 일부 열과 첫 번째 행 |
| [04_pandas_series.py](src/04_pandas_series.py) | 숫자·문자열 Series | 인덱스, 값, 자료형 |
| [05_pandas_index.py](src/05_pandas_index.py) | 사용자 지정 인덱스와 값 조회 | 과목별 점수 |
| [06_pandas_dataframe.py](src/06_pandas_dataframe.py) | DataFrame 생성, 열 선택, `head()` | 컴퓨터 부품 예시 표 |
| [07_quiz_stacked_bar.py](src/07_quiz_stacked_bar.py) | 세 데이터의 누적 높이 계산 | TIOBE 순위 그래프 |
| [08_matplotlib_scatter.py](src/08_matplotlib_scatter.py) | CSV 읽기, 산점도, 라벨, 추세선, 상관계수 | OECD 국가별 비교 |

실습 6의 제품 정보는 DataFrame 구조를 연습하기 위한 예시이며 제품의 성능 동등성을 뜻하지 않습니다.

## Quiz 풀이

3위 데이터를 먼저 그리고, 2위는 3위 값 위에서 시작하도록 설정했습니다. 1위의 시작 높이는 3위와 2위의 원소별 합입니다.

```python
bottom1 = [a + b for a, b in zip(y3, y2)]
```

2025년 예시: `10.15 + 10.29 = 20.44`에서 1위 막대가 시작하고, 전체 높이는 `20.44 + 23.28 = 43.72`입니다.

## 추가 시각화

- 입력: [piaac_employed_24.csv](data/piaac_employed_24.csv), 국가별 집계값 24건.
- x축: 취업자의 평균 수리력 점수.
- y축: 시간당 세전 소득 중앙값, PPP 보정 2022년 USD.
- 방법: `ax.scatter()`, `ax.annotate()`, `np.polyfit()`, `np.corrcoef()`.
- 결과: Pearson `r ≈ 0.6411`. 국가 간 양의 상관관계이며 인과관계나 개인 수준의 관계로 일반화하지 않습니다.
- [데이터의 출처와 정의](data/README.md).

## 결과 파일

- [TIOBE 누적 막대그래프](figures/tiobe_stacked_bar.png)
- [수리력과 소득 산점도](figures/piaac_numeracy_earnings.png)
- `screenshots/01.png`부터 `06.png`: NumPy·Pandas 결과 화면.
- `screenshots/07.png`: 산점도 결과 화면.
- `screenshots/08.png`: Quiz 결과 화면.
- `reports/`: 제출용 Word와 PDF 보고서.

보고서는 제출 당시 코드와 실행 결과를 보존합니다. 저장소의 코드는 폴더 정리 과정에서 CSV 경로, 폰트 선택, 그래프 자동 저장, 변수명 오타를 정리했습니다. 실습 데이터와 계산 내용은 같습니다.

## 실행

저장소 루트에서 의존성을 설치한 뒤 실행합니다.

```bash
python -m pip install -r requirements.txt
python assignments/01-python-libraries/src/08_matplotlib_scatter.py
```

개별 파일을 각각 실행할 수 있습니다. 01~06은 터미널에 출력하고, 07~08은 `figures/`에 그래프를 저장합니다.
