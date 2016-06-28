#pragma once

#include <string>

class INoum
{
public:
	std::string literal;
	INoum(std::string _literal): literal(_literal){}

	bool isSame(const INoum& noum) const;
};

inline bool INoum::isSame(const INoum& noum) const
{
	return this->literal == noum.literal;
}

class IVerb
{
public:
	std::string literal;
	bool negate;
	IVerb(std::string _literal) : literal(_literal)
	{
		negate = false;
	}

	bool isSame(const IVerb& verb) const;
};

inline IVerb _not(IVerb v)
{
	IVerb vn(v);
	vn.negate = !(vn.negate);
	return vn;
}

class IJJ
{
public:
	std::string literal;
	IJJ(std::string _literal) : literal(_literal) {}

	bool isSame(const IJJ& ijj) const;
};

class IVP
{
public:
	IVerb verb;
	IJJ adj;
	bool negate;
	IVP(IVerb _v , IJJ _jj) : verb(_v), adj(_jj)
	{
		negate = verb.negate;
	}

	bool isSame(const IVP& vp) const;
};

inline bool IVerb::isSame(const IVerb& verb) const
{
	return verb.literal == literal;
}

inline bool IJJ::isSame(const IJJ& ijj) const
{
	return literal == ijj.literal;
}

inline bool IVP::isSame(const IVP& vp) const
{
	return vp.verb.isSame(verb) && vp.adj.isSame(adj);
}
