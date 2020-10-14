import dendropy
from dendropy.calculate import treecompare

result_fast = open("fast_result.txt", "a")
result_raxml = open("raxml_result.txt", "a")
for folder in range(100,801,100):
    dir_name="T"+str(folder)+"/"
    
    result_fast.write(dir_name)
    result_fast.write("\n\n")
    result_raxml.write(dir_name)
    result_raxml.write("\n\n")
    
    dir_path="/mnt/e/PhD Study/FromLinux/PhD_Study/Research/Simulated_Datasets/second/HPCC/simulation/taxa/"+dir_name


    for file in range(1, 11, 1):
        model="t"+str(file)+".mt"
        fast="t"+str(file)+".fast"
        raxml="RAxML_result.t"+str(file)+".rml"
        
        m_path=dir_path+model
        f_path=dir_path+fast
        r_path=dir_path+raxml
        
        file_model=open(m_path,"r")
        file_fast=open(f_path,"r")
        file_raxml=open(r_path,"r")
        
        s1=file_model.readline()
        s2=file_fast.readline()
        s3=file_raxml.readline()
        
        
        # establish common taxon namespace
        tns = dendropy.TaxonNamespace()

        # ensure all trees loaded use common namespace
        tree1 = dendropy.Tree.get(
                data=s1,
                schema='newick',
                taxon_namespace=tns)
        tree2 = dendropy.Tree.get(
                data=s2,
                schema='newick',
                taxon_namespace=tns)
        tree3 = dendropy.Tree.get(
                data=s3,
                schema='newick',
                taxon_namespace=tns)        

        ## Unweighted Robinson-Foulds distance
        rf_fast = treecompare.symmetric_difference(tree1, tree2)
        rf_raxml= treecompare.symmetric_difference(tree1, tree3)
        #print(rf_distance)
        result_fast.write(str(rf_fast))
        result_fast.write("\n")
        result_raxml.write(str(rf_raxml))
        result_raxml.write("\n")
    
    result_fast.write("\n\n")
    result_raxml.write("\n\n")
    
   

