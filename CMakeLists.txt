project(cura-binary-data)

cmake_minimum_required(VERSION 2.8.12)

include(GNUInstallDirs)

option(ENABLE_FIRMWARE_INSTALL
       "Enable installation of firmware files" ON)
option(ENABLE_I18N_INSTALL
       "Enable installation of language files" ON)

if(ENABLE_I18N_INSTALL)
	install(DIRECTORY cura/resources/i18n DESTINATION ${CMAKE_INSTALL_DATADIR}/cura/resources)
	install(DIRECTORY uranium/resources/i18n DESTINATION ${CMAKE_INSTALL_DATADIR}/uranium/resources)
endif(ENABLE_I18N_INSTALL)

if(ENABLE_FIRMWARE_INSTALL)
	install(DIRECTORY cura/resources/firmware DESTINATION ${CMAKE_INSTALL_DATADIR}/cura/resources)
endif(ENABLE_FIRMWARE_INSTALL)

if(WIN32)
	install(FILES windows/vcredist_x64.exe DESTINATION ".")
	install(FILES windows/vcredist_x32.exe DESTINATION ".")
	install(DIRECTORY windows/arduino DESTINATION ".")
endif()
