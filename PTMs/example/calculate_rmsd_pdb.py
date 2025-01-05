
import pymol2
from collections import OrderedDict

ptms = []
res = []
ccd_ptm = []
file2 = open('/../info_table_for_af3.txt')
for line2 in file2:
    st1 = line2.split("\t")
    ptms.append(st1[0])
    res.append(st1[1])
    ccd_ptm.append(st1[6].replace("\n",""))
file2.close()

up = []
dr = []
lig = []
aa = []
num = []
ptm = []
check = []
file1 = open(
    '/../list_of_af3_ptms_for_model.txt')
for line1 in file1:
    st2 = line1.split("\t")
    up.append(st2[0])
    dr.append(st2[1])
    lig.append(st2[2])
    aa.append(st2[3])
    num.append(st2[4])
    ptm.append(st2[5].replace("-","_"))
    check.append(st2[6].replace("\n",""))
file1.close()

up2 = []
db = []
pdb = []
pdb_lig = []
chain = []
int_ptm = []
file3 = open(
    '/../full_dbptm_identified_PTMs.txt')
for line3 in file3:
    st3 = line3.split("\t")
    up2.append(st3[0])
    db.append(st3[1])
    pdb.append(st3[2])
    pdb_lig.append(st3[3])
    chain.append(st3[5])
    int_ptm.append(st3[7])
file3.close()

fp1 = open('/output_folder/rmsd_af3_pdb.txt', 'w')

for i in range(len(up)):
    if check[i] == "pdb":
        for j in range(len(ptms)):
            if ptms[j] == ptm[i] and res[j] == aa[i]:
                name = up[i]+"_"+lig[i]+"_"+aa[i]+"_"+num[i]+"_"+ptm[i]+"_"+ccd_ptm[j]
                name2 = name.lower()
                for k in range(len(up2)):
                    st4 = pdb_lig[k].split("_")
                    if up2[k] == up[i] and db[k] == dr[i] and st4[1] == lig[i]:
                        st5 = list(filter(None, int_ptm[k].split(";")))
                        ch = ""

                        st6 = list(filter(None, chain[k].split(";")))
                        ch_of_up = []
                        upid_in_ch = []
                        for st in st6:
                            st7 = st.split("_")
                            ch_of_up.append(st7[0])
                            upid_in_ch.append(st7[1])
                        upid_in_ch = list(OrderedDict.fromkeys(upid_in_ch))
                        for st in st5:
                            if aa[i]+"_"+num[i]+"_"+ptm[i] in st:
                                ch_temp = st[0:1]
                                if st4[0] in ch_of_up:
                                    if len(upid_in_ch) == 1 and ch_temp == st4[0]:
                                        ch = ch_temp
                                    elif len(upid_in_ch) == 1 and ch_temp != st4[0]:
                                        continue
                                    else:
                                        ch = ch_temp
                                else:
                                    ch = ch_temp

                                p = {}
                                for m in range (0,5):
                                    p[m+1] = pymol2.PyMOL()
                                    p[m+1].start()
                                    p[m+1].cmd.load('/path/to/cif/files'+pdb[k]+'.cif')
                                    p[m+1].cmd.select('chain '+ch)
                                    p[m+1].cmd.create('chain_to_align', 'sele')
                                    p[m+1].cmd.select("sele", "resn "+lig[i]+" and chain "+st4[0])
                                    p[m+1].cmd.create('lig_str', 'sele')
                                    
                                    p[m+1].cmd.load('/path/to/af3_output/fold_'+name2+'/fold_'+name2+'_model_'+str(m)+'.cif',' '+name2+'_model_'+str(m))
                                    p[m+1].cmd.align(name2+'_model_'+str(m), 'chain_to_align')
                                    p[m+1].cmd.select("sele", "resn "+lig[i]+" in "+name2+'_model_'+str(m))
                                    p[m+1].cmd.create('lig_model', 'sele')
                                    p[m+1].cmd.align("lig_model", "lig_str", cycles=0, transform=0, object="aln")
                                    rmsd = p[m+1].cmd.rms_cur("lig_model & aln", "lig_str & aln", matchmaker=-1)
                                    filename = up[i]+"_"+lig[i]+"_"+aa[i]+"_"+num[i]+"_"+ptm[i]+'_model_'+str(m)+"_vs_"+pdb[k]+"_"+pdb_lig[k]
                                    if rmsd <= 5.0:
                                        fp1.write(name2+'_model_'+str(m)+"\t"+pdb[k]+"\t"+pdb_lig[k]+"\t"+str(rmsd)+"\n")
                                        p[m+1].cmd.save("/output/"+filename+".pse")
                                    else:
                                        p[m+1].cmd.delete("lig_model")
                                        p[m+1].cmd.delete("aln")
                                        p[m+1].cmd.select("sele", "resn "+lig[i]+" in "+name2+'_model_'+str(m))
                                        p[m+1].cmd.select("nearby_residues", f"(byres (br. sele around 10)) and "+name2+'_model_'+str(m))
                                        p[m+1].cmd.align('nearby_residues', 'chain_to_align')
                                        p[m+1].cmd.select("sele", "resn "+lig[i]+" in "+name2+'_model_'+str(m))
                                        p[m+1].cmd.create('lig_model_new', 'sele')
                                        p[m+1].cmd.align("lig_model_new", "lig_str", cycles=0, transform=0, object="aln2")
                                        rmsd2 = p[m+1].cmd.rms_cur("lig_model_new & aln2", "lig_str & aln2", matchmaker=-1)
                                        if rmsd2 < rmsd and rmsd2 <= 5.0:
                                            fp1.write(name2+'_model_'+str(m)+"\t"+pdb[k]+"\t"+pdb_lig[k]+"\t"+str(rmsd2)+"\n")
                                            p[m+1].cmd.save("/output/"+filename+".pse")
                                        else:
                                            sel = p[m+1].cmd.select("nearby_lig", f"(byres (resn {lig[i]} within 7 of (lig_model_new))) and resn {lig[i]} and {pdb[k]}")
                                            if sel == 0:
                                                min_rmsd = min(rmsd, rmsd2)
                                                fp1.write(name2+'_model_'+str(m)+"\t"+pdb[k]+"\t"+pdb_lig[k]+"\t"+str(min_rmsd)+"\t"+"check"+"\n")
                                            else:
                                                p[m+1].cmd.align("lig_model_new", "nearby_lig", cycles=0, transform=0, object="aln3")
                                                rmsd3 = p[m+1].cmd.rms_cur("lig_model_new & aln3", "nearby_lig & aln3", matchmaker=-1)
                                                min_rmsd = min(rmsd, rmsd2, rmsd3)
                                                fp1.write(name2+'_model_'+str(m)+"\t"+pdb[k]+"\t"+pdb_lig[k]+"\t"+str(min_rmsd)+"\n")
                                            p[m+1].cmd.save("/output/"+filename+".pse")
                                    p[m+1].stop()


