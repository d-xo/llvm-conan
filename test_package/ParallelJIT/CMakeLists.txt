llvm_map_components_to_libnames(llvm_libs
    Core
    ExecutionEngine
    Interpreter
    MC
    Support
    nativecodegen
)

add_executable(ParallelJIT ParallelJIT.cpp)
target_link_libraries(ParallelJIT ${PTHREAD_LIB})
target_link_libraries(ParallelJIT ${llvm_libs})
