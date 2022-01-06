#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

typedef struct order
{
    string orderId;
    float price;
    int quantity;
    char orderType;

} order;

int check(vector<order *> &vec, order *vec2, ofstream &executionFile)
{
    cout << std::fixed << std::setprecision(2); // to print upto 2 decimal

    for (int i = 0; i < vec.size(); i++)
    {
        if (vec[i]->price == vec2->price && vec[i]->quantity == vec2->quantity)
        {
            if (vec2->orderType == 'B')
            {
                executionFile << "order " << vec2->orderId << " " << vec2->quantity << " shares purchased at price " << vec2->price << "\n";
                executionFile << "order " << vec[i]->orderId << " " << vec[i]->quantity << " shares sold at price " << vec[i]->price << "\n";
            }
            else
            {
                executionFile << "order " << vec[i]->orderId << " " << vec[i]->quantity << " shares purchased at price " << vec[i]->price << "\n";
                executionFile << "order " << vec2->orderId << " " << vec2->quantity << " shares sold at price " << vec2->price << "\n";
            }

            vec.erase(vec.begin() + i);

            return 1;
        }
    }

    return 0;
}

int main()
{
    vector<order *> buy; // Stores pointer of order datatype
    vector<order *> sell;
    float prevPrice;

    ifstream orderFile;
    ofstream executionFile("execution.txt");

    orderFile.open("orders.txt");
    orderFile >> prevPrice;

    while (orderFile.eof() == 0)
    {
        order *orderObj = new order();

        char temp, temp2;

        orderFile >> orderObj->orderId >> orderObj->orderType >> temp >> temp2 >> orderObj->price >> orderObj->quantity;
        if (orderObj->quantity == 0)
        {
            break;
        }
        cout << orderObj->orderId << orderObj->orderType << temp << temp2 << orderObj->price << orderObj->quantity << endl;

        if (orderObj->orderType == 'B')
        {
            
            if (!check(sell, orderObj, executionFile))
            {

                buy.push_back(orderObj);
            }
        }
        else
        {
            if (!check(buy, orderObj, executionFile))
            {

                sell.push_back(orderObj);
            }
        }
    }

    for (int i = 0; i < sell.size(); i++)
    {
        executionFile << "order " + sell[i]->orderId + " " << sell[i]->quantity << " shares unexecuted\n";
    }
    for (int i = 0; i < buy.size(); i++)
    {
        executionFile << "order " + buy[i]->orderId + " " << buy[i]->quantity << " shares unexecuted\n";
    }

    executionFile.close();
    orderFile.close();
    return 0;
}
