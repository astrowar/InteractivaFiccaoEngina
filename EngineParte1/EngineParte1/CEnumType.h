#pragma once
#include <memory>
#include <string>
#include "CDefinition.h"

class CEnumBoolValue
{
public:
	std::string value;;
	CEnumBoolValue(std::string noum) : value(noum) {};
};

class CEnumBoolValues  // this is usually small
{
public:
	CEnumBoolValue value_true;
	CEnumBoolValue  value_false;
	CEnumBoolValues(std::string noum);;
	CEnumBoolValues(std::string noum, std::string not_noum);
};

class CTypeDefinitionBool: public  CTypeDefinition
{
public:
	CEnumBoolValues noums;
	CTypeDefinitionBool(DefProbality _LK, CEnumBoolValues _noums);
	CTypeDefinitionBool(DefProbality _LK, std::string noum );
	CTypeDefinitionBool(DefProbality _LK, std::string noum, std::string not_noum);
};

using HTypeDefinitionBool = std::shared_ptr<CTypeDefinitionBool>;
