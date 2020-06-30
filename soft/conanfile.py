from conans import ConanFile, tools


class AnsibleTestConan(ConanFile):
    name = "ansible_test"
    version = "0.1"
    settings = "os", "build_type", "arch" #, "compiler"
    description = "<Description of AnsibleTest here>"
    default_user = "yeesha"
    default_channel = "testing"
    url = "None"
    license = "None"
    author = "None"
    topics = None

    #! Compatibility between binaries
    # def package_id(self):
        # self.info.settings.compiler.version = "10"
        # self.info.settings.compiler.libcxx = "libstdc++11"

    #! not needed for app-packages
    # def package_info(self):
    #     self.cpp_info.libs = tools.collect_libs(self)

    def package(self):
        if (self.settings.os == "Windows"):
            self.copy("*", dst="bin",           src="out/bin",           keep_path=False)
            self.copy("*", dst="bin/platforms", src="out/bin/platforms", keep_path=False)
        else:
            self.copy("*", dst="bin",           src="V:/__install_Linux-Clang-Release/bin",           keep_path=False, symlinks=True)
            self.copy("*", dst="lib",           src="V:/__install_Linux-Clang-Release/lib",           keep_path=False, symlinks=True)
            self.copy("*", dst="lib/platforms", src="V:/__install_Linux-Clang-Release/lib/platforms", keep_path=False, symlinks=True)

    def deploy(self):
        self.copy("*", dst=self.name, symlinks=True)


# conan export-pkg . ansible_test/0.1@maintainer/nix_stable -pr=linux -f
# conan export-pkg . ansible_test/0.1@maintainer/win_stable -pr=msvc -f
# conan upload ansible_test --all -r local -c --force
