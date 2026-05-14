set "SPHERICART_ARCH_NATIVE=OFF"

%PYTHON% -m pip install . -vv --no-deps --no-build-isolation
if errorlevel 1 exit 1
