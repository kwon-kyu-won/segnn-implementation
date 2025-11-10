"""
Dummy PointNet2 Operations for CPU-only Testing

This module provides placeholder implementations of PointNet2 operations
for code structure verification and testing without actual CUDA/C++ compilation.

WARNING: This is NOT a functional implementation. It only provides
the correct function signatures for import testing and code validation.

For actual 3D point cloud processing, use the real PointNet2 library
with GPU support.
"""

import torch
import warnings

__version__ = "0.1.0-dummy"
__all__ = [
    "furthest_point_sample",
    "gather_operation",
    "ball_query",
    "group_points",
    "three_nn",
    "three_interpolate"
]

# Issue warning on import
warnings.warn(
    "Using DUMMY PointNet2 operations! "
    "This is for code structure verification only. "
    "For actual experiments, use real PointNet2 with GPU.",
    UserWarning
)


def furthest_point_sample(xyz, npoint):
    """
    Dummy implementation of Furthest Point Sampling (FPS)
    
    Real implementation: Iteratively samples the farthest point from existing set
    Dummy implementation: Random sampling
    
    Args:
        xyz: (B, N, 3) tensor of point positions
        npoint: number of points to sample
        
    Returns:
        (B, npoint) tensor of sampled indices
    """
    B, N, _ = xyz.shape
    
    # Random sampling instead of actual FPS
    idx = torch.randint(0, N, (B, npoint), device=xyz.device)
    
    return idx


def gather_operation(features, idx):
    """
    Dummy implementation of feature gathering
    
    Real implementation: Gathers features according to indices
    Dummy implementation: Returns features as-is
    
    Args:
        features: (B, C, N) tensor of features
        idx: (B, npoint) tensor of indices
        
    Returns:
        (B, C, npoint) tensor of gathered features
    """
    B, C, N = features.shape
    _, npoint = idx.shape
    
    # Simple gather operation
    # In real implementation, this would use optimized CUDA kernels
    idx_expanded = idx.unsqueeze(1).expand(B, C, npoint)
    gathered = torch.gather(features, 2, idx_expanded)
    
    return gathered


def ball_query(radius, nsample, xyz, new_xyz):
    """
    Dummy implementation of ball query
    
    Real implementation: Finds points within radius of query points
    Dummy implementation: Random sampling
    
    Args:
        radius: search radius
        nsample: maximum number of points to sample in each ball
        xyz: (B, N, 3) tensor of point positions
        new_xyz: (B, S, 3) tensor of query positions
        
    Returns:
        (B, S, nsample) tensor of indices
    """
    B, N, _ = xyz.shape
    _, S, _ = new_xyz.shape
    
    # Random sampling instead of actual ball query
    idx = torch.randint(0, N, (B, S, nsample), device=xyz.device)
    
    return idx


def group_points(points, idx):
    """
    Dummy implementation of point grouping
    
    Args:
        points: (B, C, N) tensor of point features
        idx: (B, npoint, nsample) tensor of indices
        
    Returns:
        (B, C, npoint, nsample) tensor of grouped features
    """
    B, C, N = points.shape
    _, npoint, nsample = idx.shape
    
    # Simple grouping
    idx_expanded = idx.view(B, 1, npoint * nsample).expand(B, C, -1)
    grouped = torch.gather(points, 2, idx_expanded)
    grouped = grouped.view(B, C, npoint, nsample)
    
    return grouped


def three_nn(unknown, known):
    """
    Dummy implementation of 3-nearest neighbor search
    
    Real implementation: Finds 3 nearest neighbors for interpolation
    Dummy implementation: Random selection
    
    Args:
        unknown: (B, n, 3) tensor of unknown points
        known: (B, m, 3) tensor of known points
        
    Returns:
        dist: (B, n, 3) tensor of distances
        idx: (B, n, 3) tensor of indices
    """
    B, n, _ = unknown.shape
    _, m, _ = known.shape
    
    # Random selection instead of actual NN search
    idx = torch.randint(0, m, (B, n, 3), device=unknown.device)
    dist = torch.rand(B, n, 3, device=unknown.device)
    
    return dist, idx


def three_interpolate(points, idx, weight):
    """
    Dummy implementation of 3-point interpolation
    
    Args:
        points: (B, c, m) tensor of point features
        idx: (B, n, 3) tensor of neighbor indices
        weight: (B, n, 3) tensor of interpolation weights
        
    Returns:
        (B, c, n) tensor of interpolated features
    """
    B, c, m = points.shape
    _, n, _ = idx.shape
    
    # Simple weighted average
    idx_expanded = idx.view(B, 1, n, 3).expand(B, c, n, 3)
    gathered = torch.gather(
        points.unsqueeze(-1).expand(B, c, m, 3),
        2,
        idx_expanded
    )
    
    weight_expanded = weight.unsqueeze(1).expand(B, c, n, 3)
    interpolated = (gathered * weight_expanded).sum(dim=-1)
    
    return interpolated


# Compatibility aliases
class pointnet2_utils:
    """Compatibility class matching original PointNet2 API"""
    
    furthest_point_sample = staticmethod(furthest_point_sample)
    gather_operation = staticmethod(gather_operation)
    ball_query = staticmethod(ball_query)
    group_points = staticmethod(group_points)
    three_nn = staticmethod(three_nn)
    three_interpolate = staticmethod(three_interpolate)


# Print warning message
print("=" * 60)
print("WARNING: Using DUMMY PointNet2 Operations")
print("=" * 60)
print("This module provides placeholder implementations only.")
print("For actual 3D experiments, install real PointNet2 with GPU.")
print("=" * 60)
