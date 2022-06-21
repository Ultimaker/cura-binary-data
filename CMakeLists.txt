# For MSVC flags, will be ignored on non-Windows OS's and this project in general. Only needed for cura-build-environment.
cmake_policy(SET CMP0091 NEW)

project(cura-binary-data)

cmake_minimum_required(VERSION 2.8.12)

include(GNUInstallDirs)

option(ENABLE_FIRMWARE_INSTALL
    "Enable installation of firmware files" ON)
option(ENABLE_I18N_INSTALL
    "Enable installation of language files" ON)
option(ENABLE_WHATSNEW_INSTALL
    "Enable installation of What's New files" ON)

if(ENABLE_I18N_INSTALL)
    install(DIRECTORY cura/resources/i18n DESTINATION ${CMAKE_INSTALL_DATADIR}/cura/resources)
    install(DIRECTORY uranium/resources/i18n DESTINATION ${CMAKE_INSTALL_DATADIR}/uranium/resources)
endif(ENABLE_I18N_INSTALL)

if(ENABLE_FIRMWARE_INSTALL)
    install(DIRECTORY cura/resources/firmware DESTINATION ${CMAKE_INSTALL_DATADIR}/cura/resources)
endif(ENABLE_FIRMWARE_INSTALL)

if(ENABLE_WHATSNEW_INSTALL)
    install(FILES cura/resources/images/whats_new/0.png
                  cura/resources/images/whats_new/1.png
                  cura/resources/images/whats_new/2.png
                  cura/resources/images/whats_new/3.png
                  cura/resources/images/whats_new/4.png
                  cura/resources/images/whats_new/0.gif
                  cura/resources/images/whats_new/1.gif
                  cura/resources/images/whats_new/2.gif
                  cura/resources/images/whats_new/3.gif
                  cura/resources/images/whats_new/4.gif
            DESTINATION ${CMAKE_INSTALL_DATADIR}/cura/resources/images/whats_new OPTIONAL)
    install(FILES cura/resources/texts/whats_new/0.html
                  cura/resources/texts/whats_new/1.html
                  cura/resources/texts/whats_new/2.html
                  cura/resources/texts/whats_new/3.html
                  cura/resources/texts/whats_new/4.html
            DESTINATION ${CMAKE_INSTALL_DATADIR}/cura/resources/texts/whats_new OPTIONAL)
endif()

if(WIN32)
    install(DIRECTORY windows/arduino DESTINATION ".")
endif()
