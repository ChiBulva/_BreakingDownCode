#include <iostream>

using namespace std;

int add(int num1, int num2){
	num1 = num1+num2;
	return num1;
}

int sub(int num1, int num2){
	num1 = num1-num2;
	return num1;
}

int mul(int num1, int num2){
	num1 = num1*num2;
	return num1;
}

float div(float num1, int num2){
	num1 = num1/num2;
	return num1;
}
int main(){
	float num1 = 0;
	int num2 = 0;
	char opp;

	cout << "Enter first number!: ";
	cin >> num1;
	cout << "Enter second number!: ";
	cin >> num2;
	cout << "Enter an opporator (+,-,*,/): ";
	cin >> opp;


	switch(opp)
	{
		case '+':
			cout << "add\n";
			num1 = add(num1,num2);
			break;
 
		case '-': 
			cout << "sub\n";
			num1 = sub(num1,num2);
			break;

		case '*': 
			cout << "mul\n";
			num1 = mul(num1,num2);
			break;

		case '/': 	
			cout << "div\n";
			num1 = div(num1,num2);
			break;
	}
	cout << "Answer: " << num1 << "\n";
}
