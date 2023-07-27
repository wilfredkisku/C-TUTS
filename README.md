# CPP-TUTS

## Setting CMAKE

CMake is an extensible, open-source system that manages the build process in an operating system and in a compiler-independent manner. Simple configuration files placed in each source directory (```CMakeLists.txt``` files) are used to generate standard build files (e.g., ```Makefiles``` on Unix and projects/workspaces in Windows MSVC) which are used in the usual way. ```CMakeLists.txt``` file contains a set of directives and instructions describing the project's source files and targets (executable, library, or both).

* It helps create a build environment for the compilation of the source code (C, C++ etc.), create libraries, generate wrappers and build executable binaries in arbitrary combinations. CMake supports in-place and out-of-place builds, and can therefore support multiple builds from a single source tree.
* CMake locates include files, libraries, and executables, and may encounter optional build directives. The information is gathered into the cache, which may be changed by the user prior to the generation of the native build files.

## Creating the CMake config file

1. CMakeLists.txt file is placed at the source of the project you want to build.
2. Some commonly used commands
    * ```message```: prints given message
    * ```cmake_minimum_required```: sets minimum version of cmake to be used
    * ```add_executable```: adds executable target with given name
    * ```add_library```: adds a library target to be build from listed source files
    * ```add_subdirectory```: adds a subdirectory to build
    * ```file```: Read content from a file called <filename> and store it in a <variable>. Optionally start from the given <offset> and read at most <max-in> bytes. The HEX option causes data to be converted to a hexadecimal representation (useful for binary data). If the HEX option is specified, letters in the output (a through f) are in lowercase.
       * ```file(READ <filename> <variable> [OFFSET <offset>] [LIMIT <max-in>] [HEX])```

```PROJECT_SOURCE_DIR```: contains the full path to the root of your project source directory, i.e. to the nearest directory where ```CMakeLists.txt``` contains the ```PROJECT()``` command.
