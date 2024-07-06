# -*- coding: utf-8 -*-
"""9. 머신러닝.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fSJqAPdPQt6p1H-wAzYHZbWjMuxBBT8S

# **1. 머신러닝(Machine Learning)**
* 인공지능: 인공(Artificial) + 지능(Interlligence)
  * 1956년: 인간의 지능을 복제하거나 능가할 수 있는 지능형 기계를 만들고자 하는 컴퓨터 과학 분야
* 개발자에 의한 인공지능, 데이터에 의한 인공지능
* 머신러닝: 데이터를 기반으로 한 학습(learning)하는 기계(machine)
  * 1997년: 기계가 기존 데이터에서 학습하고 해당 데이터를 개선하여 의사 결정 또는 예측을 할 수 있도록 하는 AI의 하위 집합
* 딥러닝: 깊은(deep) 신경망 구조의 머신러닝
  * 2017년: 신경망 레이어를 사용하여 데이터를 처리하고 결정을 내리는 기계 학습 기술
* Generative AI
  * 2021년: 프롬프트나 기존 데이터를 기반으로 새로운 문서, 시각, 청각 컨텐츠를 생성하는 기술
* Chat GPT
  * 2022: GPT(Generative Pre-trained Transformer) 시리즈를 기반으로 하는 OpenAI가 개발한 대화형 AI 모델
  <center><img src='http://live.lge.co.kr/wp-content/uploads/2020/06/AI%EC%9A%A9%EC%96%B4%EC%82%AC%EC%A0%84_03.jpg' width='600'></center>

# **2. 머신러닝 정의**
* 배경: 데이터를 대량으로 수집 처리할 수 있는 환경이 갖춰짐으로 머신러닝으로 할 수 있는 일들이 많아짐
* 머신러닝은 데이터로부터 특징이 패턴을 찾아내는 것이기 때문에 데이터가 가장 중요함
* 인공지능의 한 분야로 컴퓨터가 학습할 수 있도록 알고리즘과 기술을 개발하는 분야
* "무엇(x)으로 무엇(y)을 예측하고 싶다"의 f(함수)를 찾아내는 것
* x: 입력변수(독립변수), y:출력변수(종속변수), f모형(머신러닝 알고리즘)

# **3. 머신러닝으로 할 수 있는 것**

### 3-1. 회귀(Regression)
* 시계열(시간적인 변화를 연속적으로 관측한 데이터)데이터 같은 연속된 데이터를 취급할 때 사용하는 기법
* 예측
* 예) 과거 주식 추세를 학습해서 내일의 주가를 예측하는 시스템을 개발

### 3-2. 분류(Classification)
* 주어진 데이터를 클래스별로 구별해 내는 과정으로 데이터와 데이터의 레이블값을 학습시키고 어느 범주에 속한 데이터인지 판단
* 예) 스팸메일인지 아닌지 구별해주는 시스템을 개발

### 3-3. 클러스터링(Clustering)
* 분류와 비슷하지만 데이터에 레이블이 없음
* 유사한 속성들을 갖는 데이터를 일정한 수의 군집으로 그룹핑하는 비지도 학습
* 예) SNS 데이터를 통해 소셜 및 사회 이슈를 파악

# **4. 학습**

### 4-1. 지도 학습(Supervised Learning)
* 문제의 정답을 모두 학습시켜 예측 또는 분류하는 문제
* y=f(x)에 대하여 입력 변수(x)와 출력 변수(y)의 관계에 대하여 모델링하는 것
* y에 대하여 예측 또는 분류하는 문제

### 4-2. 비지도 학습(Unsupervised Learning)
* 출력 변수(y)가 존재하지 않고, 입력변수(x)간의 관계에 대해 모델링 하는 것
* 군집분석: 유사한 데이터끼리 그룹화

### 4-3. 자기지도 학습(Self-Supervised Learning)
* 데이터 자체에서 스스로 레이블을 생성하여 학습에 이용하는 방법
* 다양한 Label이 없는 raw Data로부터 데이터 부분들의 관계를 통해 Label을 자동으로 생성하여 지도 학습에 이용하는 비지도 학습 기법
* GPT, BERT 모델

### 4-4. 강화 학습(Reinforcement Learning)
* 결정을 순차적으로 내려야 하는 문제에 적용
* 레이블이 있는 데이터를 통해서 가중치와 편향을 학습하는 것과 비슷하게 보상이라는 개념을 사용하여 가중치와 편향을 학습하는 것
"""