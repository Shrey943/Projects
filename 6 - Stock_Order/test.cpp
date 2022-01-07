#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
using namespace std;

int main()
{
        // std::cout << 34.4232 << std::endl;
        cout << std::fixed << std::setprecision(2);
        // std::cout << 34.4232 << std::endl;
        // std::cout << float(10) << std::endl;

    // ifstream orderFile;
    // string prevPrice;
    // string prevPrice2;

    // orderFile.open("test.txt");
    // orderFile >> prevPrice;
    // cout << prevPrice;
    // int sd;
    // while (orderFile.eof() == 0)
    // {
    //     orderFile >> prevPrice >> sd >> prevPrice2;
    //     sd++;
    //     cout << prevPrice;
    //     cout << sd;
    //     cout << prevPrice2;
    // }

        float prevPrice = 143.43;

        cout << "Last trading price: " << prevPrice << endl;
        cout << "Buy" << setw(30) << "Sell";
        cout << setfill('-') << setw(50) << endl ;
        cout << "\norderId "
             << "price"
             << " "
             << "quantity";
        return 0;
}
