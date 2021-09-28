# excel-image-extractor
문서 타입별 이미지 추출 및 비문 여부 추론 프로그램

## Overview
1. ppt, pdf, word, excel 에 존재하는 모든 이미지 추출
2. 추출된 이미지에 대해 pretrained model 기반 inference 실행 (비문 여부)
3. 문서의 비문 여부를 기록한 csv 파일 생성

## 폴더 구조
```
application
├── A_OriginalDataset/                      - 예제 input data
│     ├── Secrets/                          - 예제 input data (비밀 문서)
│     └── TFs/                              - 예제 input data (TF 문서)
├── B_Data_Preprocessing/                   - 데이터 전처리 함수 정의
│     ├── docxreader.py                     - word 파일 파싱 (https://github.com/badbye/docxpy/blob/master/docxpy/docxreader.py 참조)
│     ├── extract_word_image.py             - word 파일 이미지 추출
│     ├── extract_ppt_image.py              - ppt 파일 이미지 추출
│     ├── extract_excel_image.py            - 엑셀 파일 이미지 추출
│     └── extract_pdf_image.py              - pdf 파일 이미지 추출
├── C_PreprocessedDataSet/                  - input data로부터 추출된 이미지 저장
├── D_Training/                             - 추출된 이미지 기반 학습 코드
│     └── train.py                          
├── E_Model/                                - 학습 후 생성된 모델 저장
├── F_Inferencing_SampleData/               - inference를 진행할 예제 데이터
├── G_Inferencing/                          - 문서에 대한 inference 실행 코드
├── H_Result/                               - inference 결과를 저장할 csv 파일 문서
├── I_IncTrainSampleDataSet/                - incremental training 진행에 사용할 이미지 데이터셋
├── J_Incremental_Training/                 - inceremental training 실행 코드
│     └── incremental_train.py              - pdf 파일 이미지 추출
├── K_Tensorboard_Log/                      - 학습 과정을 기록한 tensorboard log 저장 
├── L_Utils/                                - 기타 유틸리티 프로그램
│     ├── compare_two_dir.py                - 두 디렉토리 비교 후 중복 파일 제거
│     └── temp_delete_file.py               - 디렉토리에 존재하는 모든 파일 제거
├── README.md                               - 리드미 파일
├── main.py                                 - 메인 프로그램 (문서 이미지 추출 + inference)
└── requirements.txt                        - 필수 모듈 정의
```
## 환경 설정
* 가상환경 설정 및 필수 모듈 설치
```bash
$ virtualenv venv -p python3
$ source venv/bin/activate
$ pip install -r requirements.txt
```
* 운영체제에 맞는 libreoffice 7.2 설치

  https://ko.libreoffice.org/download/libreoffice-fresh/

## Usage

### main.py - Preprocess & Inference
```bash
python main.py --model [h5 file] --input-dir [intput dir path] --output-dir [output dir path] --label [string]
```
* [h5 file] : pretrained model의 weight 파일, 추출만 진행할 시 입력하지 않음
* [input dir path] : 추출할 파일이 존재하는 디렉토리 (마지막 문자 / 생략) ex) /home/data/input_img
* [output dir path] : 추출한 이미지가 저장될 디렉토리 (마지막 문자 / 생략) ex) /home/data/output_img
* [string] : 이미지 추출 과정에서  이름 앞에 붙는 문자열

### D_Training/train.py - Model Training
파일에서 추출한 이미지 데이터를 바탕으로 CNN 모델 기반 학습 진행
```bash
python ./D_Training/train.py --dir [intput dir path]
```
* [dir path] : 학습시킬 이미지 파일이 존재하는 디렉토리 (마지막 문자 / 생략) ex) /home/data/input_img

### J_Incremental_Training/train.py - Incremental Training
추가적으로 추출한 이미지 파일을 기존 모델에 추가적으로 학습 진행 
```bash
python ./J_Incremental_Training/train.py --dir [dir path] --img [img path]
```
* [dir path] : 학습시킬 이미지 파일이 존재하는 디렉토리 (마지막 문자 / 생략) ex) /home/data/input_img
* [img path] : inference를 진행할 이미지 파일 경로
## Result
csv 파일에 다음과 같은 형식으로 추론 결과 저장
|Documents|Results|Prob (TF)|Prob (Secret)|
|---|---|---|---|
|aa.pptx|TF|73.8%|26.2%|
|bb.pdf|Secret|46.4%|53.6%|
|cc.docx|판단 불가 (이미지 없음)| | |
|dd.xlsx|TF| 99.61% | 0.39% |
