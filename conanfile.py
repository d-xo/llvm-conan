from conans import ConanFile, CMake
from os.path import join
from os import makedirs, environ

class LLVMConan(ConanFile):
    name = "llvm"
    version = "3.9"
    settings = "os", "compiler", "build_type", "arch"
    install_dir = 'install' # must be relative

    # ---------------------------------------------------------
    #  Helper
    # ---------------------------------------------------------

    def package_directory(self, directory):
        self.copy(
            pattern='*',
            dst=directory,
            src=join(self.install_dir, directory),
            keep_path=True
        )

    def checkout_repo(self, url, destination):
        self.run(
            'git clone '
            '--recursive '
            '-b release_39 '
            '--depth=1 '
            '--shallow-submodules '
            '{0} {1}'.format(
                url, destination
            )
        )

    # ---------------------------------------------------------
    #  Install
    # ---------------------------------------------------------

    def source(self):
        self.checkout_repo('http://llvm.org/git/llvm.git', 'llvm')
        self.checkout_repo('http://llvm.org/git/clang.git', 'llvm/tools/clang')
        self.checkout_repo('http://llvm.org/git/compiler-rt.git', 'llvm/projects/compiler-rt')
        self.checkout_repo('http://llvm.org/git/openmp.git', 'llvm/projects/openmp')
        self.checkout_repo('http://llvm.org/git/libcxx.git', 'llvm/projects/libcxx')
        self.checkout_repo('http://llvm.org/git/libcxxabi.git', 'llvm/projects/libcxxabi')
        self.checkout_repo('http://llvm.org/git/clang-tools-extra.git', 'llvm/tools/clang/tools/extra')

    def build(self):
        cmake = CMake(self.settings)
        makedirs(self.install_dir)

        self.run(
            'cmake {0} {1} '
            '-DLLVM_OPTIMIZED_TABLEGEN=ON '
            '-DLIBOMP_ARCH=x86_64 '
            '-DLLVM_INCLUDE_DOCS=OFF '
            '-DLLVM_BUILD_EXTERNAL_COMPILER_RT=ON '
            '-DLLVM_BUILD_LLVM_DYLIB=ON '
            '-DLLVM_ENABLE_RTTI=ON '
            '-DLLVM_ENABLE_EH=ON '
            '-DLLVM_INSTALL_UTILS=ON '
            '-DLLVM_ENABLE_LIBCXX=ON '
            '-DWITH_POLLY=ON '
            '-DLINK_POLLY_INTO_TOOLS=ON '
            '-DCMAKE_INSTALL_PREFIX={2} '
            .format(
                join(self.conanfile_directory, 'llvm'),
                cmake.command_line,
                join(self.conanfile_directory, self.install_dir)
            )
        )

        if (environ['LLVM_CONAN_UNIT_TESTS'] == 'TRUE'):
            self.run('cmake --build . -- check {0}'.format(cmake.build_config))
            self.run('cmake --build . -- check-clang {0}'.format(cmake.build_config))

        self.run('cmake --build . -- install {0}'.format(cmake.build_config))

    def package(self):
        for directory in ['include', 'bin', 'lib', 'libexec', 'share']:
            self.package_directory(directory)

    def package_info(self):
        pass
