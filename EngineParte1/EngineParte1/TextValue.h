#pragma once
#include <string>
#include "CDefinition.h"

class CTextValue
{
public:
	 
	std::string value;;
	CTextValue(std::string _value) : value(_value) {};
	virtual ~CTextValue();
};

 

class CTypeDefinitionText : public  CTypeDefinitionNamed
{
public:
	CTextValue default_value;
	CTypeDefinitionText(std::string name, DefProbality _LK, CTextValue _value);
	 
	  
};

using HTypeDefinitionText = std::shared_ptr<CTypeDefinitionText>;
