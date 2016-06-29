#pragma once
#include "CDefinition.h"


class CTypeValue
{
public:

	HTypeDefinition def;
	CTypeValue(HTypeDefinition _def) : def(_def)
	{}; 
	virtual ~CTypeValue(){}
};
