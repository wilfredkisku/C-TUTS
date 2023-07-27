# CPP-TUTS

## Setting CMAKE

CMake is an extensible, open-source system that manages the build process in an operating system and in a compiler-independent manner. Simple configuration files placed in each source directory (```CMakeLists.txt``` files) are used to generate standard build files (e.g., ```Makefiles``` on Unix and projects/workspaces in Windows MSVC) which are used in the usual way. ```CMakeLists.txt``` file contains a set of directives and instructions describing the project's source files and targets (executable, library, or both).

* It helps create a build environment for the compilation of the source code (C, C++ etc.), create libraries, generate wrappers and build executable binaries in arbitrary combinations. CMake supports in-place and out-of-place builds, and can therefore support multiple builds from a single source tree.
* CMake locates include files, libraries, and executables, and may encounter optional build directives. The information is gathered into the cache, which may be changed by the user prior to the generation of the native build files.

```PROJECT_SOURCE_DIR```: contains the full path to the root of your project source directory, i.e. to the nearest directory where ```CMakeLists.txt``` contains the ```PROJECT()``` command.
