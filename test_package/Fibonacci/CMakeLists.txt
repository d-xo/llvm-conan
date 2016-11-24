llvm_map_components_to_libnames(llvm_libs
    Core
    ExecutionEngine
    Interpreter
    MC
    MCJIT
    Support
    nativecodegen
)

add_executable(Fibonacci
    fibonacci.cpp
)

target_link_libraries(Fibonacci ${llvm_libs})
