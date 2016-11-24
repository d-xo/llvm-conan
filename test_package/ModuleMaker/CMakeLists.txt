llvm_map_components_to_libnames(llvm_libs
    BitWriter
    Core
    Support
)

add_executable(ModuleMaker ModuleMaker.cpp)
target_link_libraries(ModuleMaker ${llvm_libs})
