#pragma once
#include <string>
#include <vector>
#include "CDefinition.h"
#include "CEnumType.h"
#include "CSetType.h"
#include "CValueBase.h"
#include "TextValue.h"


class CKind
{
public:
	std::string name;
	std::vector<HTypeDefinition>  definitions;

	CKind(std::string _name): name(_name){}
	DefProbality query(std::string adjetive);
	bool KindCanBe(const HTypeDefinition& hh);
};
using HKind = std::shared_ptr<CKind>;

 



class CKindTypeDefinition
{
public:
	HKind kind;
	HTypeDefinition def;
	CKindTypeDefinition(HKind _kind, HTypeDefinition _def);
};


 


class CInstancia
{
public:
	std::string name;
	HKind tipo;
	std::vector<CTypeValue>  values;
	CInstancia(std::string _name, HKind _tipo) : name(_name), tipo(_tipo) {}

	void setValue(CTypeValue val);
	DefProbality  query(std::string adjetive) const;
};
using HInstancia = std::shared_ptr<CInstancia>;





class CTypeValueBool : public  CTypeValue
{
public:
	CEnumBoolValue value;
	 
	CTypeValueBool(CEnumBoolValue _value, HTypeDefinitionBool _def): CTypeValue(_def), value(_value)
	{};
};


class CTypeValueSet : public  CTypeValue
{
public:
	CEnumSetValue value;
    CTypeValueSet(CEnumSetValue _value, HTypeDefinitionSet _def) : CTypeValue(_def), value(_value)
	{};
};

class CTypeValueText : public  CTypeValue
{
public:
	CTextValue value;
	CTypeValueText(CTextValue _value, HTypeDefinitionSet _def) : CTypeValue(_def), value(_value)
	{};
};
 


bool setValue(CTypeValue *RV, CTypeValue *LV);

class CInterpreter
{
public:
	CInterpreter();
	virtual ~CInterpreter();
	HKind addKind(const char* str);
	HInstancia   addInstancia(std::string name, std::string type);
	bool checkConflictDefinition(const HKind& c_kind, const HTypeDefinition& hh) const;
	void addDefinition(const HKind& c_kind, const CTypeDefinitionBool& c_definition_bool);
	std::vector<HKind> kinds;
	std::vector<HInstancia> instancias;
	std::vector<CKindTypeDefinition> type_definitions;
};

