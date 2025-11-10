# Seg-NN CPU 환경 구축 프로젝트

[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![PyTorch](https://img.shields.io/badge/PyTorch-CPU-orange.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 프로젝트 개요

CVPR 2024 Highlight 논문인 **Seg-NN**([논문 링크](https://arxiv.org/pdf/2404.04050.pdf))의 코드를 Windows CPU 환경에서 구동하기 위한 환경 구축 및 검증 프로젝트입니다.

### 원본 저장소
- **GitHub**: [yangyangyang127/Seg-NN](https://github.com/yangyangyang127/Seg-NN)
- **논문**: "No Time to Train: Empowering Non-Parametric Networks for Few-shot 3D Scene Segmentation"
- **학회**: CVPR 2024 Highlight

---

## 프로젝트 목표

1. Windows CPU 환경에서 Seg-NN 실행 환경 구축
2. PointNet2 컴파일 문제 해결 (더미 모듈 구현)
3. 코드 구조 분석 및 파이프라인 검증
4. 향후 GPU 환경 전환 준비

---

## 구현 내용

### 완료된 작업
- [x] Python 3.8 기반 Conda 가상환경 구성
- [x] PyTorch CPU 버전 설치 및 검증
- [x] PointNet2 대체 모듈 구현 (더미 구현)
- [x] 기본 테스트 스크립트 작성
- [x] 코드 구조 분석 도구 작성

### 주요 해결 과제
**문제**: Windows 환경에서 PointNet2 C++ 확장 모듈 컴파일 실패
- CUDA 미지원 환경에서 빌드 불가
- Visual Studio Build Tools 의존성 문제

**해결**: 더미(Dummy) PointNet2 모듈 구현
- 실제 알고리즘 대신 간단한 대체 함수 제공
- 코드 구조 검증 및 Import 테스트 가능
- 향후 GPU 환경에서 실제 모듈로 교체 예정

---

## 실행 환경

### 필수 요구사항
- **OS**: Windows 10/11 (64-bit)
- **Python**: 3.8
- **메모리**: 최소 8GB RAM
- **GPU**: 불필요 (CPU 전용)

### 권장 사양
- **메모리**: 16GB RAM
- **저장공간**: 10GB 이상

---

## 설치 및 실행 가이드

### 1. 저장소 클론

```bash
git clone https://github.com/your-username/segnn-cpu-implementation.git
cd segnn-cpu-implementation
```

### 2. Conda 환경 생성

```bash
# Anaconda Prompt를 관리자 권한으로 실행

# 환경 생성
conda create -n SegNN python=3.8 -y

# 환경 활성화
conda activate SegNN
```

### 3. 패키지 설치

```bash
# PyTorch CPU 버전
conda install pytorch torchvision cpuonly -c pytorch -y

# 필수 패키지
pip install -r requirements.txt
```

### 4. 더미 PointNet2 모듈 설치

```bash
# 프로젝트 루트 디렉토리에서
cd pointnet2_dummy
pip install -e .
cd ..
```

### 5. 설치 검증

```bash
# 환경 테스트
python scripts/test_environment.py

# Import 테스트
python scripts/test_imports.py

# 샘플 데이터 생성 및 테스트
python scripts/create_sample_data.py
```

---

## 실행 결과

### 환경 테스트 결과
```
==================================================
CPU Environment Test for Seg-NN
==================================================

1. PyTorch Version: 1.12.0+cpu
   CUDA Available: False
   CPU threads: 8

2. Testing basic operations...
   ✓ Matrix multiplication: torch.Size([10, 5])

3. Testing PointNet2 import...
   ⚠ Using dummy PointNet2 operations (CPU only)
   ✓ Import successful

4. Memory test...
   Point cloud shape: torch.Size([2, 512, 3])
   Memory usage: 12.00 KB

==================================================
Test completed successfully!
==================================================
```

---

## 프로젝트 구조

```
segnn-cpu-implementation/
├── README.md                          # 프로젝트 개요
├── requirements.txt                   # Python 패키지 목록
│
├── environment_setup/                 # 환경 설정 가이드
│   ├── install_windows.bat           # Windows 자동 설치 스크립트
│   ├── setup_guide.md                # 상세 설치 가이드
│   └── troubleshooting.md            # 문제 해결 가이드
│
├── pointnet2_dummy/                   # 더미 PointNet2 모듈
│   ├── __init__.py
│   ├── pointnet2_ops.py              # 대체 구현
│   └── setup.py                      # 설치 스크립트
│
├── scripts/                           # 테스트 및 분석 스크립트
│   ├── test_environment.py           # 환경 검증
│   ├── test_imports.py               # Import 테스트
│   ├── create_sample_data.py         # 샘플 데이터 생성
│   └── analyze_segnn.py              # 코드 구조 분석
│
├── docs/                              # 문서
│   ├── implementation_log.md         # 구현 과정 기록
│   └── code_analysis.md              # 코드 분석 보고서
│
└── screenshots/                       # 실행 결과 스크린샷
    └── README.md
```

---

## 상세 문서

- [설치 가이드](environment_setup/setup_guide.md) - 단계별 설치 방법
- [문제 해결](environment_setup/troubleshooting.md) - 자주 발생하는 오류 해결
- [구현 일지](docs/implementation_log.md) - 구현 과정 상세 기록
- [코드 분석](docs/code_analysis.md) - Seg-NN 코드 구조 분석

---

## 제한사항

### 현재 단계의 한계
1. **실제 성능 측정 불가**: 더미 모듈 사용으로 실제 알고리즘 미구현
2. **데이터셋 미포함**: S3DIS 데이터셋 크기(10-20GB) 및 라이센스 문제
3. **GPU 실험 불가**: CPU 전용 환경

### 이는 의도된 설계입니다
본 프로젝트는 **"환경 구축 및 코드 검증"**에 초점을 맞추었습니다.

---

## 기여

본 프로젝트는 학술 연구 목적으로 작성되었습니다. 개선 사항이나 제안이 있으시면 Issue를 열어주세요.

---

## 라이센스

본 프로젝트는 MIT 라이센스를 따릅니다. 원본 Seg-NN 프로젝트의 라이센스도 참고해주세요.

---

## 참고 자료

### 논문
- [Seg-NN Paper (CVPR 2024)](https://arxiv.org/pdf/2404.04050.pdf)
- [Point-NN Paper](https://arxiv.org/abs/2209.15276)

### 관련 저장소
- [Seg-NN Official](https://github.com/yangyangyang127/Seg-NN)
- [Point-NN](https://github.com/ZrrSkywalker/Point-NN)
- [attMPTI](https://github.com/Na-Z/attMPTI)

### 데이터셋
- [S3DIS Dataset](http://buildingparser.stanford.edu/dataset.html)
- [ScanNet Dataset](http://www.scan-net.org/)

---

## 작성자

**[권규원]**
- 학교: [성균관대학교]
- 과제: 타겟논문 오픈소스 코드 분석 프로젝트
- 연락처: [anthony05@g.skku.edu]

---

## 감사의 말

이 프로젝트는 다음의 오픈소스를 기반으로 합니다:
- Seg-NN 저자들의 훌륭한 연구
- PyTorch 커뮤니티
- Point cloud processing 연구 커뮤니티

---

## 인용

본 프로젝트를 사용하시는 경우 원본 논문을 인용해주세요:

```bibtex
@inproceedings{zhu2024segnn,
  title={No Time to Train: Empowering Non-Parametric Networks for Few-shot 3D Scene Segmentation},
  author={Zhu, Xiangyang and others},
  booktitle={CVPR},
  year={2024}
}
```

---
