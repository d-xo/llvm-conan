llvm_map_components_to_libnames(llvm_libs
    BitWriter
    Core
    ExecutionEngine
    MC
    Support
    nativecodegen
)

add_executable(BrainF
    BrainF.cpp
    BrainFDriver.cpp
)

target_link_libraries(BrainF ${llvm_libs})
