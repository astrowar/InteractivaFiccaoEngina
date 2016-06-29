#pragma once
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

class CTypeDefinition
{
public:
	DefProbality LK;
	CTypeDefinition(DefProbality _k) :LK(_k){} 
	virtual ~CTypeDefinition(){};
};

using HTypeDefinition = std::shared_ptr<CTypeDefinition>;


class CTypeDefinitionNamed: public CTypeDefinition
{
public:
	std::string name  ;
	CTypeDefinitionNamed(std::string _name, DefProbality _k) :CTypeDefinition(_k), name(_name) {};
 
};