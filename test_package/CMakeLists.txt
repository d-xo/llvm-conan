cmake_minimum_required(VERSION 3.7.0)
project(conan-llvm-test)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(LLVM 3.9 REQUIRED CONFIG)
message(STATUS "Found LLVM ${LLVM_PACKAGE_VERSION}")
message(STATUS "Using LLVMConfig.cmake in: ${LLVM_DIR}")

include_directories(${LLVM_INCLUDE_DIRS})
link_directories(${LLVM_LIBRARY_DIRS})
add_definitions(${LLVM_DEFINITIONS})

add_subdirectory(BrainF)
add_subdirectory(Fibonacci)
add_subdirectory(HowToUseJIT)
add_subdirectory(Kaleidoscope)
add_subdirectory(ModuleMaker)
add_subdirectory(parallelJIT)
