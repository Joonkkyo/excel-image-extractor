# excel-image-extractor
문서 타입별 이미지 추출 및 비문 여부 추론 프로그램

## Overview
1. ppt, ddf, word, excel 에 존재하는 모든 이미지 추출
2. 추출된 이미지에 대해 pretrained model 기반 inference 실행 (비문 여부)
3. 문서의 비문 여부를 기록한 csv 파일 생성

## 폴더 구조
```
application
├── data_preprocessing/                     - 데이터 전처리 함수 정의
│     ├── docxreader.py                     - word 파일 이미지 추출
│     ├── extract_pdf_image.py              - pdf 파일 이미지 추출
│     ├── extract_ppt_imgae.py              - ppt 파일 이미지 추출
│     ├── extract_excel_imgae.py            - 엑셀 파일 이미지 추출
│     └── extract_docx_image.py             - 모델 정의
├── README.md                               - 리드미 파일
├── main.py                                 - 메인 프로그램
└── requirements.txt                        - 필수 모듈 정의
```
## Usage
```
python main.py --model [h5 file] --dir [file path] --label [string]
```

![image](https://user-images.githubusercontent.com/12121282/131793241-38b0416b-fb56-4865-bb0f-d396f6e4ff57.png)
