llvm_map_components_to_libnames(llvm_libs all)

add_executable(Kaleidoscope-Ch8 toy.cpp)
target_link_libraries(Kaleidoscope-Ch8 ${llvm_libs})
