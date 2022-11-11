import os

from conan import ConanFile
from conans import tools
from conan.errors import ConanInvalidConfiguration

required_conan_version = ">=1.47.0"


class CuraBinaryDataConan(ConanFile):
    name = "cura_binary_data"
    license = "LGPL-3.0"
    author = "Ultimaker B.V."
    url = "https://github.com/Ultimaker/cura-binary-data"
    description = "Contains binary data for Cura releases, like compiled translations and firmware."
    topics = ("conan", "binaries", "translation", "firmware", "cura")
    build_policy = "missing"
    exports = "LICENSE*"
    settings = "os", "compiler", "build_type", "arch"
    no_copy_source = True
    scm = {
        "type": "git",
        "subfolder": ".",
        "url": "auto",
        "revision": "auto"
    }

    def validate(self):
        if (self.version != None) and (tools.Version(self.version) <= tools.Version("4")):
            raise ConanInvalidConfiguration("Only versions 5+ are supported!")

    def layout(self):
        self.cpp.package.resdirs = [os.path.join("resources", "cura"), os.path.join("resources", "uranium"), "windows"]

    def package(self):
        self.copy("*", src = "cura", dst = self.cpp.package.resdirs[0])
        self.copy("*", src = "uranium", dst = self.cpp.package.resdirs[1])

        if self.settings.os == "Windows":
            self.copy("*", src = "windows", dst = self.cpp.package.resdirs[2])

    def package_info(self):
        if self.settings.os == "Windows":
            self.runenv_info.append_path("PATH", os.path.join(self.cpp.package.resdirs[2], "arduino", "amd64"))
            self.runenv_info.append_path("PATH", os.path.join(self.cpp.package.resdirs[2], "arduino", "CP210x_6.7.4"))
            self.runenv_info.append_path("PATH", os.path.join(self.cpp.package.resdirs[2], "arduino", "FTDI USB Drivers", "amd64"))

    def package_id(self):
        del self.info.settings.compiler
        del self.info.settings.build_type
