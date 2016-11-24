llvm_map_components_to_libnames(llvm_libs
    Core
    ExecutionEngine
    Interpreter
    MC
    Support
    nativecodegen
)

add_executable(HowToUseJIT
    HowToUseJIT.cpp
)

target_link_libraries(HowToUseJIT ${llvm_libs})
