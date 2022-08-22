try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3

# def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
#     if n == 1:
#         print("Move disk 1 from rod",from_rod,"to rod",to_rod)
#         return
#     TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
#     print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
#     TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
         

# n = int(input("Enter the number of disks"))
# TowerOfHanoi(n, 'A', 'C', 'B')

def TowerOfHanoi(n , from_rod, to_rod, aux_rod, string_builder):
    if n == 1:
        string_builder.append("Deplacer le disque superieur de la tour " + from_rod + " vers la tour" + to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod, string_builder)
    string_builder.append("Deplacer le disque superieur de la tour " + from_rod + " vers la tour" + to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod, string_builder)
# def TowerOfHanoi(n , from_rod, to_rod, aux_rod, string_builder):
#     if n == 1:
#         string_builder.write("Deplacer le disque superieur de la tour " + from_rod + " vers la tour" + to_rod)
#         return
#     TowerOfHanoi(n-1, from_rod, aux_rod, to_rod, string_builder)
#     string_builder.write("Deplacer le disque superieur de la tour " + from_rod + " vers la tour" + to_rod)
#     TowerOfHanoi(n-1, aux_rod, to_rod, from_rod, string_builder)
         

    
if __name__ == "__main__":
    n = int(input())
    # string_builder = ""
    string_builder = []
    TowerOfHanoi(n, 'A', 'C', 'B', string_builder)
    # string_builder = string_builder.split(",")
    for ele in string_builder:
        print(ele)
    # print(string_builder)
    # print(string_builder.read())
    
    # string_builder.close()