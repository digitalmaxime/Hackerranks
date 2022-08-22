#include <iostream>
#include <vector>
#include <memory>
using namespace std;

struct node{
    int a;
    int b;
    int c = 13;
};


int main() {
    node n1;
    shared_ptr<node> sm1;
    sm1 = make_shared<node>(n1);
    auto sm2 = sm1;
    sm1->c = 69;
    sm2->c = 88;

    cout<<"node1.c : "<<n1.c<<endl;
    cout<<"sm1->c : "<<sm1->c<<endl;
    cout<<"sm2->c : "<<sm2->c<<endl;
    sm1 = nullptr;
//------------------------------------------------------------

  int firstvalue, secondvalue;
  int * mypointer;

  mypointer = &firstvalue;
  *mypointer = 10;
  mypointer = &secondvalue;
  *mypointer = 20;
  cout << "firstvalue is " << firstvalue << '\n';
  cout << "secondvalue is " << secondvalue << '\n';
  return 0;
}