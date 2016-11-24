llvm_map_components_to_libnames(llvm_libs
    Core
    Support
)

add_executable(Kaleidoscope-Ch3 toy.cpp)
target_link_libraries(Kaleidoscope-Ch3 ${llvm_libs})
