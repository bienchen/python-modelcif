"""Chemical descriptors of commonly-used cross-linkers

   See also :class:`ihm.ChemDescriptor`.
"""

import ihm

#: DSS cross-linker that links primary amines to primary amines
dss = ihm.ChemDescriptor('DSS', chemical_name='disuccinimidyl suberate',
              smiles='C1CC(=O)N(C1=O)OC(=O)CCCCCCC(=O)ON2C(=O)CCC2=O',
              inchi='1S/C16H20N2O8/c19-11-7-8-12(20)17(11)25-15(23)5-'
                    '3-1-2-4-6-16(24)26-18-13(21)9-10-14(18)22/h1-10H2',
              inchi_key='ZWIBGKZDAWNIFC-UHFFFAOYSA-N')

#: EDC cross-linker that links carboxyls groups and primary amines
edc = ihm.ChemDescriptor('EDC',
              chemical_name='1-ethyl-3-(3-dimethylaminopropyl)carbodiimide',
              smiles='CCN=C=NCCCN(C)C',
              inchi='1S/C8H17N3/c1-4-9-8-10-6-5-7-11(2)3/h4-7H2,1-3H3',
              inchi_key='LMDZBCPBFSXMTL-UHFFFAOYSA-N')