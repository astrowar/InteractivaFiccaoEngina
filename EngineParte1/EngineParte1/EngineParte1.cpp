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


INoum _book = INoum("book");
IVerb _is = IVerb("is");

IVP __is(IJJ jj)
{
	return IVP(_is, jj);
}

IVP __not_is(IJJ jj)
{
	return  IVP(_not(_is), jj);
}


bool   teste_1a()
{
	CEngine* cint = makeEngine();

	//testa a engine
	return cint != nullptr; 
}

bool   teste_2a()
{
	CEngine* cint = makeEngine();
	CAssertion q(_book, __is(IJJ("thing")));
	cint->assign(CFact( Probality::normal,q));
	return cint->factos.size() > 0;
}

bool   teste_3a()
{
	CEngine* cint = makeEngine();
	const CFact q(_book, __is(IJJ("thing")));
	cint->assign(q);
	LikellyResult r = cint->query(q);
	return r.value > 0  ;
}
 
bool   teste_4a()
{
	CEngine* cint = makeEngine();
	const CFact fact(_book, __not_is( IJJ("thing")));
	cint->assign(fact);
	const CAssertion question(_book, __is(IJJ("thing")));
	LikellyResult r = cint->query(question);
	return r.value < 0;
}


bool   teste_5a()
{
	CEngine* cint = makeEngine();
	const CFact fact(_book, __is(IJJ("thing")));
	cint->assign(fact);
	const CAssertion question(_book, __is(IJJ("red")));
	LikellyResult r = cint->query(question);
	return r.value == 0;
}

bool   teste_6a()
{
	CEngine* cint = makeEngine();
	const CFact fact_1(Probality::never,  CAssertion( _book, __is(IJJ("red"))));
	const CFact fact_2(Probality::mosty,  CAssertion(_book, __is(IJJ("red"))));
	
	cint->assign(fact_1);
	cint->assign(fact_2);
	const CAssertion question(_book, __is( IJJ("red")));
	LikellyResult r = cint->query(question);
	return r.value < 0;
}
bool testes_grammar()
{

	assert(teste_1a());
	assert(teste_2a());
	assert(teste_3a());
	assert(teste_4a());
	assert(teste_5a());
	assert(teste_6a());
    return true;
}

