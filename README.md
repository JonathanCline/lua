# Lua Fork 

This adds a CMakeLists to the source repo and constructs the basic set of targets for use with C++.

No functionality was added/modifed/removed - this fork contains purely structural changes.

The only new code file added is lua.hpp which exists purely to ease interopt between lua and C++


# CMake Targets :

`liblua` / `lua::lua` - Lua C API **static** library 

`libluadll` / `lua::luadll` - Lua C API **shared** library

`lua` - Lua Executable


**Include `lua.hpp` if you are using C++, or `lua.h` for C**



[main lua repo](https://github.com/lua/lua)

