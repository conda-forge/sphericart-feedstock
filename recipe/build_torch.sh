#!/bin/bash

set -eu

export TORCH_CUDA_ARCH_LIST="5.0;6.0;7.0;7.5;8.0;8.6;9.0;10.0;12.0+PTX"
export SPHERICART_ARCH_NATIVE="OFF"

cd sphericart-torch

"${PYTHON}" -m pip install . -vv --no-deps --no-build-isolation
