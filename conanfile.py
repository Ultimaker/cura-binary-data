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
        if tools.Version(self.version) <= tools.Version("4"):
            raise ConanInvalidConfiguration("Only versions 5+ are support")

    def package(self):
        self.copy("*", src = "cura", dst = os.path.join(self.cpp.package.resdirs[0], "cura"))
        self.copy("*", src = "uranium", dst = os.path.join(self.cpp.package.resdirs[0], "uranium"))

        if self.settings.os == "Windows":
            self.copy("*", src = "windows", dst = os.path.join(self.cpp.package.resdirs[0], "windows"))

    def package_id(self):
        del self.info.settings.compiler
        del self.info.settings.build_type
