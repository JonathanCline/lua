#
#	Lua CMakeLists added by JonathanCline
#
#
#  CMakeLists added by Jonathan Cline
#     https://github.com/JonathanCline/lua
#

# Should match the version of lua this provides
set(lua_version 5.4)

# Where to find the lua source files
set(lua_source_dir "${CMAKE_CURRENT_SOURCE_DIR}/src")

# Where to find the lua include headers
set(lua_include_dir "include")


# Basic cmake setup
cmake_minimum_required(VERSION 3.2 FATAL_ERROR)

# Woo lua!
project(lua VERSION ${lua_version} LANGUAGES C HOMEPAGE_URL "https://github.com/JonathanCline/lua")

# Options for controlling installation
option(LUA_INSTALL "Allows lua targets to be installed" ON)
option(LUA_INSTALL_EXECUTABLE "Enables the lua executable to be installed, LUA_INSTALL must be ON" ON)
option(LUA_INSTALL_STATIC_LIBRARY "Enables the lua static library to be installed, LUA_INSTALL must be ON" ON)
option(LUA_INSTALL_DYNAMIC_LIBRARY "Enables the lua dynamic library to be installed, LUA_INSTALL must be ON" ON)

# Lua include headers
set(lua_include_lib
	lua.hpp
	lua.h
	luaconf.h
	lualib.h
	lauxlib.h
)


# Lua "core" sources list
set(lua_src_core
  lapi.c
  lcode.c
  lctype.c
  ldebug.c
  ldo.c
  ldump.c
  lfunc.c
  lgc.c
  llex.c
  lmem.c
  lobject.c  
  lopcodes.c  
  lparser.c  
  lstate.c  
  lstring.c  
  ltable.c
  ltm.c 
  lundump.c  
  lvm.c 
  lzio.c
)

# Lua "lib" target sources list
set (lua_src_lib
  lauxlib.c
  lbaselib.c
  lcorolib.c
  ldblib.c
  liolib.c
  lmathlib.c
  loslib.c
  lstrlib.c
  ltablib.c
  lutf8lib.c
  loadlib.c
  linit.c
)

# Lua executable sources
set(lua_src
  lua.c
) 


# Prepend soures with the lua source dir path
list(TRANSFORM lua_src PREPEND "${lua_source_dir}/")
list(TRANSFORM lua_src_lib PREPEND "${lua_source_dir}/")
list(TRANSFORM lua_src_core PREPEND "${lua_source_dir}/")

# Prepend includes with the lua include dir path
list(TRANSFORM lua_include_lib PREPEND "${lua_include_dir}/")



# The list of public include directories
set(lua_public_include ${lua_include_dir})

# The list of private include directories
set(lua_private_include ${lua_source_dir})


# Lua static library target
add_library(liblua ${lua_src_core} ${lua_src_lib})
target_include_directories(liblua
	PUBLIC ${lua_public_include}
	PRIVATE ${lua_private_include}
)



# Lua shared library target
add_library(libluadll SHARED ${lua_src_core} ${lua_src_lib} )
target_include_directories(libluadll
  PUBLIC ${lua_public_include}
  PRIVATE ${lua_private_include}
)



target_compile_definitions(libluadll
	PRIVATE _CRT_SECURE_NO_WARNINGS LUA_BUILD_AS_DLL )
set_target_properties(libluadll PROPERTIES OUTPUT_NAME lua53)



# Lua command line executable target
add_executable(lua ${lua_src})
target_link_libraries(lua libluadll)
target_include_directories(lua
	PRIVATE ${lua_private_include}
)

# Install configuration
if (LUA_INSTALL) 

  # Executable install
  if (LUA_INSTALL_EXECUTABLE)
    install(TARGETS lua DESTINATION "bin/")
  endif()
  
  # Static library install
  if (LUA_INSTALL_STATIC_LIBRARY)
    install(TARGETS liblua DESTINATION "lib/")
  endif()

  # Dynamic library install
  if (LUA_INSTALL_DYNAMIC_LIBRARY)
    install(TARGETS libluadll DESTINATION "lib/")
  endif()
    
  # Header file install configuration
  if (LUA_INSTALL_STATIC_LIBRARY OR LUA_INSTALL_DYNAMIC_LIBRARY)
    foreach (fpath IN LISTS lua_include_lib)
      install(FILES "${fpath}" DESTINATION "include/")
    endforeach()
  endif()

endif()


# Add library alias targets for eas of use

# Static library for the lua C API 
add_library(lua::lua ALIAS liblua)

# Shared library for the lua C API 
add_library(lua::luadll ALIAS libluadll)

