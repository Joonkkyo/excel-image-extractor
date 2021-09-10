# excel-image-extractor
문서 타입별 이미지 추출 및 비문 여부 추론 프로그램

## Overview
1. ppt, pdf, word, excel 에 존재하는 모든 이미지 추출
2. 추출된 이미지에 대해 pretrained model 기반 inference 실행 (비문 여부)
3. 문서의 비문 여부를 기록한 csv 파일 생성

## 폴더 구조
```
application
├── data_preprocessing/                     - 데이터 전처리 함수 정의
│     ├── docxreader.py                     - word 파일 파싱 (https://github.com/badbye/docxpy/blob/master/docxpy/docxreader.py 참조)
│     ├── extract_word_image.py             - word 파일 이미지 추출
│     ├── extract_ppt_imgae.py              - ppt 파일 이미지 추출
│     ├── extract_excel_imgae.py            - 엑셀 파일 이미지 추출
│     └── extract_pdf_image.py              - pdf 파일 이미지 추출
├── README.md                               - 리드미 파일
├── main.py                                 - 메인 프로그램
└── requirements.txt                        - 필수 모듈 정의
```
## Usage
```
python main.py --model [h5 file] --input-dir [intput dir path] --output-dir [output dir path] --label [string]
```
* [h5 file] : pretrained model의 weight 파일, 추출만 진행할 시 입력하지 않음
* [input dir path] : 추출할 파일이 존재하는 디렉토리
* [output dir path] : 추출한 이미지가 저장될 디렉토리
* [string] : 이미지 추출 과정에서  이름 앞에 붙는 문자열
