# Dummy PointNet2 Operations

이 패키지는 PointNet2 operations의 더미(placeholder) 구현을 제공합니다.

## 주의사항

**이것은 실제 PointNet2 구현이 아닙니다!**

- 코드 구조 검증 및 Import 테스트 목적
- 실제 알고리즘 대신 단순한 대체 함수 제공
- CPU 환경에서 컴파일 없이 사용 가능

## 설치

```bash
pip install -e .
```

## 사용법

```python
from pointnet2_ops import pointnet2_utils

# FPS (Furthest Point Sampling)
idx = pointnet2_utils.furthest_point_sample(xyz, npoint)

# Ball Query
idx = pointnet2_utils.ball_query(radius, nsample, xyz, new_xyz)
```

## 제공되는 함수

- `furthest_point_sample`: FPS 샘플링
- `gather_operation`: Feature 수집
- `ball_query`: 반경 내 이웃 탐색
- `group_points`: 포인트 그룹화
- `three_nn`: 3-최근접 이웃 탐색
- `three_interpolate`: 3점 보간

## 실제 PointNet2 사용

실제 실험을 위해서는:
1. GPU 환경 확보
2. 실제 PointNet2 라이브러리 설치
3. 본 더미 모듈 제거

```bash
pip uninstall pointnet2_ops
# 실제 PointNet2 설치
```
