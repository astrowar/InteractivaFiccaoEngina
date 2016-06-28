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

CEnumBool::CEnumBool(std::string noum): value_true(noum), value_false("not " + noum)
{
}

CEnumBool::CEnumBool(std::string noum, std::string not_noum): value_true(noum), value_false(not_noum)
{
}

CDefinitionBool::CDefinitionBool(DefProbality _LK, CEnumBool _noums): CDefinition(_LK), noums(_noums)
{
}

CDefinitionBool::CDefinitionBool(DefProbality _LK, std::string noum) : CDefinition(_LK), noums(CEnumBool(noum))
{

}

CDefinitionBool::CDefinitionBool(DefProbality _LK, std::string noum, std::string not_noum) : CDefinition(_LK), noums(CEnumBool(noum,not_noum))
{
}

DefProbality  CKind::query(std::string adjetive)
{
	for (auto it = definitions.begin(); it != definitions.end(); ++it)
	{
		CDefinitionBool *cb = dynamic_cast<CDefinitionBool*>((*it).get());
		if ( cb != nullptr)
		{
			if (cb->noums.value_true == adjetive) return cb->LK;
			if (cb->noums.value_false == adjetive) return reverse_prob(cb->LK);
		}
	}
	return DefProbality::undefined;
}

DefProbality CInstancia::query(std::string adjetive) const
{
	return (tipo->query(adjetive));

}

 

CTypeDefinition::CTypeDefinition(HKind _kind, HDefinition _def):kind(_kind), def( _def)
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

bool CInterpreter::checkConflictDefinition(const HKind & c_kind, const HDefinition & hh)
{
 bool b = c_kind->KindCanBe(  hh);
 return b;

}

void CInterpreter::addDefinition(const HKind& c_kind, const CDefinitionBool& c_definition_bool)
{
	HDefinition hh = std::make_shared<CDefinitionBool>(c_definition_bool);
	if (checkConflictDefinition(c_kind, hh) == false) return;
	 
	type_definitions.push_back(CTypeDefinition(c_kind, hh));
}
