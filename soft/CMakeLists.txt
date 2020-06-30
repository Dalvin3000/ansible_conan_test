cmake_minimum_required(VERSION 3.16.0)

project(ansible_test)

include(${CMAKE_CURRENT_LIST_DIR}/cmake/common.cmake)


# core parameters
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)


# install qt plugins
install_qt_plugins(
    Gui:QWindowsIntegrationPlugin
    Gui:QXcbIntegrationPlugin
)


# define product components
collect_projects_with_deps(
    FIND_NONEXISTENT
    FAIL_ON_NOT_FOUND
    ROOT_PATHS
        libs
        apps
)


message(STATUS "--------------------------------------------------")


# -- manifest
get_project_version_tag(. MAIN)
get_project_version_tag_author(. BUNDLE_AUTHOR)


# -- package
package_bundle(
    PROJECT
        ${PROJECT_NAME}
    VERSION_VAR
        MAIN
    CONTACT
        "${BUNDLE_AUTHOR}"
    DESCRIPTION
        "-"
    VENDOR
        "Pay-Trans"
    NO_COMPONENT_IN_PATH FORCE_Z
)

include(CPack)
