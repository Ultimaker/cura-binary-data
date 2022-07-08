# cura-binary-data

<p align="center">
    <a href="https://github.com/Ultimaker/cura-binary-data/actions/workflows/conan-package.yml" alt="Unit Tests">
        <img src="https://github.com/Ultimaker/cura-binary-data/actions/workflows/conan-package.yml/badge.svg" /></a>
    <a href="https://github.com/Ultimaker/cura-binary-data/issues" alt="Open Issues">
        <img src="https://img.shields.io/github/issues/ultimaker/cura-binary-data" /></a>
    <a href="https://github.com/Ultimaker/cura-binary-data/issues?q=is%3Aissue+is%3Aclosed" alt="Closed Issues">
        <img src="https://img.shields.io/github/issues-closed/ultimaker/cura-binary-data?color=g" /></a>
    <a href="https://github.com/Ultimaker/cura-binary-data/pulls" alt="Pull Requests">
        <img src="https://img.shields.io/github/issues-pr/ultimaker/cura-binary-data" /></a>
    <a href="https://github.com/Ultimaker/cura-binary-data/graphs/contributors" alt="Contributors">
        <img src="https://img.shields.io/github/contributors/ultimaker/cura-binary-data" /></a>
    <a href="https://github.com/Ultimaker/cura-binary-data" alt="Repo Size">
        <img src="https://img.shields.io/github/repo-size/ultimaker/cura-binary-data?style=flat" /></a>
    <a href="https://github.com/Ultimaker/cura-binary-data/blob/master/LICENSE" alt="License">
        <img src="https://img.shields.io/github/license/ultimaker/cura-binary-data?style=flat" /></a>
</p>


Contains binary data for Cura releases, like compiled translations and firmware..

## License

![License](https://img.shields.io/github/license/ultimaker/cura-binary-data?style=flat)  
cura-binary-data is released under terms of the AGPLv3 License. Terms of the license can be found in the LICENSE file. Or at
http://www.gnu.org/licenses/agpl.html

> But in general it boils down to:  
> **You need to share the source of any cura-binary-data modifications if you make an application with cura-binary-data.**


## How to set up a development environment

> **Note:**  
> We are currently in the process of switch our builds and pipelines to an approach which uses [Conan](https://conan.io/)
> and pip to manage our dependencies, which are stored on our JFrog Artifactory server and in the pypi.org.
> At the moment not everything is fully ported yet, so bare with us.

If you want to develop Cura with cura-binary-data see the Cura Wiki: [Running Cura from source](https://github.com/Ultimaker/Cura/wiki/Running-Cura-from-Source)

If you have never used [Conan](https://conan.io/) read their [documentation](https://docs.conan.io/en/latest/index.html)
which is quite extensive and well maintained. Conan is a Python program and can be installed using pip

```bash
pip install conan --upgrade
conan config install https://github.com/ultimaker/conan-config.git
conan profile new default --detect
```

**Community developers would have to remove the Conan `cura` repository because that one requires credentials.**
```bash
conan remote remove cura
```

## Creating a new cura-binary-data Conan package

To create a new cura-binary-data Conan package such that it can be used in Cura, run the following command:

```shell
conan export-pkg . cura_binary_data/<version>@<username>/<channel>
```

This package will be stored in the local Conan cache (`~/.conan/data` or `C:\Users\username\.conan\data` ) and can be used in downstream
projects, such as Cura, by adding it as a requirement in the `conanfile.py` or in `conandata.yml` if that project is set up
in such a way. You can also specify the override at the commandline, to use the newly created package, when you execute the `conan install`
command in the root of the consuming project, with:

```shell
conan install . -build=missing --update --require-override=cura_binary_data/<version>@<username>/<channel>
```
