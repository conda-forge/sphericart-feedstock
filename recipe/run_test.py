import math

import numpy as np
from sphericart import SolidHarmonics, SphericalHarmonics


def check_calculator(calculator_cls):
    xyz = np.array(
        [
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
        ],
        dtype=np.float64,
    )

    values = calculator_cls(2).compute(xyz)
    assert values.shape == (2, 9)
    assert values.dtype == np.float64

    expected_z_axis = np.array(
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
        dtype=np.float64,
    )
    np.testing.assert_allclose(values[0], expected_z_axis, rtol=1e-12, atol=1e-12)


check_calculator(SphericalHarmonics)
check_calculator(SolidHarmonics)
