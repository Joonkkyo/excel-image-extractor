# excel-image-extractor
---

## Overview
1. Seegene의 densenet 기반 inference 모델을 IPU에서 실행 가능하도록 변환

    - poptorch 모듈 사용을 위한 환경 설정
    - DataLoader 변경
    - poptorch.inferenceModel 함수를 통한 모델 변환
    - 기타 불필요한 코드 정리
2. Compile / Inference 파일을 별도로 분리
>
## Usage
```
python main.py --model [h5 file] --dir [file path] --label [string]
```
## 폴더 구조
