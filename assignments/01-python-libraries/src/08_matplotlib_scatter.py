from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
import pandas as pd

# 설치된 한글 폰트를 선택한다. 한글 폰트가 없으면 영문 라벨을 사용한다.
available_fonts = {font.name for font in font_manager.fontManager.ttflist}
korean_font = next(
    (name for name in ("AppleGothic", "Malgun Gothic", "NanumGothic", "Noto Sans CJK KR")
     if name in available_fonts),
    None,
)
if korean_font:
    plt.rcParams["font.family"] = korean_font
plt.rcParams["axes.unicode_minus"] = False

# 데이터 불러오기
assignment_dir = Path(__file__).resolve().parents[1]
data = pd.read_csv(assignment_dir / "data" / "piaac_employed_24.csv")

x = data["Numeracy_Score"]
y = data["Wage_Metric"]

# 국가명 한글 변환
country_ko = {
    "Austria": "오스트리아",
    "Canada": "캐나다",
    "Chile": "칠레",
    "Czechia": "체코",
    "Denmark": "덴마크",
    "Estonia": "에스토니아",
    "Finland": "핀란드",
    "France": "프랑스",
    "Germany": "독일",
    "Hungary": "헝가리",
    "Ireland": "아일랜드",
    "Italy": "이탈리아",
    "Japan": "일본",
    "Korea": "한국",
    "Latvia": "라트비아",
    "Lithuania": "리투아니아",
    "Netherlands": "네덜란드",
    "Norway": "노르웨이",
    "Portugal": "포르투갈",
    "Slovak Republic": "슬로바키아",
    "Spain": "스페인",
    "Sweden": "스웨덴",
    "Switzerland": "스위스",
    "United States": "미국",
}

# 겹침 완화를 위한 국가별 라벨 위치 조정값
# (x방향, y방향) in points
offsets = {
    "Chile": (8, 8),
    "Portugal": (8, 8),
    "Hungary": (8, 12),
    "Lithuania": (-10, 8),
    "Latvia": (10, -8),
    "Slovak Republic": (10, -15),
    "Spain": (8, -10),
    "Italy": (-15, 12),
    "France": (8, 10),
    "Korea": (8, 10),
    "Czechia": (8, -10),
    "Estonia": (8, 10),
    "Japan": (8, -4),
    "United States": (8, -10),
    "Ireland": (8, 10),
    "Austria": (8, 10),
    "Germany": (8, 10),
    "Canada": (8, 10),
    "Sweden": (8, 10),
    "Finland": (8, -12),
    "Netherlands": (8, 12),
    "Norway": (8, 10),
    "Denmark": (8, 10),
    "Switzerland": (8, 10),
}

# 그래프 생성
fig, ax = plt.subplots(figsize=(13, 8))

# 산점도 점 표시
ax.scatter(x, y, s=70, color="royalblue", edgecolor="black", linewidth=0.6, alpha=0.9)

# 국가명 라벨 표시
for _, row in data.iterrows():
    country = str(row["Country"])
    korean_name = country_ko.get(country, country) if korean_font else country

    dx, dy = offsets.get(country, (6, 6))

    ax.annotate(
        korean_name,
        (row["Numeracy_Score"], row["Wage_Metric"]),
        xytext=(dx, dy),
        textcoords="offset points",
        fontsize=9,
        ha="left",
        va="bottom",
    )

# 선형 추세선 계산
slope, intercept = np.polyfit(x, y, 1)
x_line = np.linspace(x.min(), x.max(), 100)
y_line = slope * x_line + intercept

# 추세선 표시
ax.plot(
    x_line, y_line, color="black", linestyle="--", linewidth=1.6, label="선형 추세선"
)

# Pearson 상관계수
r = np.corrcoef(x, y)[0, 1]
ax.text(
    0.03,
    0.95,
    f"Pearson r = {r:.2f}",
    transform=ax.transAxes,
    fontsize=13,
    verticalalignment="top",
)

# 제목 및 축 이름
ax.set_title("성인 수리력과 시간당 소득 중앙값의 관계", fontsize=20)

ax.set_xlabel("평균 수리력 점수", fontsize=13, labelpad=10)

ax.set_ylabel("시간당 소득 중앙값 (2022년 USD, PPP 보정)", fontsize=13, labelpad=20)

if not korean_font:
    ax.set_title("Adult numeracy and median hourly earnings", fontsize=20)
    ax.set_xlabel("Mean numeracy score", fontsize=13, labelpad=10)
    ax.set_ylabel("Median hourly earnings (2022 USD, PPP adjusted)", fontsize=13, labelpad=20)
    ax.lines[0].set_label("Linear trend")

# 격자
ax.grid(linestyle="--", alpha=0.25)

# 추세선 범례
ax.legend(loc="lower right", fontsize=10, frameon=False)

# 여백
fig.subplots_adjust(left=0.12, right=0.97, top=0.90, bottom=0.12)

output_dir = assignment_dir / "figures"
output_dir.mkdir(exist_ok=True)
fig.savefig(output_dir / "piaac_numeracy_earnings.png", dpi=180, bbox_inches="tight")
print(f"Countries: {len(data)}, Pearson r: {r:.4f}")
if plt.get_backend().lower() != "agg":
    plt.show()
