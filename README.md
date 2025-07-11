<p align="center">
  <img width="180" src="https://github.com/user-attachments/assets/8d20cf82-44ee-4b7e-98c0-248bc83e4fb1" />
</p>
<h1 align="center">DrugDomain Database</h1>

<p align="center">
  <a href="https://doi.org/10.1002/pro.5116">
    <img src="https://img.shields.io/badge/DrugDomain%20Paper-Protein%20Science-green" />
  </a>
</br>
  <a href="https://doi.org/10.1186/s13321-025-01019-y">
    <img src="https://img.shields.io/badge/Small%20molecule%20binding%20associated%20PTMs-J%20of%20Chemoinformatics-blue" />
  </a>
  </br>
  <a href="https://github.com/kirmedvedev/DrugDomain/wiki/DrugDomain-database-Tutorial">
    <img src="https://img.shields.io/badge/Tutorial-red" />
  </a>
</p>

DrugDomain database v2.0 [1,2] (https://drugdomain.cs.ucf.edu/) reports:
1. [ECOD](http://prodata.swmed.edu/ecod) [3] domains of proteins that are targets for small molecules and drugs (including all ligands available in Protein Data Bank)
2. Small molecule binding-associated post-translational modifications (PTMs)

DrugDomain database version 2.0, includes 43,023 UniProt accessioins, 174,545 PDB structures, 37,367 ligands from PDB, 7,561 DrugBank molecules

<img width="1085" alt="Screenshot 2025-06-16 at 5 32 27 PM" src="https://github.com/user-attachments/assets/69f27fd9-603d-4987-a4f4-aca0986fdd67" />
<img width="1085" alt="Screenshot 2024-12-26 at 4 39 22 PM" src="https://github.com/user-attachments/assets/a07a4f41-a121-484c-ad95-a882091fbb2a" />

## Small molecule binding-associated Post Translational Modifications (PTMs) [4]
We identified PTMs within 10 Å of all atoms of each small molecule bound to all human proteins that have been analyzed and reported through the DrugDomain database. The overall non-redundant number of identified small molecule binding-associated PTMs is 6,131. This includes 30 types of PTMs (such as Phosphorylation, Ubiquitination, etc.) and 47 combinations of PTM and amino acid types (for example Phosphorylation of SER, Acetylation of LYS, etc.)

<img width="900" alt="Fig1" src="https://github.com/user-attachments/assets/3a7b5b86-7546-4cc8-9b22-b0cc1e634229" /> <br>
<b>Distribution of small molecule binding-associated PTMs types in ECOD architecture groups.</b> <b>(A)</b> Statistics for experimental PDB structures. <b>(B)</b> Statistics for AlphaFill models. Thickness of the lines shows the number of PTMs per ECOD A-group.

## Files
<b>DrugDomain v2.0:</b></br>
https://drugdomain.cs.ucf.edu/download/DrugDomain_v2.0_data_PDBs_ECODv292.txt - domain annotations for all Protein Data Bank structures containing ligands (small molecules or metal ions)

<b>DrugDomain v1.0:</b></br>
```/DrugDomain_data_for_download/DrugDomain_v1.0_data_PDBs_ECODv291.txt``` - domain annotations for all human proteins that are targets for small molecules and drugs from DrugBank and that have experimentally determined PDB structures </br>
```/DrugDomain_data_for_download/DrugDomain_v1.0_data_AlphaFill.txt``` - domain annotations for all human proteins that are targets for small molecules and drugs from DrugBank and that DO NOT have experimentally determined PDB structures

<b>PTMs data</b></br>
```/PTMs/PTMs_per_residue_with_ligs.txt``` - list of all identified small molecule binding-associated PTMs
```/PTMs/PTMs_pdb_structures_ECOD_domains_with_ligs.txt``` - domain annotations for identified small molecule binding-associated PTMs in PDB structures </br>
```/PTMs/PTMs_alphafill_models_ECOD_domains_with_ligs.txt``` - domain annotations for identified small molecule binding-associated PTMs in AlphaFill models </br>
```/PTMs/example/*``` - files that are required for ```calculate_rmsd_pdb.py``` </br>

<b>Running calculate_rmsd_pdb.py:</b> ```/path/to/pymol/pymol -c calculate_rmsd_pdb.py``` </br>

## References
1. Medvedev KE, Schaeffer RD, Grishin NV. DrugDomain: The evolutionary context of drugs and small molecules bound to domains. _Protein Science_. 2024, 33(8):e5116. https://doi.org/10.1002/pro.5116
2. Medvedev KE, Schaeffer RD, Grishin NV. DrugDomain 2.0: comprehensive database of protein domains-ligands/drugs interactions across the whole Protein Data Bank. _bioRxiv_. 2025, 2025.07.03.663025. https://doi.org/10.1101/2025.07.03.663025
3. Schaeffer RD, Medvedev KE, Andreeva A, Chuguransky S, Lázaro-Pinto B, Zhang J, Cong Q, Bateman A, Grishin NV. ECOD: Integrating classifications of protein domains from experimental and predicted structures. _Nucleic Acids Research_. 2025, 53(D1): D411-D418. https://doi.org/10.1093/nar/gkae1029
4. Medvedev KE, Schaeffer RD, Grishin NV. Leveraging AI to Explore Structural Contexts of Post-Translational Modifications in Drug Binding. _Journal of Chemoinformatics_. 2025, 17(1): 67. https://doi.org/10.1186/s13321-025-01019-y 
