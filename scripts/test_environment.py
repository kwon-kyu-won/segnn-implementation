"""
Environment Test Script for Seg-NN CPU Implementation

This script verifies that the environment is correctly set up.
"""

import sys
import torch
import numpy as np

print("=" * 60)
print("CPU Environment Test for Seg-NN")
print("=" * 60)

# 1. PyTorch 확인
print("\n1. PyTorch Information:")
print(f"   PyTorch Version: {torch.__version__}")
print(f"   CUDA Available: {torch.cuda.is_available()}")
print(f"   CPU threads: {torch.get_num_threads()}")

if torch.cuda.is_available():
    print("   ⚠ WARNING: CUDA is available but this project uses CPU only")
else:
    print("   ✓ CPU-only mode (correct for this project)")

# 2. 기본 연산 테스트
print("\n2. Testing basic operations...")
try:
    x = torch.randn(10, 3)
    y = torch.randn(3, 5)
    z = torch.mm(x, y)
    print(f"   ✓ Matrix multiplication: {z.shape}")
except Exception as e:
    print(f"   ✗ Error: {e}")
    sys.exit(1)

# 3. PointNet2 import 테스트
print("\n3. Testing PointNet2 import...")
try:
    from pointnet2_ops import pointnet2_utils
    print("   ✓ PointNet2 operations imported")
    print("   ⚠ Note: Using dummy implementation (CPU only)")
except ImportError as e:
    print(f"   ✗ Failed to import PointNet2: {e}")
    print("   → Run: cd pointnet2_dummy && pip install -e . && cd ..")
    sys.exit(1)

# 4. PointNet2 함수 테스트
print("\n4. Testing PointNet2 functions...")
try:
    # Test FPS
    xyz = torch.randn(2, 100, 3)
    idx = pointnet2_utils.furthest_point_sample(xyz, 32)
    print(f"   ✓ FPS output shape: {idx.shape}")
    
    # Test ball query
    new_xyz = torch.randn(2, 32, 3)
    ball_idx = pointnet2_utils.ball_query(0.2, 16, xyz, new_xyz)
    print(f"   ✓ Ball query output shape: {ball_idx.shape}")
except Exception as e:
    print(f"   ✗ Error: {e}")
    sys.exit(1)

# 5. 메모리 테스트
print("\n5. Memory test...")
try:
    points = torch.randn(2, 512, 3)
    print(f"   Point cloud shape: {points.shape}")
    memory_mb = points.element_size() * points.nelement() / (1024 * 1024)
    print(f"   Memory usage: {memory_mb:.2f} MB")
except Exception as e:
    print(f"   ✗ Error: {e}")
    sys.exit(1)

# 6. NumPy 호환성 테스트
print("\n6. NumPy compatibility test...")
try:
    np_array = np.random.randn(10, 3)
    torch_tensor = torch.from_numpy(np_array)
    print(f"   ✓ NumPy to Torch: {torch_tensor.shape}")
except Exception as e:
    print(f"   ✗ Error: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("All tests passed! ✓")
print("=" * 60)
print("\nEnvironment is ready for Seg-NN code verification.")
print("\nNext steps:")
print("  1. python scripts/test_imports.py")
print("  2. python scripts/create_sample_data.py")
print("  3. Explore Seg-NN code structure")
print("\nNote: This environment is for code verification only.")
print("For actual experiments, GPU environment is required.")
print("=" * 60)
