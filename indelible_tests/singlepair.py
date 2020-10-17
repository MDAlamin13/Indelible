import dendropy
from dendropy.calculate import treecompare

#f = open("results.txt", "a")
#file1=open("/home/ubuntu/PhD_Study/Research/Simulated_Datasets/Taxa/t200","r")
file1=open("/mnt/e/PhD_Study/FromLinux/PhD_Study/Research/Simulated_Datasets/Indelible/indelible_tests/height/h2.0/t10.mt", "r")
s1=file1.readline()
#name="RAxML_bestTree.t200BS"
#file2name="/home/ubuntu/PhD_Study/Research/Simulated_Datasets/Taxa/outputs/" + name
#file2 = open(file2name, "r")
file2=open("/mnt/e/PhD_Study/FromLinux/PhD_Study/Research/Simulated_Datasets/Indelible/indelible_tests/height/h2.0/t10.fast", "r")
s2 = file2.readline()
# establish common taxon namespace
tns = dendropy.TaxonNamespace()

# ensure all trees loaded use common namespace
try:
    tree1 = dendropy.Tree.get(
                data=s1,
                schema='newick',
                taxon_namespace=tns)
    tree2 = dendropy.Tree.get(
                data=s2,
                schema='newick',
                taxon_namespace=tns)

    ## Unweighted Robinson-Foulds distance
    rf_distance = treecompare.symmetric_difference(tree1, tree2)
    print(rf_distance)
    #f.write(name)
    #f.write("\n")
    #f.write(rf_distance.__str__())
    #f.write("\n")
except:
    print("Input model tree problem")