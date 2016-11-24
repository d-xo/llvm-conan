llvm_map_components_to_libnames(llvm_libs
    Core
    ExecutionEngine
    Object
    Support
    native
)

add_executable(Kaleidoscope-Ch9 toy.cpp)
target_link_libraries(Kaleidoscope-Ch9 ${llvm_libs})
