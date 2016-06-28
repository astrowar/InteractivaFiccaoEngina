// EngineParte1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cassert>
#include "Engine.h"
#include "Grammar.h"


CEngine  * makeEngine()
{
	
	return new CEngine();
}

bool   teste_1()
{
	CEngine* cint = makeEngine();

	//testa a engine
	return cint != nullptr; 
}

bool   teste_2()
{
	CEngine* cint = makeEngine();
	CAssertion q(INoum("book"), IVP(IVerb("is"), IJJ("thing")));
	cint->assign(CFact(q,Probality::normal));
	return cint->factos.size() > 0;
}

bool   teste_3()
{
	CEngine* cint = makeEngine();
	const CFact q(INoum("book"), IVP(IVerb("is"), IJJ("thing")));
	cint->assign(q);
	LikellyResult r = cint->query(q);
	return r.value > 0  ;
}
 
bool   teste_4()
{
	CEngine* cint = makeEngine();
	const CFact fact(INoum("book"), IVP(_not(IVerb("is")), IJJ("thing")));
	cint->assign(fact);
	const CAssertion question(INoum("book"), IVP(IVerb("is"), IJJ("thing")));
	LikellyResult r = cint->query(question);
	return r.value < 0;
}

int main()
{

	assert(teste_1());
	assert(teste_2());
	assert(teste_3());
	assert(teste_4());
    return 0;
}

