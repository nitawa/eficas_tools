texteDebut = '<?xml version="1.0" encoding="UTF-8"?>\n<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"\nxmlns="http://chercheurs.edf.com/logiciels/{}"\nxmlns:{}="http://chercheurs.edf.com/logiciels/{}"\ntargetNamespace="http://chercheurs.edf.com/logiciels/{}"\nelementFormDefault="qualified" attributeFormDefault="unqualified" version="0">\n'
texteDebutNiveau2 = '<?xml version="1.0" encoding="UTF-8"?>\n<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"\nxmlns="http://chercheurs.edf.com/logiciels/{}"\nxmlns:{}="http://chercheurs.edf.com/logiciels/{}"\nxmlns:{}="http://chercheurs.edf.com/logiciels/{}"\ntargetNamespace="http://chercheurs.edf.com/logiciels/{}"\nelementFormDefault="qualified" attributeFormDefault="unqualified" version="0">\n'
texteDebutNiveau3 = '<?xml version="1.0" encoding="UTF-8"?>\n<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"\nxmlns="http://chercheurs.edf.com/logiciels/{}"\nxmlns:{}="http://chercheurs.edf.com/logiciels/{}"\nxmlns:{}="http://chercheurs.edf.com/logiciels/{}"\nxmlns:{}="http://chercheurs.edf.com/logiciels/{}"\ntargetNamespace="http://chercheurs.edf.com/logiciels/{}"\nelementFormDefault="qualified" attributeFormDefault="unqualified" version="0">\n'
texteFin = "</xs:schema>"
#texteDebut = '<?xml version="1.0" encoding="UTF-8"?>\n<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"\nxmlns="odyssee/cocagne/{}"\nxmlns:{}="odyssee/cocagne/{}"\ntargetNamespace="odyssee/cocagne/{}"\nelementFormDefault="qualified" attributeFormDefault="unqualified" version="0">\n'


# texteAnnotation= '\t<xs:simpleType name="PNEFdico_{}">\n\t\t<xs:annotation>\n\t\t<xs:documentation>{}\n\t\t</xs:documentation>\n\t\t</xs:annotation>\n\t<xs:restriction base="xs:string"></xs:restriction>\n\t</xs:simpleType>\n'
texteAnnotation = '\t<xs:simpleType name="PNEFdico">\n\t\t<xs:annotation>\n\t\t<xs:documentation>{}\n\t\t</xs:documentation>\n\t\t</xs:annotation>\n\t<xs:restriction base="xs:string"></xs:restriction>\n\t</xs:simpleType>\n'

# SIMP
debutSimpleType = '\t<xs:simpleType name="{}">\n'
debutSimpleTypeSsNom = "\t<xs:simpleType>\n"
fermeSimpleType = "\t</xs:simpleType>\n"
debutRestrictionBase = '\t\t<xs:restriction base="{}">\n'
fermeRestrictionBase = "\t\t</xs:restriction>\n"
enumeration = '\t\t\t<xs:enumeration value="{}"/>\n'
maxInclusiveBorne = '\t\t\t<xs:maxInclusive value = "{}"/>\n'
minInclusiveBorne = '\t\t\t<xs:minInclusive value = "{}"/>\n'

typeAvecAttributUnite = '\t<xs:complexType name="{}">\n\t\t<xs:simpleContent>\n\t\t\t<xs:extension base="{}:{}_NoUnit">\n\t\t\t<xs:attribute name="unite_{}" type="xs:string"  fixed = "{}"/>\n\t\t\t </xs:extension>\n\t\t</xs:simpleContent>\n\t</xs:complexType>\n'
debutTypeSimpleListe = "\t\t<xs:restriction>\n\t\t\t<xs:simpleType>\n\t\t\t\t<xs:list>\n\t\t\t\t\t<xs:simpleType>\n"
finTypeSimpleListe = "\t\t</xs:restriction>\n\t\t\t</xs:simpleType>\n\t\t\t\t</xs:list>\n\t\t\t\t\t</xs:simpleType>\n"
fermeBalisesMileu = "\t\t\t\t\t\t</xs:restriction>\n\t\t\t\t\t</xs:simpleType>\n\t\t\t\t</xs:list>\n\t\t\t </xs:simpleType>\n"

