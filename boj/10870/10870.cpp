#include <iostream>

using namespace std;

int* fiboArr = (int*)malloc(sizeof(int)*20);
	
int fibo(int n){	
	if(n<2 || fiboArr[n]!=0){
		return fiboArr[n];
	}
	return fibo(n-1)+fibo(n-2);
}
int main(){
	fiboArr[1]=1;
	int num;
	cin >> num ;
	cout << fibo(num);
	return 0;
}
