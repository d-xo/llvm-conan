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

add_executable(BuildingAJIT-Ch2 toy.cpp)
target_link_libraries(BuildingAJIT-Ch2 ${llvm_libs})
