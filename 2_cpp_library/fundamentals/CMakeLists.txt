cmake_minimum_required(VERSION 3.14)
project(cpp_fundamentals LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(SOURCES
    01_types_io.cpp
    02_pointers_references.cpp
    03_stl_containers.cpp
    04_classes_raii.cpp
    05_templates.cpp
    06_smart_pointers.cpp
)

foreach(src ${SOURCES})
    get_filename_component(name ${src} NAME_WE)
    add_executable(${name} ${src})
endforeach()
