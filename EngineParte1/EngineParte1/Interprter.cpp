#include "Interprter.h"


DefProbality reverse_prob(DefProbality LK)
{
	if (LK == DefProbality::never) return DefProbality::always;
	if (LK == DefProbality::sometimes) return DefProbality::mosty;
	if (LK == DefProbality::normal) return DefProbality::not;
	if (LK == DefProbality::not) return DefProbality::normal;
	if (LK == DefProbality::mosty) return DefProbality::sometimes;
	if (LK == DefProbality::always) return DefProbality::never;
	return DefProbality::undefined;
}

CEnumBoolValues::CEnumBoolValues(std::string noum): value_true(noum), value_false("not " + noum)
{
}

CEnumBoolValues::CEnumBoolValues(std::string noum, std::string not_noum): value_true(noum), value_false(not_noum)
{
}

CTypeDefinitionBool::CTypeDefinitionBool(DefProbality _LK, CEnumBoolValues _noums): CTypeDefinition(_LK), noums(_noums)
{
}

CTypeDefinitionBool::CTypeDefinitionBool(DefProbality _LK, std::string noum) : CTypeDefinition(_LK), noums(CEnumBoolValues(noum))
{

}

CTypeDefinitionBool::CTypeDefinitionBool(DefProbality _LK, std::string noum, std::string not_noum) : CTypeDefinition(_LK), noums(CEnumBoolValues(noum,not_noum))
{
}

DefProbality  CKind::query(std::string adjetive)
{
	for (auto it = definitions.begin(); it != definitions.end(); ++it)
	{
		CTypeDefinitionBool *cb = dynamic_cast<CTypeDefinitionBool*>((*it).get());
		if ( cb != nullptr)
		{
			if (cb->noums.value_true.value == adjetive) return cb->LK;
			if (cb->noums.value_false.value == adjetive) return reverse_prob(cb->LK);
		}
	}
	return DefProbality::undefined;
}

bool CKind::KindCanBe(const HTypeDefinition & hh)
{
	return true;
}



void CInstancia::setValue(CTypeValue val)
{
	// find for what definitions is value belong ...
	HTypeDefinition d = val.def;
	// ja existe esse tipo setado na instancia .
	for(auto it = values.begin(); it != values.end();++it)
	{
		if(it->def == d)
		{
			//temos uma valor ja definido para esta declaracao 
			// vamos fazer o override do valor 
			
		} 

	}
}

DefProbality CInstancia::query(std::string adjetive) const
{
	return (tipo->query(adjetive));

}

 

CKindTypeDefinition::CKindTypeDefinition(HKind _kind, HTypeDefinition _def):kind(_kind), def( _def)
{
	_kind->definitions.push_back(def);
}

CInterpreter::CInterpreter()
{
}


CInterpreter::~CInterpreter()
{
}

HKind CInterpreter::addKind(const char* str)
{
	HKind c = std::make_shared<CKind>(str);
	this->kinds.push_back(c);
	return c;
}

HInstancia CInterpreter::addInstancia(std::string name, std::string tipo)
{
	for (auto it = kinds.begin(); it != kinds.end(); ++it)
	{
		if ((*it)->name != tipo) continue;
		HInstancia c = std::make_shared<CInstancia>(name, *it);
		this->instancias.push_back(c);
		return c;
	}
	return nullptr;
}

bool CInterpreter::checkConflictDefinition(const HKind & c_kind, const HTypeDefinition & hh) const
{
 bool b = c_kind->KindCanBe(  hh);
 return b;

}

void CInterpreter::addDefinition(const HKind& c_kind, const CTypeDefinitionBool& c_definition_bool)
{
	HTypeDefinition hh = std::make_shared<CTypeDefinitionBool>(c_definition_bool);
	if (checkConflictDefinition(c_kind, hh) == false) return;
	 
	type_definitions.push_back(CKindTypeDefinition(c_kind, hh));
}

bool setValueBool(CTypeValue * RV, CTypeValue * LV)
{
	CTypeValueBool * RBool = dynamic_cast<CTypeValueBool*>(RV);
	if (RBool != nullptr)
	{
		CTypeValueBool* LBool = dynamic_cast<CTypeValueBool*>(LV);
		if (LBool != nullptr)
		{
			RBool->value = LBool->value;
			return true;
		}
	}
	return false;
}


bool setValueSet(CTypeValue * RV, CTypeValue * LV)
{
	CTypeValueSet * RSet = dynamic_cast<CTypeValueSet*>(RV);
	if (RSet != nullptr)
	{
		CTypeValueSet* LSet = dynamic_cast<CTypeValueSet*>(LV);
		if (LSet != nullptr)
		{
			RSet->value = LSet->value;
			return true;
		}
	}
	return false;
}


bool setValue(CTypeValue *RV, CTypeValue *LV)
{
	if (setValueSet(RV, LV)) return true;
	if (setValueBool(RV, LV)) return true;
	return false;
}