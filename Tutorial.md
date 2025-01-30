# DrugDomain database Tutorial

DrugDomain database includes two types of hierarchy: protein and molecule-centric. The complete lists of proteins and small molecules can be accessed through the top menu. The protein or molecule can be searched using the search field on the main page. The search can be conducted using UniProt or DrugBank accession numbers:
<p align="center">
<img width="800" alt="1" src="https://github.com/user-attachments/assets/c2613cfd-0ed5-4d73-8404-64d680db17fe" />
</p>
Search result for the UniProt accession P07949 (http://prodata.swmed.edu/DrugDomain/proteins/data/P07949.html) is shown below. Each protein page includes UniProt accession, gene name, protein name and table of molecules and drugs that target this protein protein. The list of molecules includes links to DrugDomain data webpages, DrugBank accession, molecule name, drug action data from DrugBank, affinity data from BindingDB, InChI Key, and SMILES formula:
<p align="center">
<img width="800" alt="2" src="https://github.com/user-attachments/assets/816c2516-6fdd-4708-a859-1f360d5ed0d7" />
</p>
Search result for the DrugBank accession DB00398 (http://prodata.swmed.edu/DrugDomain/molecules/data/DB00398.html) is shown below. Each molecule page lists the DrugBank accession, molecule name, InChI Key, SMILES formula, and small molecule PDB accession followed by the list of human proteins that are targets for this molecule. The list of proteins includes links to DrugDomain data webpages, UniProt accession, drug action data from DrugBank, protein names, and affinity data from BindingDB:
<p align="center">
<img width="800" alt="3" src="https://github.com/user-attachments/assets/71b6d7e6-72ad-4086-b7db-43ba08f935c4" />
</p>
DrugDomain data webpage (for example: http://prodata.swmed.edu/DrugDomain/data/P07949_DB15822.html) contains DrugBank accession, molecule name, InChI Key, SMILES formula, small molecule PDB accession, and drug action data from DrugBank followed by the table of PDB structures and/or AF models with target particular protein. The table contains different information depending on the availability of experimentally determined 3D protein structures together with a particular DrugBank molecule. For cases with known PDB structure that includes DrugBank molecule and target protein DrugDomain data webpage's table includes PDB accession linked to RCSB, downloadable PyMOL script, an indication that this interaction between molecule and protein target was confirmed experimentally, a list of ECOD domains interacting with the molecule with links to the ECOD database, names of corresponded ECOD X-groups (possible homology level) and 2D diagrams of ligand–protein interactions (LigPlots):
<p align="center">
<img width="800" alt="4" src="https://github.com/user-attachments/assets/c99d3dd5-d30b-44b5-8ed5-eef00d3c7db2" />
</p>
The PyMOL script downloads the PDB structure from RCSB, colors ECOD domains by different colors, colors residues interacting with the molecule in magenta:
<p align="center">
<img width="800" alt="5" src="https://github.com/user-attachments/assets/f41025f3-264e-4841-b8b5-c4ca9de6468f" />
</p>
DrugDomain data webpage for cases without experimental PDB structure that includes DrugBank molecule and target protein includes AF accession, downloadable PyMOL script, an indication that this interaction between molecule and protein target was not confirmed experimentally (and was predicted), a list of ECOD domains interacting with the molecule with links to the AF-based ECOD database and names of corresponded ECOD X-groups:
<p align="center">
<img width="800" alt="6" src="https://github.com/user-attachments/assets/07313bb7-e8d5-472e-b93b-e78918df8383" />
</p>
The PyMOL script in these cases includes the AF model, colors it by ECOD domains, colors residues interacting with the molecule in magenta:
<p align="center">
<img width="800" alt="7" src="https://github.com/user-attachments/assets/ebd8cd81-1d4e-4aea-834c-f96bfe8446aa" />
</p>
