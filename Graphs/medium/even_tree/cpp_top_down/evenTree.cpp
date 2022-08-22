#include <iostream>
#include <vector>
#include <memory>
using namespace std;

int t_nodes = 10, t_edges = 9;
vector <int> t_from = {2, 3, 4, 5, 6, 7, 8, 9, 10};
vector <int> t_to = {1, 1, 3, 2, 1, 2, 6, 8, 8};


struct node { 
    int data, parent; 
    //vector<shared_ptr<node>> children; // apres plusieurs essais, cest pas ce que je voulais?
    vector<node*> children;
};

vector<int> find_children_index(const node& parent) {
    int parent_data = parent.data;
    vector<int> vec_index;
    for (auto it = t_to.begin(); it != t_to.end(); it++) {
        if (*it == parent_data) {
            int index = distance(t_to.begin(), it); 
            vec_index.push_back(index);
        }  
    } 
    return vec_index;
}

void find_children(node& parent, vector<node>& tree) {
    vector<int> vec_idx = find_children_index(parent);
    for (auto i : vec_idx) {
        // shared_ptr<node> ptr = make_shared<node>(tree[i+1]);
        node* ptr = &(tree[i+1]);
        parent.children.push_back(ptr);
    }
}

int recursive_call(const node& parent, int &count) {
    cout<<"recursion called on Parent : "<<parent.data<<endl;
    for (const auto& c : parent.children) {
        cout<<"checking out node : "<<c->data<<", it has "<<c->children.size()<<" immediate children"<<endl;
        count++;
        if (c->children.size() != 0){
            recursive_call(*c, count);
        }
    }
    return count;
}

int evenForest(int t_nodes, int t_edges, vector<int> t_from, vector<int> t_to) {
    vector<node> tree(t_nodes);              // initialse graph

    for (int i=0; i<t_nodes; i++) {           // initialise node with data and parent
        if (i==0) {
            tree[i].parent = -1;
            tree[i].data = 1;
        } else 
        {
        tree[i].parent = t_to[i-1]; 
        tree[i].data = t_from[i-1];
        }
    }
    for (int i=0; i<tree.size(); i++) {         //affichage
        cout<<tree[i].data<<" ";
    }
    cout<<endl;

    for (auto &node : tree) {                   // initialisation de children
        find_children(node, tree);
    }

    // for (const auto &node : tree){                 //affichage
    //     cout<<"\nParent : "<<node.data<<" has "<<node.children.size()<< " children "<<endl;
    //     for (const auto &c : node.children) {
    //         cout<<"node "<<c->data<<", has "<<c->children.size()<<" children\t";
    //     }
    // }

    int count = 0;
    int number_of_children = recursive_call(tree[5], count);
    cout<<"number of total children : "<< number_of_children << endl;

    int number_of_cuts = 0;
    for (int i =0; i < t_nodes; ++i) {
        int count = 0;
        int num_of_children = recursive_call(tree[i], count);
        if (num_of_children %2 == 0 && num_of_children != 0) {
            number_of_cuts++;
        }
    };

    return number_of_cuts;
}

/*
int main(int argc, char*argv[]) {
    int result = evenForest(t_nodes, t_edges, t_from, t_to);
    cout<<"Final answer is : "<<result<<" number of cuts possible"<<endl;
    cout<<endl;
    return 0;
}
*/