#pragma once
#ifndef LUA_HPP
#define LUA_HPP

// Adds the extern "C" directive around C source headers

#ifdef __cplusplus
extern "C"
{
#endif

	#include "lua.h"
	#include "lualib.h"
	#include "lauxlib.h"

#ifdef __cplusplus
};
#endif

#endif