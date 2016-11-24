llvm_map_components_to_libnames(llvm_libs
    Analysis
    Core
    ExecutionEngine
    InstCombine
    Object
    OrcJIT
    RuntimeDyld
    ScalarOpts
    Support
    TransformUtils
    native
)

add_executable(BuildingAJIT-Ch5-Server server.cpp)
target_link_libraries(BuildingAJIT-Ch5-Server ${llvm_libs})