maxLengthTypeSimple = '\t\t\t<xs:maxLength value = "{}"/>\n'
minLengthTypeSimple = '\t\t\t<xs:minLength value = "{}"/>\n'
eltDsSequence = (
    '\t\t\t<xs:element name="{}" type="{}:{}" minOccurs="{}" maxOccurs="{}"/>\n'
)
eltDsSequenceWithHelp = '\t\t\t<xs:element name="{}" type="{}:{}" minOccurs="{}" maxOccurs="{}">\n\t\t\t\t<xs:annotation>\n\t\t\t\t\t<xs:documentation>{}</xs:documentation>\n\t\t\t\t</xs:annotation>\n\t\t\t</xs:element>\n'
eltDsSequenceWithDefautAndHelp = '\t\t\t<xs:element name="{}" type="{}:{}" minOccurs="{}" maxOccurs="{}" default="{}">\n\t\t\t\t<xs:annotation>\n\t\t\t\t\t<xs:documentation>{}</xs:documentation>\n\t\t\t\t</xs:annotation>\n\t\t\t</xs:element>\n'
eltDsSequenceWithDefaut = '\t\t\t<xs:element name="{}" type="{}:{}" minOccurs="{}" maxOccurs="{}" default="{}"/>\n'
UsingASSDkeyRefDeclaration = '\n\t<xs:keyref name="{}_Name_ref_a{}" refer="{}:Key_Name_For_{}"> \n\t\t<xs:selector xpath="{}"/>\n\t\t<xs:field xpath="."/>\n\t</xs:keyref>\n'
#    <xs:key name="Key_Name_For_ElementarySurface">
#            <xs:selector xpath="./Vimmp:CDM/Vimmp:Geometric_Domain/Vimmp:Surface"/>
#            <xs:field    xpath="./Vimmp:SurfaceName"/>
#        </xs:key>

# <xs:keyref name="MyField_Ref_A_CreateMesh" refer="Test1:Key_Name_In_ReadMesh_CreateMesh">
# <xs:selector xpath="./Test1:MyField/Test1:onMesh"/>


# COMPO
debutTypeCompo = '\t<xs:complexType name="{}" >\n'
debutTypeCompoEtape = '\t <xs:complexContent>\n\t  <xs:extension base="T_step_{}">\n'
finTypeCompoEtape = "\t  </xs:extension>\n\t </xs:complexContent>\n"
debutTypeCompoSeq = "\t\t<xs:sequence>\n"
finTypeCompoSeq = "\t\t</xs:sequence>\n"
finTypeCompo = "\t</xs:complexType>\n"
eltCompoDsSequence = (
    '\t\t\t<xs:element name="{}" type="{}:{}" minOccurs="{}" maxOccurs="{}"/>\n'
)
eltCompoDsSequenceWithHelp = (
    '\t\t\t<xs:element name="{}" type="{}:{}" minOccurs="{}" maxOccurs="{}"/>\n'
)
# name="{}" type="{}:{}" minOccurs="{}" maxOccurs="{}">\n\t\t\t\t<xs:annotation>\n\t\t\t\t\t<xs:documentation>{}</xs:documentation>\n\t\t\t\t</xs:annotation>\n\t\t\t</xs:element>\n'
# eltCompoDsSequenceInExtension = '\t\t\t<xs:element name="{}" type="{}:{}"/>\n'

