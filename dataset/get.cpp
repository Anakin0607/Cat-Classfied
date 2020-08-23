#include<windows.h>
#include<iostream>

using namespace std;

int main(){
    cout<<"Starting......"<<endl;

    system("python getdata.py -s Persian_cat -o Persian --limit 10000");
    system("python getdata.py -s Birman_cat -o Birman --limit 10000");
    system("python getdata.py -s Norwegian_Forest_Cat -o forest --limit 10000");
    system("python getdata.py -s Ragdoll_cat -o Ragdoll --limit 10000");
    system("python getdata.py -s Himalayan_cat -o Himalayan --limit 10000");
    system("python getdata.py -s Scottish_fold_cat -o Scottish --limit 10000");
    system("python getdata.py -s Dragen-Li_cat -o dragan --limit 10000");

    return 0;
}