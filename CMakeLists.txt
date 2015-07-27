project(cura-binary-data)

cmake_minimum_required(VERSION 2.8.12)

include(GNUInstallDirs)

install(DIRECTORY cura DESTINATION ${CMAKE_INSTALL_DATADIR})
install(DIRECTORY uranium DESTINATION ${CMAKE_INSTALL_DATADIR})