# ETAPE
eltEtape = '\t<xs:element name="{}" type="{}:{}" substitutionGroup="step_{}"/>\n'
eltEtapeWithHelp = '\t<xs:element name="{}" type="{}:{}" substitutionGroup="step_{}">\n\t\t\t\t<xs:annotation>\n\t\t\t\t\t<xs:documentation>{}</xs:documentation>\n\t\t\t\t</xs:annotation>\n\t\t\t</xs:element>\n'
eltEtapeSimple = (
    '\t\t\t<xs:element name="{}" type="{}:{}" minOccurs="{}" maxOccurs="{}"/>\n'
)
eltEtapeSimpleWithHelp = '\t\t\t<xs:element name="{}" type="{}:{}" minOccurs="{}" maxOccurs="{}">\n\t\t\t\t<xs:annotation>\n\t\t\t\t\t<xs:documentation>{}</xs:documentation>\n\t\t\t\t</xs:annotation>\n\t\t\t</xs:element>\n'


# BLOC
debutTypeSubst = '\t<xs:group name="{}">   \n\t\t<xs:sequence>\n'
finTypeSubst = "\t\t</xs:sequence>\n\t</xs:group>\n"
substDsSequence = '\t\t\t<xs:group ref="{}:{}"  minOccurs="{}" maxOccurs="{}">\n\t\t\t\t<xs:annotation>\n\t\t\t\t\t<xs:documentation>{}</xs:documentation>\n\t\t\t\t</xs:annotation>\n\t\t\t</xs:group>\n'
# choiceDsBloc     = '\t\t\t<xs:choice minOccurs={}>\n'
debutChoiceDsBloc = "\t\t<xs:choice>\n"
debutChoiceDsBlocAvecMin = '<xs:choice minOccurs="{}">\n'
finChoiceDsBloc = "\t\t</xs:choice>\n"
debSequenceDsBloc = "<xs:sequence>\n"
finSequenceDsBloc = "</xs:sequence>\n"
debutTypeSubstDsBlocFactorise = '\t<xs:group name="{}">\n'
finTypeSubstDsBlocFactorise = "\t</xs:group>\n"
debutUnion = "\t\t\t<xs:union>\n"
finUnion = "\t\t\t</xs:union>\n"
reconstitueUnion = '{} maxOccurs="1">\n\t\t\t\t<xs:annotation>\n\t\t\t\t\t<xs:documentation>{}</xs:documentation>\n\t\t\t\t</xs:annotation>\n\t\t\t</xs:element>\n'


# User OR ASSD
attributeNameName = '\t\t<xs:attribute name="sdName" type="xs:string"/>\n'
attributeTypeForASSD = (
    '\t\t<xs:attribute name="sdType" type="xs:string" fixed="ASSD"/>\n'
)
attributeTypeUtilisateurName = (
    '\t\t<xs:attribute name="typeUtilisateur" type="xs:string" fixed="{}"/>\n'
)
producingASSDkeyRefDeclaration = '\t<xs:key name="Key_Name_For_{}">\n\t\t<xs:selector xpath="."/>\n\t\t<xs:field xpath="{}"/>\n\t</xs:key>\n'
texteFieldUnitaire = "./{}:{}/@name |"
defBaseXSDASSD = '\t<xs:simpleType name="AccasAssd">\n\t\t<xs:restriction base="xs:string">\n\t\t</xs:restriction>\n\t</xs:simpleType>\n'
defBaseXSDUserASSD = '\t<xs:simpleType name="AccasUserAssd">\n\t\t<xs:restriction base="xs:string">\n\t\t</xs:restriction>\n\t</xs:simpleType>\n'
defBaseXSDUserASSDMultiple = '\t<xs:simpleType name="AccasUserAssdMultiple">\n\t\t<xs:restriction base="xs:string">\n\t\t</xs:restriction>\n\t</xs:simpleType>\n'

defUserASSDMultiple = '\t<xs:simpleType name="{}">\n\t\t<xs:restriction base="AccasUserAssdMultiple">\n\t\t</xs:restriction>\n\t</xs:simpleType>\n'
defUserASSD = '\t<xs:simpleType name="{}">\n\t\t<xs:restriction base="AccasUserAssd">\n\t\t</xs:restriction>\n\t</xs:simpleType>\n'

