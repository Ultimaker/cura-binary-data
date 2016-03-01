project(cura-binary-data)

cmake_minimum_required(VERSION 2.8.12)

include(GNUInstallDirs)

install(DIRECTORY cura DESTINATION ${CMAKE_INSTALL_DATADIR})
install(DIRECTORY uranium DESTINATION ${CMAKE_INSTALL_DATADIR})

if(WIN32)
	install(FILES windows/vcredist_x64.exe DESTINATION ".")
	install(FILES windows/vcredist_x32.exe DESTINATION ".")
	install(DIRECTORY windows/arduino DESTINATION ".")
endif()
