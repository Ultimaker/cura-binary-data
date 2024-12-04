import os

from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.scm import Version
from conan.tools.files import copy, update_conandata

required_conan_version = ">=2.7.0"


class CuraBinaryDataConan(ConanFile):
    name = "cura_binary_data"
    license = "LGPL-3.0"
    author = "Ultimaker B.V."
    url = "https://github.com/Ultimaker/cura-binary-data"
    description = "Contains binary data for Cura releases, like compiled translations and firmware."
    topics = ("conan", "binaries", "translation", "firmware", "cura")
    exports = "LICENSE*"
    settings = "os", "compiler", "build_type", "arch"
    no_copy_source = True

    def set_version(self):
        if not self.version:
            self.version = self.conan_data["version"]

    def export(self):
        update_conandata(self, {"version": self.version})

    def export_sources(self):
        copy(self, "*", os.path.join(self.recipe_folder, "cura"), os.path.join(self.export_sources_folder, "cura"))
        copy(self, "*", os.path.join(self.recipe_folder, "uranium"), os.path.join(self.export_sources_folder, "uranium"))
        copy(self, "*", os.path.join(self.recipe_folder, "windows"), os.path.join(self.export_sources_folder, "windows"))

    def layout(self):
        self.cpp.package.resdirs = [os.path.join("resources", "cura"), os.path.join("resources", "uranium"), "windows"]

    def package(self):
        copy(self, "*", src = os.path.join(self.export_sources_folder, "cura"), dst = os.path.join(self.package_folder, self.cpp.package.resdirs[0]))
        copy(self, "*", src = os.path.join(self.export_sources_folder, "uranium"), dst = os.path.join(self.package_folder, self.cpp.package.resdirs[1]))

        if self.settings.os == "Windows":
            copy(self, "*", src = os.path.join(self.export_sources_folder, "windows"), dst = os.path.join(self.package_folder, self.cpp.package.resdirs[2]))

    def package_info(self):
        if self.settings.os == "Windows":
            self.runenv_info.append_path("PATH", os.path.join(self.cpp.package.resdirs[2], "arduino", "amd64"))
            self.runenv_info.append_path("PATH", os.path.join(self.cpp.package.resdirs[2], "arduino", "CP210x_6.7.4"))
            self.runenv_info.append_path("PATH", os.path.join(self.cpp.package.resdirs[2], "arduino", "FTDI USB Drivers", "amd64"))

    def compatibility(self):
        del self.info.settings.compiler
        del self.info.settings.build_type
        if self.info.settings.os != "Windows":
            return [{"settings": [("os", "Linux")]}]
