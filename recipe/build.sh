#!/bin/bash

set -eu

export TORCH_CUDA_ARCH_LIST="5.0;6.0;7.0;7.5;8.0;8.6;9.0;10.0;12.0+PTX"

python -m pip install . -vv
