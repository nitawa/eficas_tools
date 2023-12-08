texteDebut='<?xml version="1.0" encoding="UTF-8"?>\n<schema xmlns="http://www.w3.org/2001/XMLSchema" xmlns:{}="http://chercheurs.edf.com/logiciels/{}" targetNamespace="http://chercheurs.edf.com/logiciels/{}" elementFormDefault="qualified" attributeFormDefault="qualified"\n>'
texteFin='</schema>'

# SIMP
typeSimple    = '\t<simpleType name="{}">\n\t\t<restriction base="{}"/>\n\t</simpleType>\n'
debutTypeSimpleWithInto  = '\t<simpleType name="{}">\n\t\t<restriction base="{}">\n'
typeSimpleWithInto       = '\t\t\t<enumeration value="{}"/>\n'
finTypeSimpleWithInto    = '\t\t</restriction>\n\t</simpleType>\n'
eltDsSequence = '\t\t\t<element name="{}" type="{}:{}" minOccurs="{}" maxOccurs="{}"/>\n'

# COMPO
debutTypeCompo = '\t<complexType name="{}" >\n\t\t<sequence minOccurs="{}" maxOccurs="{}">\n'
finTypeCompo   = '\t\t</sequence>\n\t</complexType>\n'
eltCompoDsSequence = '\t\t\t<element name="{}" type="{}:{}" minOccurs="{}" maxOccurs="{}"/>\n'
eltCompoDsSequenceSiProc = '\t\t\t<element name="{}" type="{}:{}" />\n'

# BLOC
debutTypeSubst = '\t<group name="{}">   \n\t\t<sequence>\n'
finTypeSubst   = '\t\t</sequence>\n\t</group>\n'
substDsSequence = '\t\t\t<group ref="{}:{}"  minOccurs="{}" maxOccurs="{}"/>\n'


# CATA
debutTypeCata = '\t<complexType name="{}">\n\t\t<choice minOccurs="0" maxOccurs="unbounded">\n'
finTypeCata   = '\t\t</choice>\n\t</complexType> '
eltCata = '\t<element name="{}" type="{}:{}"/>\n'


if __name__ == '__main__' :
    nomElt='Simple'
    nomDuType='T_Simple'
    nomDuTypeBase='int'
    nomDuComplexe='T_Complexe'
    nomDuCode='monCode'
    minOccurs=1
    maxOccurs=1

    texteSimple=typeSimple.format(nomDuType, nomDuTypeBase)
    texteElt=eltDsSequence.format(nomElt,nomDuCode,nomDuType,minOccurs,maxOccurs)

    minOccurs=0
    texteComplexe=debutTypeComplexe.format(nomDuComplexe)
    texteComplexe+=texteElt
    texteComplexe+=finTypeComplexe
    texteEltComplexe=eltDsSequence.format(nomElt,nomDuCode,nomDuType,minOccurs,maxOccurs)

    texteCata=debutTypeCata.format(nomDuCode)
    texteCata+=texteEltComplexe
    texteCata+=finTypeCata

    eltRacine=eltCata.format(nomDuCode, 'T_'+nomDuCode)
    print (texteSimple+texteComplexe+texteCata+eltRacine)
