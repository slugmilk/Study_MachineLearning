# -*- coding: utf-8 -*-
"""16. 랜덤 포레스트.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19uIMTFEs6xZS3Fi13fjI8bvW-_pycShb

# **1. hotel 데이터셋**
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

hotel_df = pd.read_csv('/content/drive/MyDrive/컴퓨터비전_시즌2/3. 데이터 분석/Data/hotel.csv')

hotel_df.info()

"""* hotel: 호텔 종류
* is_canceled: 취소 여부
* lead_time: 예약 시점으로부터 체크인 될 때까지의 기간(얼마나 미리 예약했는지)
* arrival_date_year: 예약 연도
* arrival_date_month: 예약 월
* arrival_date_week_number: 예약 주
* arrival_date_day_of_month: 예약 일
* stays_in_weekend_nights: 주말을 끼고 얼마나 묶었는지
* stays_in_week_nights: 평일을 끼고 얼마나 묶었는지
* adults: 성인 인원수
* children: 어린이 인원수
* babies: 아기 인원수
* meal: 식사 형태
* country: 지역
* distribution_channel: 어떤 방식으로 예약했는지
* is_repeated_guest: 예약한적이 있는 고객인지
* previous_cancellations: 몇번 예약을 취소했었는지
* previous_bookings_not_canceled: 예약을 취소하지 않고 정상 숙박한 횟수
* reserved_room_type: 희망한 룸타입
* assigned_room_type: 실제 배정된 룸타입
* booking_changes: 예약 후 서비스가 몇번 변경되었는지
* deposit_type: 요금 납부 방식
* days_in_waiting_list: 예약을 위해 기다린 날짜
* customer_type: 고객 타입
* adr: 특정일에 높아지거나 낮아지는 가격
* required_car_parking_spaces: 주차공간을 요구했는지
* total_of_special_requests: 특별한 별도의 요청사항이 있는지
* reservation_status_date: 예약한 날짜
* name: 이름
* email: 이메일
* phone-number: 전화번호
* credit_card: 카드번호
"""

hotel_df.drop(['name', 'email', 'phone-number', 'credit_card', 'reservation_status_date'], axis=1, inplace=True)
hotel_df.head()

hotel_df.describe()

sns.displot(hotel_df['lead_time'])

sns.boxplot(hotel_df['lead_time'])

sns.barplot(x=hotel_df['distribution_channel'], y=hotel_df['is_canceled'])

hotel_df['distribution_channel'].value_counts()

sns.barplot(x=hotel_df['hotel'], y=hotel_df['is_canceled'])

sns.barplot(x=hotel_df['arrival_date_year'], y=hotel_df['is_canceled'])

plt.figure(figsize=(15, 5))
sns.barplot(x=hotel_df['arrival_date_month'], y=hotel_df['is_canceled'])

import calendar

print(calendar.month_name[1])
print(calendar.month_name[2])
print(calendar.month_name[3])

months = []
for i in range(1, 13):
    months.append(calendar.month_name[i])

months

plt.figure(figsize=(15, 5))
sns.barplot(x=hotel_df['arrival_date_month'], y=hotel_df['is_canceled'], order=months)

sns.barplot(x=hotel_df['is_repeated_guest'], y=hotel_df['is_canceled'])

sns.barplot(x=hotel_df['deposit_type'], y=hotel_df['is_canceled'])

hotel_df['deposit_type'].value_counts()

# corr(): 열들 간의 상관관계를 계산하는 함수 (피어슨 상관계수)
# -1 ~ 1까지의 범위를 가지며 0에 가까울수록 두 변수의 상관관계가 없거나 매우 약함
hotel_df.corr(numeric_only=True)

plt.figure(figsize=(15, 15))
sns.heatmap(hotel_df.corr(numeric_only=True), cmap='coolwarm', vmax=1, vmin=-1, annot=True)

hotel_df.isna().mean()

hotel_df = hotel_df.dropna()

hotel_df.head()

hotel_df[hotel_df['adults'] == 0]

# people 파생변수
hotel_df['people'] = hotel_df['adults'] + hotel_df['children'] + hotel_df['babies']
hotel_df.head()

hotel_df[hotel_df['people'] == 0]

hotel_df = hotel_df[hotel_df['people'] != 0]
hotel_df

hotel_df['total_nights'] = hotel_df['stays_in_week_nights'] + hotel_df['stays_in_weekend_nights']
hotel_df.head()

# season 파생변수
# arrival_date_month에 따라 아래와 같이 값을 저장
# 12, 1, 2: winter
# 3, 4, 5: spring
# 6, 7, 8: summer
# 9, 10, 11: fall
season_dic = {'spring':[3, 4, 5], 'summer': [6, 7, 8], 'fall': [9, 10, 11], 'winter': [12, 1, 2]}

new_season_dic = {}

for i in season_dic:
    for j in season_dic[i]:
        new_season_dic[calendar.month_name[j]] = i

new_season_dic

hotel_df['season'] = hotel_df['arrival_date_month'].map(new_season_dic)
hotel_df.head()

hotel_df.info()

hotel_df['expected_room_type'] = (hotel_df['reserved_room_type'] == hotel_df['assigned_room_type']).astype(int)
hotel_df.head()

hotel_df['cancel_rate'] = hotel_df['previous_cancellations'] / (hotel_df['previous_cancellations'] + hotel_df['previous_bookings_not_canceled'])
hotel_df.head()

hotel_df[hotel_df['cancel_rate'].isna()]

hotel_df['cancel_rate'] = hotel_df['cancel_rate'].fillna(-1)

hotel_df.head()

hotel_df.info()

hotel_df['hotel'].dtype

hotel_df['is_canceled'].dtype

hotel_df['children'].dtype

obj_list = []

for i in hotel_df.columns:
    if hotel_df[i].dtype == 'O':
        obj_list.append(i)

obj_list

for i in obj_list:
    print(i, hotel_df[i].nunique())

hotel_df.drop(['country', 'arrival_date_month'], axis=1, inplace=True)

obj_list.remove('country')
obj_list.remove('arrival_date_month')

hotel_df = pd.get_dummies(hotel_df, columns=obj_list)
hotel_df.head()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(hotel_df.drop('is_canceled', axis=1), hotel_df['is_canceled'], test_size=0.3, random_state=2024)

X_train.shape, y_train.shape

X_test.shape, y_test.shape

"""# **2. 앙상블(ensemble) 모델**
* 여러개의 머신러닝 모델을 이용해 최적의 답을 찾아내는 기법을 사용하는 모델
* 보팅(Voting)
    * 서로 다른 알고리즘 model을 조합해서 사용
    * 모델에 대해 투표로 결과를 도출
