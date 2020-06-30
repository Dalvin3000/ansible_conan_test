cmake_minimum_required(VERSION 3.16.0)

start_project()
define_project(
    QT
)

target_link_libraries(${PROJECT_NAME}
    PUBLIC
        Qt5::Core
        Qt5::Gui
        Qt5::Widgets
)

set_target_properties(${PROJECT_NAME}
    PROPERTIES
        CXX_STANDARD 20
)
