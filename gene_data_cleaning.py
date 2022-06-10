import csv
import pandas as pd
import numpy as np
import os


fieldnames=['CHROM','POS','ID','REF','ALT','FILTER','ALLELE','EFFECT',
            'IMPACT','GENE','GENEID','FEATURE','FEATUREID','HGVS_C','HGVC_P',
            'RANK','CDNA_POS/LEN','AA_POS/LEN','CDS_POS/LEN','DISTANCE',
            'ERRORS','LOF','NMD','ExAC_AF','1000Gp3_RA_GF','1000Gp3_RR_GF',
            '1000Gp3_HomC','1000Gp3_AA_GF','1000Gp3_AF','CLNSIG','CLNDBN',
            'CLNDSDBID','CLNDSDB','Regulome_dbSNP141','COSMIC_CNT','MutationAssessor_pred',
            'MutationTaster_pred','phastCons20way_mammalian','GERP++_RS',
            'Uniprot_id_Polyphen2','Polyphen2_HVAR_pred','Polyphen2_HDIV_pred',
            'GERP++_NR','Uniprot_aapos_Polyphen2','CADD_phred','phyloP20way_mammalian',
            'SIFT_pred','MGI_mouse_gene','Essential_gene','LoFtool_score','RVIS_percentile',
            'RVIS','ZFIN_zebrafish_phenotype_tag','GDI-Phred','Entrez_gene_id',
            'ZFIN_zebrafish_gene','Pathway(BioCarta)_short','GDI','dbSNPBuildID',
            'repeats','ACMG_GENE','ACMG_PATH','ACMG_INHRT','ACMG_MIM_GENE','AR_GENE']
directory='F:\\Genetics Data\\Split Chromosomes\\'
chromosomeNums=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','X','Y']
splitCounts=[15,14,12,11,11,10,10,9,8,8,9,9,6,6,7,6,5,6,5,3,3,7,1]
#filelist=[]
for file in os.listdir(directory):
    fileName=directory+str(file)
    print(fileName)
    chr_df = pd.read_csv(fileName, header=None, names=fieldnames, delimiter='\t', usecols=[0,1,2,3,4,6,7,8,11])
    newDir=('F:\\Genetics Data\\Split Chromosomes\\cutdown\\'+str(file))
    chr_df.to_csv(newDir)

#print(filelist)