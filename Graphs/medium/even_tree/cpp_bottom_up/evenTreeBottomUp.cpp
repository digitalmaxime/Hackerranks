#include <iostream>
#include <vector>
#include <memory>
using namespace std;

int t_nodes = 30, t_edges = 29;
vector <int> t_from = {2, 3, 4, 5, 6, 
                        7, 8, 9, 10, 11, 
                        12, 13, 14, 15, 16, 
                        17, 18, 19, 20, 21, 
                        22, 23, 24, 25, 26, 
                        27, 28, 29, 30};
vector <int> t_to = {1, 2, 3, 2, 4,
                    4, 1, 5, 4, 4,
                    8, 2, 2, 8, 10,
                    1, 17, 18, 4, 15,
                    20, 2, 12, 21, 17,
                    5, 27, 4, 25
                    };


int evenForest(int t_nodes, int t_edges, vector<int> t_from, vector<int> t_to) {
    struct node {                           //node data structure
        int data, parent; 
        int weight = 0;
    };

    vector<node> tree(t_nodes);              // initialse graph

    for (int i=0; i<t_nodes; i++) {           // initialise node with data and parent
        if (i==0) {
            tree[i].parent = 0;
            tree[i].data = 1;
        } else 
        {
        tree[i].parent = t_to[i-1]; 
        tree[i].data = t_from[i-1];
        }
    }
    for (int i=0; i<tree.size(); i++) {         //affichage
        cout<<tree[i].data<<" parent "<<tree[i].parent<<endl;
    }
    cout<<endl;

                                                // setting weight of each node
    for (int i = t_edges; i > 0; i--) {
        int parent_idx = tree[i].parent - 1;
        while (parent_idx != -1) {
            cout<<"Bottom up, checking out node : "<<tree[parent_idx].data<<endl; 
            tree[parent_idx].weight += 1;
            parent_idx = tree[parent_idx].parent - 1;
        }
    }

    cout<<endl;

    int number_of_cuts = 0;                 //calculating number of cuts (%2)
    for (auto &node : tree) {
        cout<<"Node "<<node.data<<" has "<<node.weight<<" children"<<endl;
        if ((node.weight + 1) %2 == 0 && node.data != 1) {
            number_of_cuts ++;
        }
    }

    return number_of_cuts;
}

int main() {
    int result = evenForest(t_nodes, t_edges, t_from, t_to);
    cout<<"Final result : "<<result<<" number of cuts\n"<<endl;


    return 0;
}
