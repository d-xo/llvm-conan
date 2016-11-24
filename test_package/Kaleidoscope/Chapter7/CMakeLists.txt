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

add_executable(Kaleidoscope-Ch7 toy.cpp)
target_link_libraries(Kaleidoscope-Ch7 ${llvm_libs})
