# 문제 해결 가이드 (Troubleshooting)

이 문서는 Seg-NN CPU 환경 구축 시 자주 발생하는 문제들과 해결 방법을 정리한 것입니다.

## 목차
1. [Conda 관련 문제](#conda-관련-문제)
2. [PyTorch 설치 문제](#pytorch-설치-문제)
3. [패키지 의존성 문제](#패키지-의존성-문제)
4. [PointNet2 관련 문제](#pointnet2-관련-문제)
5. [실행 오류](#실행-오류)

---

## Conda 관련 문제

### 문제 1: `conda` 명령어를 찾을 수 없음

**증상:**
```
'conda'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
배치 파일이 아닙니다.
```

**해결 방법:**

1. **Anaconda Prompt 사용**
   - 일반 명령 프롬프트 대신 "Anaconda Prompt" 실행
   - 시작 메뉴에서 검색

2. **환경 변수 설정**
   ```
   제어판 → 시스템 → 고급 시스템 설정 → 환경 변수
   Path에 다음 경로 추가:
   - C:\Users\[사용자명]\anaconda3
   - C:\Users\[사용자명]\anaconda3\Scripts
   - C:\Users\[사용자명]\anaconda3\Library\bin
   ```

3. **Conda 초기화**
   ```bash
   conda init cmd.exe
   # 또는
   conda init powershell
   ```

---

### 문제 2: 환경 생성 실패

**증상:**
```
CondaValueError: prefix already exists
```

**해결 방법:**
```bash
# 기존 환경 삭제
conda env remove -n SegNN

# 다시 생성
conda create -n SegNN python=3.8 -y
```

---

## PyTorch 설치 문제

### 문제 3: PyTorch 설치 중 오류

**증상:**
```
PackagesNotFoundError: The following packages are not available from current channels
```

**해결 방법:**

1. **채널 추가**
   ```bash
   conda config --add channels conda-forge
   conda config --add channels pytorch
   ```

2. **특정 버전 설치**
   ```bash
   # 더 최신 버전 시도
   conda install pytorch torchvision cpuonly -c pytorch
   ```

3. **pip로 설치**
   ```bash
   pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
   ```

---

### 문제 4: CUDA 관련 오류

**증상:**
```
RuntimeError: CUDA out of memory
```

**해결 방법:**
이 프로젝트는 CPU 전용입니다. CUDA 오류가 발생하면:

```python
# Python에서 확인
import torch
print(torch.cuda.is_available())  # False여야 함
```

만약 True라면 PyTorch CPU 버전을 재설치:
```bash
pip uninstall torch torchvision
conda install pytorch torchvision cpuonly -c pytorch
```

---

## 패키지 의존성 문제

### 문제 5: NumPy 버전 충돌

**증상:**
```
ImportError: numpy.core.multiarray failed to import
```

**해결 방법:**
```bash
# NumPy 재설치
pip uninstall numpy
pip install numpy==1.19.5
```

---

### 문제 6: h5py 설치 오류

**증상:**
```
error: Microsoft Visual C++ 14.0 is required
```

**해결 방법:**

1. **pip wheel 사용**
   ```bash
   pip install --only-binary=h5py h5py
   ```

2. **conda로 설치**
   ```bash
   conda install h5py
   ```

---

## PointNet2 관련 문제

### 문제 7: PointNet2 Import 실패

**증상:**
```
ModuleNotFoundError: No module named 'pointnet2_ops'
```

**해결 방법:**

1. **더미 모듈 재설치**
   ```bash
   cd pointnet2_dummy
   pip install -e . --force-reinstall
   cd ..
   ```

2. **Python Path 확인**
   ```python
   import sys
   print(sys.path)
   # 프로젝트 디렉토리가 포함되어 있는지 확인
   ```

---

### 문제 8: 실제 PointNet2 컴파일 시도

**증상:**
```
error: subprocess-exited-with-error
```

**이것은 정상입니다!**
- 본 프로젝트는 더미 모듈을 사용합니다
- 실제 PointNet2 컴파일은 필요하지 않습니다
- Windows CPU 환경에서는 컴파일이 어렵습니다

---

## 실행 오류

### 문제 9: 메모리 부족

**증상:**
```
MemoryError: Unable to allocate array
```

**해결 방법:**

1. **배치 크기 줄이기**
   - 코드에서 `batch_size` 파라미터를 줄임

2. **포인트 수 줄이기**
   - `pc_npts` 파라미터를 512 또는 그 이하로 설정

3. **백그라운드 프로그램 종료**
   - 메모리를 많이 사용하는 다른 프로그램 종료

---

### 문제 10: Import 오류

**증상:**
```
ImportError: cannot import name 'xxx' from 'yyy'
```

**해결 방법:**

1. **환경 확인**
   ```bash
   # 올바른 환경이 활성화되어 있는지
   conda env list
   # SegNN 옆에 * 표시가 있어야 함
   ```

2. **패키지 재설치**
   ```bash
   pip install --force-reinstall -r requirements.txt
   ```

---

### 문제 11: 경로 문제

**증상:**
```
FileNotFoundError: [Errno 2] No such file or directory
```

**해결 방법:**

1. **작업 디렉토리 확인**
   ```bash
   # 현재 위치 확인
   cd
   
   # 프로젝트 루트로 이동
   cd segnn-cpu-implementation
   ```

2. **절대 경로 사용**
   - Windows에서는 `/` 대신 `\` 또는 `\\` 사용
   - 또는 Python에서는 `/` 사용 가능

---

## Python 버전 문제

### 문제 12: Python 3.8 외 버전 사용

**증상:**
호환성 문제 또는 예상치 못한 오류

**해결 방법:**

```bash
# 환경 삭제
conda env remove -n SegNN

# Python 3.8로 재생성
conda create -n SegNN python=3.8 -y
```

**참고:** Python 3.9나 3.10도 대부분 작동하지만, 3.8이 가장 안정적입니다.

---

## 일반적인 디버깅 팁

### 1. 환경 정보 수집

```bash
# 시스템 정보
python --version
conda --version
pip --version

# 설치된 패키지
pip list

# 환경 변수
echo %PATH%
```

### 2. 깨끗한 재설치

```bash
# 1. 환경 삭제
conda deactivate
conda env remove -n SegNN

# 2. conda 캐시 정리
conda clean --all

# 3. 처음부터 재설치
conda create -n SegNN python=3.8 -y
conda activate SegNN
# ... (나머지 설치 과정)
```

### 3. 로그 확인

대부분의 오류는 상세한 오류 메시지를 제공합니다:
- **빨간색 텍스트**를 주의 깊게 읽기
- **첫 번째 오류**가 실제 원인인 경우가 많음
- 오류 메시지를 Google에서 검색

---

## 추가 도움

### 문서 참고
- [설치 가이드](setup_guide.md)
- [구현 일지](../docs/implementation_log.md)

### 온라인 리소스
- [PyTorch Forum](https://discuss.pytorch.org/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/pytorch)
- [Conda Documentation](https://docs.conda.io/)

### GitHub Issues
- 본 저장소의 Issues 탭에 질문 올리기
- 원본 Seg-NN 저장소 Issues 참고

---



