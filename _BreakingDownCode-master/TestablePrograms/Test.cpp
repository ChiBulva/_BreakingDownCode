#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

int humanTurn(int &Humantotalscore);
int computerTurn(int &Computertotalscore);
int roll ();
int turn = 0;
int d = 0;

int main()
{
	srand(time(NULL));
	int Humantotalscore = 0;
	int Computertotalscore = 0;

	while ((humanTurn(Humantotalscore) < 100) && (computerTurn(Computertotalscore) <100))
	{
	if ((humanTurn(Humantotalscore) >= 100) && (computerTurn(Computertotalscore) <100))
	{
			cout << "congradulations you win!" << endl;
			cout << "       =D\n";
	}

	else if ((Computertotalscore >= 100) && (Humantotalscore < 100))
	{
			cout << "sorry, you have lost" <<endl;
			cout << "       =(\n";
	}
	}
	return 0;
}

int humanTurn(int& Humantotalscore)
{
	int Humanscorethisturn = 0;
	int Scoreperroll = 0;
	char choice = 'r';
	char roll = 'r';

	Humanscorethisturn = 0;

	while ((Scoreperroll != 1) && (choice == 'r') && (Humantotalscore <100))
	{
		Scoreperroll = (rand() %6 +1);

		if(Humanscorethisturn == 0)
		{
		cout << "please press r to roll: ";
		cin >> roll;
		}

		if (Scoreperroll >= 2)
		{
			if (Humanscorethisturn ==0)
			{
			Humanscorethisturn = 0;
			}

			else if (Humanscorethisturn != 0)
			{
				Humanscorethisturn = Humanscorethisturn;
			}

			Humanscorethisturn =  Scoreperroll + Humanscorethisturn;
			cout << "You have rolled a " << Scoreperroll <<"\n" << "Your score this turn is: " << Humanscorethisturn << "\n" << " Please press r to roll again or h to hold: ";
			cin >> choice;
		}
		
		else
		{
			Humanscorethisturn = 0;
			cout << "You have rolled a 1, End of turn\n" ;
		}		
	}
	Humantotalscore = Humantotalscore + Humanscorethisturn;
	cout << "Your totall score is: " << Humantotalscore << "\n";
	return (Humantotalscore);
}

int computerTurn(int& Computertotalscore)
{
	int Computersscorethisturn = 0;
	int Scoreperroll = 0;
	char choice = 'r';

	Computersscorethisturn = 0;

	while ((Computertotalscore < 100) && (choice == 'r') && (Scoreperroll != 1) && (Computersscorethisturn < 20))
	{

		Scoreperroll = (rand() %6 +1);
		if (Scoreperroll >= 2)
		{
			if (Computersscorethisturn == 0)
			{
				Computersscorethisturn = 0;
			}

			else if (Computersscorethisturn != 0)
			{
				Computersscorethisturn = Computersscorethisturn;
			}
			Computersscorethisturn = Computersscorethisturn + Scoreperroll;
			cout << "the computer has rolled a: " << Scoreperroll << "\n" << "the computer's score this turn is: " << Computersscorethisturn << "\n";
		}

		else if (Scoreperroll == 1)
		{
			Computersscorethisturn = 0;
			cout << "The computer has rolled a 1, End of turn\n";
		}
	}
	Computertotalscore = Computertotalscore + Computersscorethisturn;
	cout << "The computer's total score is: " << Computertotalscore <<"\n";
	return (Computertotalscore);
}
