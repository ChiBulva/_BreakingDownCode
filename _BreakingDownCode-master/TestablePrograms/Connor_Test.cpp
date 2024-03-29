#include <stdlib.h>
#include <stdio.h>
#include <fstream>
#include <cmath>
using namespace std;

struct entry{

  int index;
  char data;
  void operator=( struct entry& );
  
};

class sorter {
  
    ifstream reader;
    struct entry * scrambled;
    struct entry temp;
    int size;
  public:
    sorter(int);
    ~sorter();
  
    void init();
    void morph();
  
    void print();

};

void entry::operator=(struct entry & old){

  this->index=old.index;
  this->data=old.data;

}

sorter::sorter(int num){

  scrambled=new struct entry[num];
  size=num;

}

sorter::~sorter(){
  if(scrambled!=NULL){  delete [] scrambled;}
}

void sorter::init(){
  int i, count=0;
  reader.open("anagrams.txt");

  do{
    reader>>scrambled[i].data;
    reader>>scrambled[i].index;
    count++;
    i++;
  }while(!reader.eof());
  reader.close();
}

void sorter :: print(){
  printf("\t\t");
  for(int j=0;j<=size;j++){
    if(scrambled[j].data=='%'){
      printf(" ");
    }
    else{printf("%c", scrambled[j].data);}
  }
  printf("\n");

  for(int k=0;k<9*pow(10,6);k+=2){k--;}


  printf("------------------------------");
  printf("\n");
  return;
}

void sorter::morph(){
  int check=0, i,j,k=0;

  do{
    check=0;
    print();
    for (i=1;i<=size;i++){
      if(scrambled[i-1].index>scrambled[i].index){
        temp=scrambled[i-1];
        scrambled[i-1]=scrambled[i];
        scrambled[i]=temp;
        check=1;
      }
    }



  }while(check);


}

int main(){

class sorter mine(19);

mine.init();
mine.morph();

  return 0;
}
