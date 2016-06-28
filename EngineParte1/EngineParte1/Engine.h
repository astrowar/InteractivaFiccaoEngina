#pragma once
#include "Grammar.h"
#include <vector>

enum Probality
{
	never = 0,
	sometimes = 2,
	normal = 3,
    mosty = 4,
	always = 10

};


class CAssertion
{
public :
	INoum noum;
	IVP vp;
	 
	CAssertion(INoum _n , IVP _vp): noum(_n), vp(_vp)
	{
		 
	}

	bool isSame(const CAssertion& c_assertion) const;
};


struct  LikellyResult
{
	float value; // 0, indiferente, >0 sim, <0 nao 
	LikellyResult(float v):value(v){}
};

class CFact : public CAssertion
{
public:
 
	Probality LK;
	CFact(INoum _n, IVP _vp) : CAssertion( _n ,_vp)
	{
		LK = Probality::normal;
	}
	CFact(CAssertion _cf, Probality k) : CAssertion(_cf), LK(k) {}
	 
	LikellyResult Valida(const CAssertion& c_assertion) const;
 
};


class CEngine
{
public:
	std::vector<CFact> factos;
	CEngine();
	virtual ~CEngine();
	void assign(const CFact& fact);
	LikellyResult query(const CAssertion& c_assertion);
};

