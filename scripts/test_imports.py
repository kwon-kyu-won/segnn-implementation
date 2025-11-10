"""
Import Test Script

Tests all required package imports for Seg-NN
"""

import sys

print("=" * 60)
print("Testing Package Imports")
print("=" * 60)

packages_to_test = [
    ("torch", "PyTorch"),
    ("torchvision", "TorchVision"),
    ("numpy", "NumPy"),
    ("scipy", "SciPy"),
    ("sklearn", "Scikit-learn"),
    ("h5py", "H5Py"),
    ("yaml", "PyYAML"),
    ("tqdm", "TQDM"),
    ("matplotlib", "Matplotlib"),
]

failed = []
passed = []

for module_name, display_name in packages_to_test:
    try:
        module = __import__(module_name)
        version = getattr(module, "__version__", "unknown")
        print(f"✓ {display_name:20s} {version}")
        passed.append(display_name)
    except ImportError as e:
        print(f"✗ {display_name:20s} FAILED: {e}")
        failed.append(display_name)

# Test PointNet2
print("\nTesting PointNet2 Operations:")
try:
    from pointnet2_ops import pointnet2_utils
    print("✓ PointNet2 operations   (dummy implementation)")
    passed.append("PointNet2 (dummy)")
except ImportError as e:
    print(f"✗ PointNet2 operations   FAILED: {e}")
    failed.append("PointNet2")

print("\n" + "=" * 60)
print(f"Results: {len(passed)} passed, {len(failed)} failed")
print("=" * 60)

if failed:
    print("\n⚠ Failed imports:")
    for pkg in failed:
        print(f"  - {pkg}")
    print("\nTo install missing packages:")
    print("  pip install -r requirements.txt")
    sys.exit(1)
else:
    print("\n✓ All required packages are installed!")
    print("\nYour environment is ready for Seg-NN development.")
    
print("=" * 60)
