#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
using namespace std;

// Complete the sockMerchant function below.
int sockMerchant(int n, vector<int> ar)
{

    int nb_pair = 0;

    sort(ar.begin(), ar.end()); //check

    vector<int> vec_temp;
    for (int i = 0; i < n; i++)
    {   
        if ( find(vec_temp.begin(), vec_temp.end(), ar[i]) == vec_temp.end()) {
            vec_temp.push_back(ar[i]);
        }
    };
    for (int i=0; i<vec_temp.size(); i++) {
        cout<<vec_temp[i]<<" ";
    };
    cout<<endl;

    for (int i = 0; i < vec_temp.size(); i++) {
        int nb = 0;
        nb = count(ar.begin(), ar.end(), vec_temp[i]);
        nb_pair += floor(nb / 2);
    };

    return nb_pair;
}
//------------------------------main----------------------------------
int main()
{
    int n = 9;
    vector<int> vec = {10, 20, 20, 10, 10, 30, 50, 10, 20};

    int val = sockMerchant(n, vec);
    cout << "\n";
    cout << val << endl;

    return 0;
}