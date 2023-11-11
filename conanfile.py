import os

from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.scm import Git, Version
from conan.tools.files import load, update_conandata

required_conan_version = ">=1.59.0"


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
        git = Git(self, self.recipe_folder)
        scm_url, scm_commit = git.get_url_and_commit()
        update_conandata(self, {"sources": {"commit": scm_commit, "url": scm_url}, "version": self.version})

    def source(self):
        git = Git(self)
        sources = self.conan_data["sources"]
        git.clone(url = sources["url"], target = ".")
        git.checkout(commit = sources["commit"])

    def validate(self):
        if (self.version != None) and (Version(self.version) <= Version("4")):
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
        if self.settings.os != "Windows":
            compatible_pkg = self.info.clone()
            compatible_pkg.settings.os = "Linux"
            self.compatible_packages.append(compatible_pkg)