defUserASSDOrUserASSDMultiple = '\t<xs:simpleType name="{}_{}">\n\t\t<xs:restriction base="{}">\n\t\t</xs:restriction>\n\t</xs:simpleType>\n'


# CATA
# debutTypeCata      = '\t<xs:complexType name="T_{}">\n\t\t<xs:choice minOccurs="0" maxOccurs="unbounded">\n'
debutTypeCata = (
    '\t<xs:complexType name="T_{}">\n\t\t<xs:choice minOccurs="0" maxOccurs="1">\n'
)
debutTypeCataExtension = '\t<xs:complexType name="T_{}">\n'
finTypeCata = "\t\t</xs:choice>\n\t</xs:complexType>\n"
finSchema = "</xs:schema>"
# eltCataSimple      = '\t<xs:element name="{}" type="{}:{}"/>\n'
# eltCodeSpecDsCata = '\t\t\t<xs:element ref="{}_Abstract" minOccurs="0" maxOccurs="1"/>\n'
# fermeEltCata      = '\t</xs:element>\n'
includeCata = '<xs:include schemaLocation="cata_{}.xsd" />\n\n'


# EXTENSION
debutExtension = '\t\t<xs:complexContent>\n\t\t<xs:extension base="{}:T_{}_Abstract">\n\t\t<xs:choice minOccurs="0" maxOccurs="unbounded">\n'
finExtension = "\t\t</xs:choice>\n\t\t</xs:extension>\n\t\t</xs:complexContent>\n"

# TYPE ABSTRAIT
eltAbstraitCataPPal = '\t<xs:complexType name="T_step_{}" abstract="true"/>\n'
eltAbstraitCataFils = '\t<xs:complexType name="T_step_{}" abstract="true">\n\t\t<xs:complexContent>\n\t\t\t<xs:extension base="{}:T_step_{}"/>\n\t\t</xs:complexContent>\n\t</xs:complexType>\n'
eltCataPPal = '\t<xs:element name="step_{}" type="{}:T_step_{}"/>\n'
eltCataPPalWithHelp = '\t<xs:element name="step_{}" type="{}:T_step_{}"/>\n\t\t\t\t<xs:annotation>\n\t\t\t\t\t<xs:documentation>{}</xs:documentation>\n\t\t\t\t</xs:annotation>\n\t\t\t</xs:element>\n'
eltCataFils = (
    '\t<xs:element name="step_{}" type="{}:T_step_{}" substitutionGroup="step_{}"/>\n'
)
eltCataFilsWithHelp = '\t<xs:element name="step_{}" type="{}:T_step_{}" substitutionGroup="step_{}"/>\n\t\t\t\t<xs:annotation>\n\t\t\t\t\t<xs:documentation>{}</xs:documentation>\n\t\t\t\t</xs:annotation>\n\t\t\t</xs:element>\n'

eltCata = '\t<xs:element name="{}" type="{}:T_{}"/>\n\t\t<xs:complexType name="T_{}">\n\t\t  <xs:choice minOccurs="0" maxOccurs="unbounded">\n\t\t\t<xs:element ref="step_{}" minOccurs="0" maxOccurs="1"/>\n\t\t  </xs:choice>\n\t\t</xs:complexType>\n'

eltCataSimple = '\t<xs:element name="{}" type="{}:T_{}"/>\n\t\t<xs:complexType name="T_{}">\n\t\t  <xs:choice minOccurs="0" maxOccurs="unbounded">\n'
finEltCataSimple = "\t\t  </xs:choice>\n\t\t</xs:complexType>\n"

# \n\t<xs:element name="{}_Abstract" type="{}:T_{}_Abstract"/>\n'
# implementeAbstrait  = '\t<xs:element name="{}" type="{}:{}" substitutionGroup="{}:{}_Abstract"/>\n'


