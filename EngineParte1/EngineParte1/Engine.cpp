#include "Engine.h"


LikellyResult CFact::Valida(const CAssertion& c_assertion) const
{
	//Esta fato eh sobre esta assertacao ?
	if (this->isSame(c_assertion))
	{
		if (this->LK == Probality::never) return LikellyResult(-10);
		if (this->LK == Probality::sometimes) return LikellyResult(-3);
		if (this->LK == Probality::normal) return LikellyResult(1);
		if (this->LK == Probality::mosty) return LikellyResult(3);
		if (this->LK == Probality::always) return LikellyResult(10);
		return LikellyResult(0);

	}
	return LikellyResult(0);
}

 


CEngine::CEngine()
{
}


CEngine::~CEngine()
{
}

void CEngine::assign(const CFact& fact)
{
	factos.push_back(fact);
}

LikellyResult  CEngine::query(const CAssertion& c_assertion)
{
	LikellyResult r = LikellyResult(0); //indiferent
	for(auto ifac = factos.begin(); ifac != factos.end();++ifac)
	{
		LikellyResult rt = ifac->Valida(c_assertion);
		if (ifac->vp.negate) rt.value = -rt.value;
		r.value += rt.value; 
	}

	return r;
}

bool CAssertion::isSame(const CAssertion & c_assertion) const
{
	if( noum.isSame(c_assertion.noum) )
	{
		if ( vp.isSame(c_assertion.vp))
		{
			return true;
		}
	}
	return false;

}