* 배깅(Bagging)
    * 같은 알고리즘 내에서 다른 sample 조합을 사용
    * 샘플 중복 생성을 통해 결과를 도출
* 부스팅(Boosting)
    * 약한 학습기들을 순차적으로 학습시켜 강력한 학습기를 만듦
    * 이전 오차를 보완해가면서 가중치를 부여
    * 성능이 우수하지만 잘못된 레이블이나 아웃라이어에 대해 필요이상으로 민감
    * AdaBoost, Gradient Boosting, XGBoost, LightGBM
* 스태킹(Stacking)
    * 다양한 개별 모델들을 조합하여 새로운 모델을 생성
    * 다양한 모델들을 학습시켜 예측 결과를 얻은 다음, 다양한 모델들의 예측 결과를 입력으로 새로운 메타 모델을 학습

# **3. 랜덤 포레스트(Random Forest)**
* 머신러닝에서 많이 사용되는 앙상블 기법 중 하나이며, 결정 나무를 기반으로 함
* 학습을 통해 구성해 놓은 결정 나무로부터 분류 결과를 취합해서 결론을 얻는 방식
* 랜덤 포레스트의 트리는 원본 데이터에서 무작위로 선택된 샘플을 기반으로 학습함
* 각 트리가 서로 다른 데이터셋으로 학습되어 다양한 트리가 생성되며 모델의 다양성이 증가함
* 각각의 트리가 예측한 결과를 기반으로 다수결 또는 평균을 이용하여 최종 예측을 수행함
* 분류와 회귀 문제에 모두 사용할 수 있으며, 특히 데이터가 많고 복잡한 경우에 매우 효과적인 모델
* 성능은 꽤 우수한 편이나 오버피팅 하는 경향이 있음
"""

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(random_state=2024)

rf.fit(X_train, y_train)

pred1 = rf.predict(X_test)
pred1

proba1 = rf.predict_proba(X_test)
proba1

# 첫번째 테스트 데이터에 대한 예측 결과
proba1[0]

# 모든 테스트 데이터에 대한 호텔 예약을 취소할 확률만 출력
proba1[:, 1]

"""# **4. 머신러닝/딥러닝에서 모델의 성능을 평가하는 데 사용되는 측정값**
* Accuracy: 올바른 에측의 비율 (정밍도)
* Precision: 모델에서 수행한 총 긍정 예측 수에 대한 참 긍정 예측의 비율
* Recall: 실제 긍정 사례의 총 수에 대한 참 긍정 예측의 비율 (재현율)
* F1 Score: 정밀도와 재현율의 조화평균이며, 정밀도와 재현율 간의 균형을 맞추기 위한 단일 메트릭으로 사용
* AUC-ROC Curve: 참양성률(TPR)과 가양성률(FPR) 간의 균형을 측정
  * 예: TPR: 실제로 질병이 있을 때, 검사 결과가 양성인 경우
  * 예: FPR: 실제로 질병이 없을 때, 검사 결과가 음성인 경우
  * ROC: 이진 분류의 성능을 보여주는 그래프. 민감도(TPR)와 특이도(FPR) 사이의 관계
  * AUC: ROC 커브와 직선 사이의 면적을 의미. 범위는 0.5~1이며, 값이 클수록 예측의 정확도 높음

  <center><img src='https://miro.medium.com/v2/resize:fit:722/1*pk05QGzoWhCgRiiFbz-oKQ.png'></center>
  
  *AOC 오타임*

  <center><img src='https://www.datasciencecentral.com/wp-content/uploads/2021/10/1341805045.jpg'></center>
  
  *오른쪽으로 갈수록 잘 분류된 모델*

  * AUC = 1
    * 두 개의 곡선이 전혀 겹치지 않는 경우 모델은 가장 이상적인 분류 성능을 보임
    * 양성 클래스와 음성 클래스를 완벽하게 구별할 수 있음
  * AUC = 0.75
    * 설정한 theshold에 따라 오류값들을 최소화 또는 최대화 할 수 있음
    * 해당 분류 모델이 양성 클래스와 음성 클래스를 구별할 수 있는 확률이 75%임을 의미
  * AUC = 0.5
    * 분류 모델의 성능이 최악인 상황
    * 해당 분류 모델은 양성 클래스와 음성 클래스를 구분할 수 있는 능력이 없음


