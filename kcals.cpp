#include <iostream>
#include <fstream>
#include <string>

int main ()
{
  std::fstream input ("input.txt", std::ios::app);
  if (input.is_open())
    { 
      line = 0;
      string str;
      while (str.length() == 0 ) getline(std::cin, str);
      std::cout << "line:" << line += 1;
    }
  return 0;
}
