#include "TextValue.h"



 


CTextValue::~CTextValue()
{
}

CTypeDefinitionText::CTypeDefinitionText(std::string name ,DefProbality _LK, CTextValue _value):CTypeDefinitionNamed(name,_LK),default_value(_value)
{
}
