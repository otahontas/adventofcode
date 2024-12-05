cmake_minimum_required(VERSION 3.10)

# Set the project name
project(AdventOfCode)

# Set C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Export compile commands and symlink it to root for langserver
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
execute_process(
    COMMAND ${CMAKE_COMMAND} -E create_symlink
        ${CMAKE_BINARY_DIR}/compile_commands.json
        ${CMAKE_SOURCE_DIR}/compile_commands.json
)

# Add libraries
add_library(utils utils/utils.cc)
add_library(int_code_comp int_code_comp/int_code_comp.cc)

# Add executables for each day
add_executable(01 01.cc)
add_executable(02 02.cc)
add_executable(03 03.cc)
add_executable(04 04.cc)
add_executable(05 05.cc)
add_executable(06 06.cc)
add_executable(07 07.cc)
add_executable(08 08.cc)
add_executable(09 09.cc)
add_executable(10 10.cc)

# Link libraries to executables
target_link_libraries(01 PRIVATE utils)
target_link_libraries(02 PRIVATE utils)
target_link_libraries(02 PRIVATE int_code_comp)
target_link_libraries(03 PRIVATE utils)
target_link_libraries(04 PRIVATE utils)
target_link_libraries(05 PRIVATE utils)
target_link_libraries(05 PRIVATE int_code_comp)
target_link_libraries(06 PRIVATE utils)
target_link_libraries(07 PRIVATE utils)
target_link_libraries(07 PRIVATE int_code_comp)
target_link_libraries(08 PRIVATE utils)
target_link_libraries(09 PRIVATE utils)
target_link_libraries(09 PRIVATE int_code_comp)
target_link_libraries(10 PRIVATE utils)
