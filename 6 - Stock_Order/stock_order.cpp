#include <iomanip>
#include <iostream>
#include <string>
#include <list>
#include <fstream>
using namespace std;

typedef struct order
{
    string orderId;
    float price;
    int quantity;
    char orderType;

} order;

void display(list<order *> listRef)
{
    for (list<order *>::iterator iter = listRef.begin(); iter != listRef.end(); iter++)
    {
        cout << "order " + (*iter)->orderId + " " << (*iter)->price << " " << (*iter)->quantity << endl;
    }
    // for (list<order *>::iterator iter = buy.begin(); iter != buy.end(); iter++)
    // {
    //     executionFile << "order " + (*iter)->orderId + " " << (*iter)->quantity << " shares unexecuted\n";
    // }
}

int check(list<order *> &vec, order *vec2, ofstream &executionFile)
{
    typename list<order *>::iterator iter = vec.begin();

    for (iter = vec.begin(); iter != vec.end(); iter++)
    {
        // Abhi sahi nai h, price greater mai chahiye
        if (vec2->orderType == 'B' && (*iter)->price <= vec2->price && (*iter)->quantity == vec2->quantity)
        {
            // if (vec2->orderType == 'B')
            // {
            executionFile << "order " << vec2->orderId << " " << vec2->quantity << " shares purchased at price " << (*iter)->price << "\n";
            executionFile << "order " << (*iter)->orderId << " " << (*iter)->quantity << " shares sold at price " << (*iter)->price << "\n";

            cout << "\norder " << vec2->orderId << " " << vec2->quantity << " shares purchased at price " << (*iter)->price << "\n";
            cout << "order " << (*iter)->orderId << " " << (*iter)->quantity << " shares sold at price " << (*iter)->price << "\n";

            cout << "Before erase: " << endl;
            display(vec);
            vec.erase(iter);
            cout << "After erase: " << endl;
            display(vec);

            return 1;
        }
        else if (vec2->orderType == 'S' && (*iter)->price >= vec2->price && (*iter)->quantity == vec2->quantity)
        {
            executionFile << "order " << (*iter)->orderId << " " << (*iter)->quantity << " shares purchased at price " << (*iter)->price << "\n";
            executionFile << "order " << vec2->orderId << " " << vec2->quantity << " shares sold at price " << (*iter)->price << "\n";

            cout << "\norder " << (*iter)->orderId << " " << (*iter)->quantity << " shares purchased at price " << (*iter)->price << "\n";
            cout << "order " << vec2->orderId << " " << vec2->quantity << " shares sold at price " << (*iter)->price << "\n";

            cout << "Before erase: " << endl;
            display(vec);
            vec.erase(iter);
            cout << "After erase: " << endl;
            display(vec);

            return 1;
        }
    }

    return 0;
}

void insert(list<order *> &listRef, order *orderObj)
{
    typename list<order *>::iterator iter = listRef.begin();
    if (!listRef.empty())
    {
        for (iter = listRef.begin(); iter != listRef.end(); iter++)
        {
            cout << "list: " << (*(iter))->orderId << endl;

            if (orderObj->orderType == 'B' && orderObj->price > (*iter)->price)
            {
                break;
            }
            else if (orderObj->orderType == 'S' && orderObj->price < (*iter)->price)
            {
                break;
            }
        }
    }
    listRef.insert(iter, orderObj);
    cout << "INserted: " << orderObj->orderId << endl;
}

int main()
{
    cout << std::fixed << std::setprecision(2); // to print upto 2 decimal

    list<order *> buy; // Stores pointer of order datatype
    list<order *> sell;
    float prevPrice;

    ifstream orderFile;
    ofstream executionFile("execution.txt");
    executionFile << std::fixed << std::setprecision(2); // to print upto 2 decimal

    orderFile.open("orders2.txt");
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
        // cout << orderObj->orderId << orderObj->orderType << temp << temp2 << orderObj->price << orderObj->quantity << endl;

        if (orderObj->orderType == 'B')
        {
            cout<<"BUY"<<endl;
            if (!check(sell, orderObj, executionFile))
            {
                insert(buy, orderObj);
                // buy.push_back(orderObj);
            }
        }
        else
        {
            cout<<"Sell"<<endl;
            if (!check(buy, orderObj, executionFile))
            {
                insert(sell, orderObj);

                // sell.push_back(orderObj);
            }
        }
    }

    for (list<order *>::iterator iter = sell.begin(); iter != sell.end(); iter++)
    {
        executionFile << "order " + (*iter)->orderId + " " << (*iter)->quantity << " shares unexecuted\n";
    }
    for (list<order *>::iterator iter = buy.begin(); iter != buy.end(); iter++)
    {
        executionFile << "order " + (*iter)->orderId + " " << (*iter)->quantity << " shares unexecuted\n";
    }

    executionFile.close();
    orderFile.close();
    return 0;
}
