"""
Create Sample Data for Testing

Generates small synthetic point cloud data for testing purposes
"""

import numpy as np
import os
import torch

print("=" * 60)
print("Creating Sample Point Cloud Data")
print("=" * 60)

# Create output directory
output_dir = "sample_data"
os.makedirs(output_dir, exist_ok=True)

# Parameters
n_samples = 5
n_points = 512
n_classes = 3
n_features = 6  # xyz + rgb

print(f"\nParameters:")
print(f"  Number of samples: {n_samples}")
print(f"  Points per sample: {n_points}")
print(f"  Number of classes: {n_classes}")
print(f"  Features per point: {n_features} (xyz + rgb)")

# Generate samples
print(f"\nGenerating samples...")
for i in range(n_samples):
    # Generate random point cloud
    # xyz coordinates: [-1, 1]
    xyz = np.random.randn(n_points, 3).astype(np.float32)
    
    # rgb colors: [0, 1]
    rgb = np.random.rand(n_points, 3).astype(np.float32)
    
    # Combine xyz + rgb
    points = np.concatenate([xyz, rgb], axis=1)
    
    # Generate random labels
    labels = np.random.randint(0, n_classes, n_points).astype(np.int32)
    
    # Save as NumPy files
    np.save(os.path.join(output_dir, f"sample_{i}_points.npy"), points)
    np.save(os.path.join(output_dir, f"sample_{i}_labels.npy"), labels)
    
    print(f"  ✓ Sample {i}: points {points.shape}, labels {labels.shape}")

# Also create PyTorch tensor versions
print(f"\nCreating PyTorch tensor versions...")
for i in range(n_samples):
    points = np.load(os.path.join(output_dir, f"sample_{i}_points.npy"))
    labels = np.load(os.path.join(output_dir, f"sample_{i}_labels.npy"))
    
    points_tensor = torch.from_numpy(points)
    labels_tensor = torch.from_numpy(labels)
    
    torch.save({
        'points': points_tensor,
        'labels': labels_tensor
    }, os.path.join(output_dir, f"sample_{i}.pt"))
    
    print(f"  ✓ Sample {i}.pt saved")

# Create a simple batch for testing
print(f"\nCreating batched data...")
batch_points = []
batch_labels = []

for i in range(min(3, n_samples)):  # Use first 3 samples
    points = np.load(os.path.join(output_dir, f"sample_{i}_points.npy"))
    labels = np.load(os.path.join(output_dir, f"sample_{i}_labels.npy"))
    batch_points.append(points)
    batch_labels.append(labels)

batch_points = np.stack(batch_points, axis=0)  # (batch, n_points, features)
batch_labels = np.stack(batch_labels, axis=0)  # (batch, n_points)

np.save(os.path.join(output_dir, "batch_points.npy"), batch_points)
np.save(os.path.join(output_dir, "batch_labels.npy"), batch_labels)

print(f"  ✓ Batch: points {batch_points.shape}, labels {batch_labels.shape}")

# Create statistics file
print(f"\nCreating statistics...")
stats = {
    'n_samples': n_samples,
    'n_points': n_points,
    'n_classes': n_classes,
    'n_features': n_features,
    'point_range': [-1.0, 1.0],
    'color_range': [0.0, 1.0]
}

# Save statistics
import json
with open(os.path.join(output_dir, "stats.json"), 'w') as f:
    json.dump(stats, f, indent=2)

print("=" * 60)
print("Sample data creation completed!")
print("=" * 60)

print(f"\nCreated files in '{output_dir}/':")
print(f"  - {n_samples} × .npy point files")
print(f"  - {n_samples} × .npy label files")
print(f"  - {n_samples} × .pt PyTorch files")
print(f"  - 1 × batch files")
print(f"  - 1 × stats.json")

print(f"\nTotal data size:")
data_size = sum(
    os.path.getsize(os.path.join(output_dir, f))
    for f in os.listdir(output_dir)
) / (1024 * 1024)
print(f"  {data_size:.2f} MB")

print("\nUsage example:")
print("  import numpy as np")
print(f"  points = np.load('{output_dir}/sample_0_points.npy')")
print(f"  labels = np.load('{output_dir}/sample_0_labels.npy')")
print("  print(points.shape, labels.shape)")

print("\nOr with PyTorch:")
print("  import torch")
print(f"  data = torch.load('{output_dir}/sample_0.pt')")
print("  points, labels = data['points'], data['labels']")

print("=" * 60)
