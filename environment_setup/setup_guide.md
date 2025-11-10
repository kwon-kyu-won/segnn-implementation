# Seg-NN CPU 환경 설치 가이드

이 문서는 Windows 환경에서 Seg-NN을 실행하기 위한 단계별 설치 가이드입니다.

## 목차
1. [사전 준비](#사전-준비)
2. [환경 구축](#환경-구축)
3. [설치 검증](#설치-검증)
4. [문제 해결](#문제-해결)

---

## 사전 준비

### 1. Anaconda 설치

**다운로드:**
- [Anaconda 공식 사이트](https://www.anaconda.com/download)
- 또는 [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (최소 설치)

**설치 확인:**
```bash
# 명령 프롬프트 또는 Anaconda Prompt에서
conda --version
```

### 2. Git 설치 (선택사항)

```bash
# Git이 있는지 확인
git --version

# 없다면 설치: https://git-scm.com/download/win
```

---

## 환경 구축

### 방법 1: 자동 설치 (권장)

```bash
# Anaconda Prompt를 관리자 권한으로 실행

# 저장소 디렉토리로 이동
cd segnn-cpu-implementation

# 설치 스크립트 실행
environment_setup\install_windows.bat
```

### 방법 2: 수동 설치

#### Step 1: Conda 환경 생성

```bash
# Anaconda Prompt 실행 (관리자 권한)

# 환경 생성
conda create -n SegNN python=3.8 -y

# 환경 활성화
conda activate SegNN

# 활성화 확인 (프롬프트 앞에 (SegNN) 표시)
```

#### Step 2: PyTorch 설치

```bash
# CPU 버전 PyTorch 설치
conda install pytorch==1.12.0 torchvision==0.13.0 cpuonly -c pytorch -y

# 설치 확인
python -c "import torch; print('PyTorch:', torch.__version__)"
```

#### Step 3: 필수 패키지 설치

```bash
# 프로젝트 루트 디렉토리에서
pip install -r requirements.txt

# 설치 확인
pip list
```

#### Step 4: 더미 PointNet2 모듈 설치

```bash
# pointnet2_dummy 디렉토리로 이동
cd pointnet2_dummy

# 개발 모드로 설치
pip install -e .

# 상위 디렉토리로 복귀
cd ..
```

---

## 설치 검증

### 1. 환경 테스트

```bash
python scripts/test_environment.py
```

**예상 출력:**
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

### 2. Import 테스트

```bash
python scripts/test_imports.py
```

### 3. 샘플 데이터 생성 및 테스트

```bash
python scripts/create_sample_data.py
```

---

## 설치 후 체크리스트

- [ ] Conda 환경이 `SegNN` 이름으로 생성됨
- [ ] PyTorch CPU 버전이 설치됨 (`torch.cuda.is_available()` = False)
- [ ] 모든 필수 패키지가 설치됨 (`pip list` 확인)
- [ ] 더미 PointNet2 모듈이 import 됨
- [ ] 테스트 스크립트들이 정상 실행됨

---

## 환경 관리

### 환경 활성화/비활성화

```bash
# 활성화
conda activate SegNN

# 비활성화
conda deactivate
```

### 환경 삭제 (필요시)

```bash
# 환경 비활성화 후
conda deactivate

# 환경 삭제
conda env remove -n SegNN
```

### 환경 목록 확인

```bash
conda env list
```

---

## 시스템 요구사항

### 최소 사양
- **OS**: Windows 10 (64-bit)
- **RAM**: 8GB
- **저장공간**: 5GB
- **Python**: 3.8

### 권장 사양
- **OS**: Windows 10/11 (64-bit)
- **RAM**: 16GB
- **저장공간**: 10GB
- **CPU**: 4 cores 이상

---

## 다음 단계

설치가 완료되었다면:

1. **코드 구조 분석**
   ```bash
   python scripts/analyze_segnn.py
   ```

2. **문서 읽기**
   - [구현 일지](../docs/implementation_log.md)
   - [코드 분석 보고서](../docs/code_analysis.md)

3. **원본 Seg-NN 코드 탐색**
   - [GitHub 저장소](https://github.com/yangyangyang127/Seg-NN)

---

## 참고 자료

- [Conda 사용 가이드](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)
- [PyTorch 문서](https://pytorch.org/docs/stable/index.html)
- [Python 가상환경 가이드](https://docs.python.org/3/tutorial/venv.html)

---

**문제가 발생하면**: [troubleshooting.md](troubleshooting.md)를 참고하세요.
