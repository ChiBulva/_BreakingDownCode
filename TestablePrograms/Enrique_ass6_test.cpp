#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<string>
using namespace std;
struct netflix
{
	string title;
	int stars;
	string * cast; 
	string rating; 
};
void showInfo(netflix movie1, int cnum)
{
	int x=0;
	cout<<"MOVIE: "<<movie1.title<<endl;
	cout<<"STARS: "<<movie1.stars<<endl;
	cout<<"---CAST---"<<endl;	
	while(x<cnum)
	{
		cout<<movie1.cast[x]<<endl;
		x++;
	}
	cout<<"RATING: "<<movie1.rating<<endl;
}
void getinfo()
{
		string castnum ;
		int castn=0;	
		netflix movie;
                cin.ignore(); 
		cout << "Movie title: ";
                getline(cin,movie.title);
                cout<<endl<<"number of stars: ";
                cin >> movie.stars;
                cout <<endl<<"number of cast members:";
		cin>>castn;
                movie.cast = new string[castn];
                cin.ignore(); 
		for (int y =0; y<castn ; y++)
                {
                        cout << "type in name for cast "<<y<<endl;
                        getline(cin,movie.cast[y]);
                }
                cout << " type in rating " << endl;
                getline(cin,movie.rating);
		showInfo(movie,castn);
}
int main ()
{
	string x;
	cout<<" wanna enter a movie? yes or no? "<<endl;
	cin >>x;
	while (x == "yes")
	{
		getinfo();
		cout<<" wanna enter a movie? yes,no)"<<endl;
        	cin >>x;
	}
	return 0;
}
