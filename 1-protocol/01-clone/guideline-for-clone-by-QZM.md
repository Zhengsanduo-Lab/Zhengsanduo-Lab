1. For transient expression in mammalian cell (293T, CHO, Expi293), use pcDNA3.1 as backbone.
2. For expression of protein in E.coli, use pET28a, pET-dual as backbone.
3. For knockout in mammalian cell, use plenti-CRISPR-V2-sgRNA system or px459 system.
4. For knockin in mammalian cell, use pLJM vector.
5. For protein expression in insect cell, use pFastBac, pFastBac-Dual as backbone.
6. To lower target gene expression, use different promoter. CMV > SFFV > SV40 > TK promoter.
7. For protein purification, use His-Tag (HHHHHH), Flag-tag (DYKDDDDK) or ProteinC-tag (EDQVDPRLIDGK). We have homemade Ni-NTA beads, M1-Flag beads and Protein C beads. M1-Flag antibody can only recognize Flag-tag fused at N-terminal of a protein. ProteinC antibody can recognize ProteinC-tag at anywhere of a protein.
8. For secretion in Expi293 cell, use IL10 signal peptide (MHSSALLCCLVLLTGVRA).
9. For Nanobody expression in E.coli periplasm, use pelB signal peptide (MKYLLPTAAAGLLLLAAQPAMA).
10. For GPCR expression, use HA-Flag tag (MKTIIALSYIFCLVFADYKDDDDK).

How to make a clone:
1. insert fragment > 100 bp, use Gibson assemble
2. insert fragment < 100 bp, but > 40 bp, use annealing
3. insert fragment <20 bp, use quickchange
4. T4 ligase is less efficient than Gibson assemble
5. gene can come from cDNA, vector or sythesized fragment.
6. KOD-plus-neo works best, if not, add 1 ul DMSO to 50 ul PCR system.
7. for insertion of many fargments, use overlap PCR (or gibson).
8. always sequencing vectors from others!
