#include <iostream>
#include <string>
using namespace std;

string getCardType(const string& cardNumber){
  string answer;
  if (cardNumber.substr(0,1)=="4")
    answer = "Visa";
  else if(cardNumber.substr(0,1)=="5")
    answer = "Master Card";
  else if (cardNumber.substr(0,2)=="34" || cardNumber.substr(0,2)=="37")
    answer = "American Express";
  else 
    answer = "unknown";
  
  return answer;
}

int doubledDigitValue(int number){
  number+=number;
  int y = number % 10;
  if (number <10)
    return number;
  else{
    number = y + (number/10);
    return number;
  }
}

int charToInt(char digit){
  int number= digit - '0';
  return number;
}

int sumOfDigits(const string& cardNumber){
  int sum= 0;
  for(int i=cardNumber.length()-1;i>=0;i--){
    char x = cardNumber[i];
    int y = charToInt(x);
    if (i % 2==0 || i==0){
      y+=0;
    }
    else{
      y=doubledDigitValue(y);
    }
    sum +=y;
  }
  return sum;
}

string getInput(const string& prompt){
  cout << prompt;
  string input;
  cin >> input;
  return input;
}

bool isValid(const string& cardNumber){
  int valid = sumOfDigits(cardNumber);
  if ( valid % 10 == 0)
    return 1;
    else    
    return 0;
}

int main(){
  string cardNum = getInput("Enter card number:");
  if (isValid(cardNum))
    cout << "Valid number";
  else
    cout << "Not a valid number";
  
  string y= getCardType(cardNum);
  cout << ", " << y;
return 0;
}
