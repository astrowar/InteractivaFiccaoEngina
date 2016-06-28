#pragma once
#include <string>
#include <vector>
#include <memory>

enum DefProbality
{
	never = -10,
	sometimes = -3,
	not = -1,
	undefined = 0,
	normal = 1,
	mosty = 3,
	always = 10

};

DefProbality reverse_prob(DefProbality LK);

class CDefinition
{
public:
	DefProbality LK;
	CDefinition(DefProbality _k) :LK(_k){}
	virtual ~CDefinition(){};
};

using HDefinition = std::shared_ptr<CDefinition>;


class CEnumBool  // this is usually small
{
public:
	std::string value_true;
	std::string value_false;
	CEnumBool(std::string noum);;
	CEnumBool(std::string noum, std::string not_noum);
};

class CDefinitionBool: public  CDefinition
{
public:
   CEnumBool noums;
	CDefinitionBool(DefProbality _LK, CEnumBool _noums);
	CDefinitionBool(DefProbality _LK, std::string noum );
	CDefinitionBool(DefProbality _LK, std::string noum, std::string not_noum);
};


class CKind
{
public:
	std::string name;
	std::vector<HDefinition>  definitions;

	CKind(std::string _name): name(_name){}
	DefProbality query(std::string adjetive);
	bool KindCanBe(const HDefinition& hh);
};
using HKind = std::shared_ptr<CKind>;

class CInstancia
{
public:
	std::string name;
	HKind tipo;
	CInstancia(std::string _name , HKind _tipo) : name(_name), tipo(_tipo) {}

	DefProbality  query(std::string adjetive ) const;
};
using HInstancia = std::shared_ptr<CInstancia>;





class CTypeDefinition
{
public:
	HKind kind;
	HDefinition def;
	CTypeDefinition(HKind _kind, HDefinition _def);
};



class CInterpreter
{
public:
	CInterpreter();
	virtual ~CInterpreter();
	HKind addKind(const char* str);
	HInstancia   addInstancia(std::string name, std::string type);
	bool checkConflictDefinition(const HKind& c_kind, const HDefinition& hh);
	void addDefinition(const HKind& c_kind, const CDefinitionBool& c_definition_bool);
	std::vector<HKind> kinds;
	std::vector<HInstancia> instancias;
	std::vector<CTypeDefinition> type_definitions;
};

