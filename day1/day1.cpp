#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool getFileContent(string fileName, vector<int> & intVec)
{
    fstream inputFile(fileName);
    if(inputFile.is_open())
    {
        int line;
        while(!inputFile.eof())
        {
            inputFile >> line;
            intVec.push_back(line);
        }
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
    vector<int> intVec;
    int answer, sum, line, max_entries=3;
    bool found=false;
    getFileContent("input_day1.txt", intVec);

    for (vector<int>::iterator i=intVec.begin(); i!=intVec.end(); ++i)
    {
        for (vector<int>::iterator j=intVec.begin(); j!=intVec.end(); ++j)
        {
            if(*i == *j){continue;}
            for (vector<int>::iterator k=intVec.begin(); k!=intVec.end(); ++k)
            {   
                if(*i == *k || *j == *k){continue;}
                sum = *i + *j + *k;
                if (sum==2020)
                {
                    answer = *i * *j * *k;
                    cout << *i * *j * *k <<" candidate \n";
                    // sumVec.push_back(*i * *j * *k);
                    found=true;
                    break;
                }
            }
            if (found){break;}
        }
        if (found){break;}
    }

    cout << answer <<" is the answer \n";
    
    return 0;
}