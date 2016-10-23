project(cura-binary-data)

cmake_minimum_required(VERSION 2.8.12)

include(GNUInstallDirs)

option(ENABLE_FIRMWARE_INSTALL
       "Enable installation of firmware files" ON)
option(ENABLE_L18N_INSTALL
       "Enable installation of language files" ON)

if(ENABLE_L18N_INSTALL)
	install(DIRECTORY cura/resources/i18n DESTINATION ${CMAKE_INSTALL_DATADIR}/cura/resources/i18n)
	install(DIRECTORY uranium/resources/i18n DESTINATION ${CMAKE_INSTALL_DATADIR}/uranium/resources/i18n)
endif(ENABLE_L18N_INSTALL)

if(ENABLE_L18N_INSTALL)
	install(DIRECTORY cura/resources/firmware DESTINATION ${CMAKE_INSTALL_DATADIR}/cura/resources/firmware)
endif(ENABLE_L18N_INSTALL)

if(WIN32)
	install(FILES windows/vcredist_x64.exe DESTINATION ".")
	install(FILES windows/vcredist_x32.exe DESTINATION ".")
	install(DIRECTORY windows/arduino DESTINATION ".")
endif()
