"""
Dummy PointNet2 Package

This package provides placeholder implementations of PointNet2 operations
for CPU-only testing and code verification.
"""

from .pointnet2_ops import (
    furthest_point_sample,
    gather_operation,
    ball_query,
    group_points,
    three_nn,
    three_interpolate,
    pointnet2_utils
)

__version__ = "0.1.0-dummy"
__all__ = [
    "furthest_point_sample",
    "gather_operation",
    "ball_query",
    "group_points",
    "three_nn",
    "three_interpolate",
    "pointnet2_utils"
]
