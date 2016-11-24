llvm_map_components_to_libnames(llvm_libs
    Analysis
    Core
    ExecutionEngine
    InstCombine
    Object
    RuntimeDyld
    ScalarOpts
    Support
    native
)

add_executable(Kaleidoscope-Ch6 toy.cpp)
target_link_libraries(Kaleidoscope-Ch6 ${llvm_libs})
