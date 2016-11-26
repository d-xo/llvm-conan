# llvm-conan

Conan package for llvm 3.9 that includes the following components:

    - llvm
    - clang
    - compiler-rt
    - openmp
    - libcxx
    - libcxxabi
    - clang-tools-extra

## Usage

You will need to use `find_package(LLVM)` in your CMakeLists to make use of llvm (check the examples in the [`test_package`]())
