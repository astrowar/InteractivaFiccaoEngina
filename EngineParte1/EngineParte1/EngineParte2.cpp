
// Definicoes sao DECLARE de baixo nivel do interpretador

#include <cassert>
#include "Interprter.h"


CInterpreter  * makeCInterpreter()
{

	return new CInterpreter();
}




bool teste_1b()
{
	CInterpreter  *cint = makeCInterpreter();

	return cint != nullptr;
}
bool teste_2b()
{
	CInterpreter  *cint = makeCInterpreter();

	auto k =  cint->addKind("Thing");
	assert(k != nullptr);
	auto obj = cint->addInstancia("book", "Thing");

	assert( obj != nullptr);
	return obj->tipo == k;
}

bool teste_3b()
{
	CInterpreter  *cint = makeCInterpreter();

	auto k = cint->addKind("Thing");
	cint->addDefinition( k,  CDefinitionBool(DefProbality::normal,"small"));
	auto obj = cint->addInstancia("book", "Thing");

	float lk = obj->query("small");
	return (lk> 0);
}

bool teste_4b()
{
	CInterpreter  *cint = makeCInterpreter();

	auto k = cint->addKind("Thing");
	cint->addDefinition(k, CDefinitionBool(mosty, "small","big"));
	auto _book = cint->addInstancia("book", "Thing");

	auto lk1 = _book->query("red");
	assert(lk1 == 0); // undefined definition 

	auto lk2 = _book->query("big");
	return (lk2 < 0);
}

bool testes_definitions()
{
	assert(teste_1b());
	assert(teste_2b());
	assert(teste_3b());
	assert(teste_4b());
	return true;
}
