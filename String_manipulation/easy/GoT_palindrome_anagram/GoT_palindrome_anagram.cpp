#include <iostream>
#include <string>
using namespace std;

int GoT(string s) {
    cout<<"Welcome to GoT"<<endl;
    char list[26]; 
    for (char lettre : s) {
        if (find(list, list+26, lettre) != list+26) {

        }
    }
    int occurence = count(s.begin(), s.end(), 'b');
    return occurence;
}

int main() {
    
    string s1 = "aaabbbb";
    string s2 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzz";

    //int res = GoT(s1);
    //cout<<"result : "<<res<<endl;

    char list[26];
    int i = 0;
    for (char lettre : s1) {
        
        if (find(list, list+26, lettre) != list+26) {
            cout<<lettre<<" lettre found"<<endl;
            
        }
        else {
            list[i] = lettre;
            i++;
        }
    }
    cout<<list<<endl;
    

    return 0;
}