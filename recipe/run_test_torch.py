import math

import torch
from sphericart.torch import SphericalHarmonics


xyz = torch.tensor(
    [
        [0.0, 0.0, 1.0],
        [1.0, 0.0, 0.0],
    ],
    dtype=torch.float64,
)

values = SphericalHarmonics(2).compute(xyz)
assert values.shape == (2, 9)
assert values.dtype == torch.float64

expected_z_axis = torch.tensor(
    [
        1.0 / (2.0 * math.sqrt(math.pi)),
        0.0,
        math.sqrt(3.0 / (4.0 * math.pi)),
        0.0,
        0.0,
        0.0,
        math.sqrt(5.0 / (4.0 * math.pi)),
        0.0,
        0.0,
    ],
    dtype=torch.float64,
)
torch.testing.assert_close(values[0], expected_z_axis, rtol=1e-12, atol=1e-12)