# TUPLE
tupleNonHomogeneSimpleType = '\t<xs:simpleType name="{}_n{}_tuple">\n\t\t<xs:restriction base="{}"/>\n\t\t</xs:simpleType>\n'
tupleNonHomogeneElt = (
    '\t\t\t<xs:element name="{}" type="{}:{}" minOccurs="{}" maxOccurs="{}"/>\n'
)
tupleDebutComplexeType = '\t<xs:complexType name="{}">\n\t\t<xs:sequence>'
tupleMilieuComplexeType = (
    '\n\t\t\t<xs:element name="n{}" type="{}_n{}_tuple" minOccurs="1" maxOccurs="1"/>'
)
tupleFinComplexeType = '\n\t\t</xs:sequence>\n\t\t<xs:attribute name="sdType" type="xs:string" fixed="Tuple"/>\n\t</xs:complexType>\n'
tupleDebutComplexeTypeMinZero = '\t<xs:complexType name="{}">\n\t\t<xs:choice>\n\t\t<xs:sequence>\n\t\t</xs:sequence>\n\t\t<xs:sequence maxOccurs={}>'
tupleFinComplexeTypeMinZero = '\n\t\t</xs:sequence>\n\t\t</xs:choice>\n\t\t<xs:attribute name="sdType" type="xs:string" fixed="Tuple"/>\n\t</xs:complexType>\n'

# MATRICE
eltMatrice = (
    '\t\t\t <xs:element name="{}" type="{}:{}" minOccurs="{}" maxOccurs="{}"/>\n'
)
matriceSimpleType = '\t<xs:simpleType name="{}_line">\n\t\t<xs:restriction>\n\t\t\t<xs:simpleType>\n\t\t\t\t<xs:list>\n\t\t\t\t\t<xs:simpleType>\n\t\t\t\t\t\t<xs:restriction  base="{}_element"/>\n\t\t\t\t\t</xs:simpleType>\n\t\t\t\t</xs:list>\n\t\t\t</xs:simpleType>\n\t\t\t<xs:minLength value="{}"/>\n\t\t\t<xs:maxLength value="{}"/>\n\t\t</xs:restriction>\n\t</xs:simpleType>\n'
matriceSimpleType += '\t<xs:group name="{}_matrix">\n\t\t<xs:sequence>\n\t\t\t<xs:element name="line" type="{}:{}_line" minOccurs="{}" maxOccurs="{}"/>\n\t\t </xs:sequence>\n\t</xs:group>\n'
matriceSimpleType += '\t<xs:complexType name="{}"> \n\t\t<xs:group ref="{}:{}_matrix" minOccurs="1" maxOccurs="1"/>\n\t\t<xs:attribute name="sdType" type="xs:string" fixed="Matrice"/>\n\t</xs:complexType>\n'

# CHAINES AVEC BLANC
debutChaineAvecBlancsInto = (
    '\t<xs:simpleType name="{}_enum">\n\t\t<xs:restriction base="xs:string">\n'
)
milieuChaineAvecBlancsInto = '\t\t\t<xs:enumeration value="{}"/>\n'
finChaineAvecBlancsInto = "\t\t</xs:restriction>\n\t\t</xs:simpleType>\n"

complexChaineAvecBlancs = '\t<xs:complexType name="{}">\n\t\t<xs:sequence maxOccurs="{}">\n\t\t\t\t<xs:element name="s__" type="{}_enum"/>\n\t\t\t</xs:sequence>\n\t</xs:complexType>\n'

typeEltChaineAvecBlancSansInto = '\t\t<xs:simpleType name="{}_enum">\n\t\t\t<xs:restriction base="xs:string">\n\t\t\t</xs:restriction>\n\t\t</xs:simpleType>'
if __name__ == "__main__":
    print("ne fait rien")