"""

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score

accuracy_score(y_test, pred1)

confusion_matrix(y_test, pred1)

print(classification_report(y_test, pred1))

roc_auc_score(y_test, proba1[:, 1])

# 하이퍼 파라미터 수정 (max_depth=30을 적용)
rf2 = RandomForestClassifier(max_depth=30, random_state=2024)
rf2.fit(X_train, y_train)
proba2 = rf2.predict_proba(X_test)
roc_auc_score(y_test, proba2[:, 1])

# 하이퍼 파라미터 수정 후 (성능 증가)
0.9319781899069026 - 0.9315576511541386

# 하이퍼 파라미터 수정(max_depth=30, min_samples_split=5, n_estimators=120을 적용)
rf3 = RandomForestClassifier(max_depth=30, random_state=2024,
                             min_samples_split=5, n_estimators=120)
rf3.fit(X_train, y_train)
proba3 = rf3.predict_proba(X_test)
roc_auc_score(y_test, proba3[:, 1])

# 하이퍼 파라미터 추가 수정 후 (성능 감소)
0.931059217235636 - 0.9319781899069026

"""# **5. 하이퍼 파라미터 최적의 값 찾기**
* GridSearchCV: 원하는 모든 하이퍼 파라미터를 적용하여 최적의 값을 찾음
* RandomizedSearchCV: 원하는 하이퍼 파라미터를 지정하고 n_iter값을 설정하여 해당 수 만큼 random하게 조합하여 최적의 값을 찾음
"""

from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

params = {
    'max_depth': [30, 40],
    'min_samples_split': [2, 3],
    'n_estimators': [100, 120]
}

rf4 = RandomForestClassifier(random_state = 2024)
# grid_df = GridSearchCV(rf4, params, cv=5) cv: 교차검증 횟수
grid_df = GridSearchCV(rf4, params)
grid_df.fit(X_train, y_train)

grid_df.cv_results_
# 'rank_test_score': array([4, 1, 5, 6, 7, 8, 2, 3], dtype=int32)}: 두번쨰 파라미터 조합이 가장 성능 좋음

grid_df.best_params_ # 가장 좋은 파라미터 조합

rf5 = RandomForestClassifier(random_state=2024)
rand_df = RandomizedSearchCV(rf5, params, n_iter=3, random_state=2024) # n_iter=3 : 8개의 파라미터 조합 중 랜덤하게 3개 뽑음
rand_df.fit(X_train, y_train)

rand_df.cv_results_
# 랜덤으로 선택된 파라미터: [{'n_estimators': 120, 'min_samples_split': 2, 'max_depth': 30}, {'n_estimators': 100, 'min_samples_split': 3, 'max_depth': 40}, {'n_estimators': 100, 'min_samples_split': 2, 'max_depth': 40}]

rand_df.best_params_

proba5 = rand_df.predict_proba(X_test)

import matplotlib.pyplot as plt
from sklearn.metrics._plot.roc_curve import roc_curve

fpr, tpr, thr = roc_curve(y_test, proba5[:, 1])
print(fpr, tpr, thr)

plt.plot(fpr, tpr, label='ROC Curve')
plt.plot([0, 1], [0, 1])
plt.show()

"""# **6. 피처 중요도(Feature Importances)**
* 결정 나무에서 노드를 분기할 때 해당 피처가 클래스를 나누는데 얼마나 영향을 미쳤는지 표기하는 척도
* 0에 가까우면 클래스를 구분하는데 해당 피처의 영향이 거의 없다는 것이며, 1에 가까우면 해당 피처가 클래스를 나누는데 영향을 많이 줬다는 의미
"""

# {'n_estimators': 120, 'min_samples_split': 2, 'max_depth': 30}
rf6 = RandomForestClassifier(random_state=2024, max_depth=30, min_samples_split=2, n_estimators=120)
rf6.fit(X_train, y_train)
proba6 = rf6.predict_proba(X_test)
roc_auc_score(y_test, proba6[:, 1])

proba6

rf6.feature_importances_

1.25445350e-01

feature_imp = pd.DataFrame({
    'features': X_train.columns,
    'importances': rf6.feature_importances_
})

feature_imp

top10 = feature_imp.sort_values('importances', ascending=False).head(10)
top10

plt.figure(figsize=(5, 10))
sns.barplot(x='importances', y='features', data=top10, palette='Set2')

