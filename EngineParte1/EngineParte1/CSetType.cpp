#include "CSetType.h"
#include <algorithm>


CEnumSetValues::CEnumSetValues(std::string noum1, std::string noum2)
{
	values.push_back(CEnumSetValue(noum1));
	values.push_back(CEnumSetValue(noum2));

}

CEnumSetValues::CEnumSetValues(std::string noum1, std::string noum2, std::string noum3)
{
	values.push_back(CEnumSetValue(noum1));
	values.push_back(CEnumSetValue(noum2));
	values.push_back(CEnumSetValue(noum3));
}

CEnumSetValues::CEnumSetValues(std::string noum1, std::string noum2, std::string noum3, std::string noum4)
{
	values.push_back(CEnumSetValue(noum1));
	values.push_back(CEnumSetValue(noum2));
	values.push_back(CEnumSetValue(noum3));
	values.push_back(CEnumSetValue(noum4));
}

bool CEnumSetValues::isInSet(CEnumSetValue v)
{
	return isInSet(v.value);
}

bool CEnumSetValues::isInSet(std::string v)
{
	auto item = std::find_if(values.begin(), values.end(), [&v](CEnumSetValue &s) {return s.value == v; });
	if (item != values.end()) return true;
	return false;

}

CTypeDefinitionSet::CTypeDefinitionSet(DefProbality _LK, CEnumSetValue _default_value, CEnumSetValues _noums): CTypeDefinition(_LK), noums(_noums), default_value(_default_value)
{
	if (noums.isInSet(_default_value) == false )
	{
		default_value = noums.values[0];
	}
}
