#pragma once
#include <memory>
#include <string>
#include "CDefinition.h"


class CEnumSetValue
{
public:
	std::string value;;
	CEnumSetValue(std::string noum) : value(noum) {};
};

class CEnumSetValues  // this is usually small
{
public:
	std::vector<CEnumSetValue> values;
	 
	 
	CEnumSetValues(std::string noum1, std::string noum2);
	CEnumSetValues(std::string noum1, std::string noum2, std::string noum3);
	CEnumSetValues(std::string noum1, std::string noum2, std::string noum3, std::string noum4);

	bool isInSet(CEnumSetValue v);
	bool isInSet(std::string v);
};


class CTypeDefinitionSet : public  CTypeDefinition
{
public:
	CEnumSetValues noums;
	CEnumSetValue default_value;
	CTypeDefinitionSet(DefProbality _LK, CEnumSetValue  _default_value, CEnumSetValues _noums);
	 
};

using HTypeDefinitionSet = std::shared_ptr<CTypeDefinitionSet>;