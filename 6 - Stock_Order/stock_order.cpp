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

class Stock_order
{
    float prevPrice;
    list<order *> *buy;
    list<order *> *sell;
    ifstream *orderFile;
    ofstream *executionFile;

public:
    Stock_order(ifstream *orderFile, ofstream *executionFile)
    {

        this->buy = new list<order *>;
        this->sell = new list<order *>;
        this->orderFile = orderFile;
        this->executionFile = executionFile;
    }

    // ~Stock_order()
    // {
    //     this->orderFile->close();
    //     this->executionFile->close();
    // }

    void display()
    {
        cout << "\nLast trading price: " << prevPrice << endl;
        cout << "Buy" << setw(50) << "Sell" << endl;
        cout << setfill('-') << setw(75) << "\n";
        cout << setfill(' ');

        list<order *>::iterator iter1 = buy->begin();
        list<order *>::iterator iter2 = sell->begin();

        for (iter1, iter2; iter1 != buy->end() || iter2 != sell->end(); iter1++, iter2++)
        {
            if (iter1 != buy->end())
            {
                cout << (*iter1)->orderId
                     << " "
                     << (*iter1)->price
                     << " "
                     << (*iter1)->quantity;
            }
            else
            {
                cout << setw(15) << " ";
            }
            if (iter2 != sell->end())
            {
                cout << setw(40)
                     << (*iter2)->orderId
                     << " "
                     << (*iter2)->price
                     << " "
                     << (*iter2)->quantity << endl;
            }
            else
            {
                cout << endl;
            }
        }
        cout << endl;
    }

    void insert(order *orderObj)
    {
        char type = orderObj->orderType;
        list<order *> listRef;

        if (type == 'B')
        {

            typename list<order *>::iterator iter = buy->begin();
            if (!buy->empty())
            {
                for (iter = buy->begin(); iter != buy->end(); iter++)
                {
                    // cout << "list: " << (*(iter))->orderId << endl;

                    if (type == 'B' && orderObj->price > (*iter)->price)
                    {
                        break;
                    }
                    else if (type == 'S' && orderObj->price < (*iter)->price)
                    {
                        break;
                    }
                }
            }
            buy->insert(iter, orderObj);
            display();
        }
        else
        {

            typename list<order *>::iterator iter = sell->begin();
            if (!sell->empty())
            {
                for (iter = sell->begin(); iter != sell->end(); iter++)
                {
                    // cout << "list: " << (*(iter))->orderId << endl;

                    if (type == 'B' && orderObj->price > (*iter)->price)
                    {
                        break;
                    }
                    else if (type == 'S' && orderObj->price < (*iter)->price)
                    {
                        break;
                    }
                }
            }
            sell->insert(iter, orderObj);
            display();
        }
    }

    int check(order *vec2)
    {
        char type = vec2->orderType;
        list<order *> vec;

        if (type == 'B')
        {

            typename list<order *>::iterator iter = sell->begin();

            for (iter = sell->begin(); iter != sell->end(); iter++)
            {

                if (type == 'B' && (*iter)->price <= vec2->price && (*iter)->quantity == vec2->quantity)
                {

                    *(executionFile) << "order " << vec2->orderId << " " << vec2->quantity << " shares purchased at price " << (*iter)->price << "\n";
                    *(executionFile) << "order " << (*iter)->orderId << " " << (*iter)->quantity << " shares sold at price " << (*iter)->price << "\n";

                    cout << "\norder " << vec2->orderId << " " << vec2->quantity << " shares purchased at price " << (*iter)->price << "\n";
                    cout << "order " << (*iter)->orderId << " " << (*iter)->quantity << " shares sold at price " << (*iter)->price << "\n";

                    prevPrice = (*iter)->price;
                    sell->erase(iter);
                    display();

                    return 1;
                }
                else if (type == 'S' && (*iter)->price >= vec2->price && (*iter)->quantity == vec2->quantity)
                {
                    *(executionFile) << "order " << (*iter)->orderId << " " << (*iter)->quantity << " shares purchased at price " << (*iter)->price << "\n";
                    *(executionFile) << "order " << vec2->orderId << " " << vec2->quantity << " shares sold at price " << (*iter)->price << "\n";

                    cout << "\norder " << (*iter)->orderId << " " << (*iter)->quantity << " shares purchased at price " << (*iter)->price << "\n";
                    cout << "order " << vec2->orderId << " " << vec2->quantity << " shares sold at price " << (*iter)->price << "\n";

                    prevPrice = (*iter)->price;
                    sell->erase(iter);
                    display();

                    return 1;
                }
            }
        }
        else
        {

            typename list<order *>::iterator iter = buy->begin();

            for (iter = buy->begin(); iter != buy->end(); iter++)
            {

                if (type == 'B' && (*iter)->price <= vec2->price && (*iter)->quantity == vec2->quantity)
                {

                    *(executionFile) << "order " << vec2->orderId << " " << vec2->quantity << " shares purchased at price " << (*iter)->price << "\n";
                    *(executionFile) << "order " << (*iter)->orderId << " " << (*iter)->quantity << " shares sold at price " << (*iter)->price << "\n";

                    cout << "\norder " << vec2->orderId << " " << vec2->quantity << " shares purchased at price " << (*iter)->price << "\n";
                    cout << "order " << (*iter)->orderId << " " << (*iter)->quantity << " shares sold at price " << (*iter)->price << "\n";

                    prevPrice = (*iter)->price;
                    buy->erase(iter);
                    display();

                    return 1;
                }
                else if (type == 'S' && (*iter)->price >= vec2->price && (*iter)->quantity == vec2->quantity)
                {
                    *(executionFile) << "order " << (*iter)->orderId << " " << (*iter)->quantity << " shares purchased at price " << (*iter)->price << "\n";
                    *(executionFile) << "order " << vec2->orderId << " " << vec2->quantity << " shares sold at price " << (*iter)->price << "\n";

                    cout << "\norder " << (*iter)->orderId << " " << (*iter)->quantity << " shares purchased at price " << (*iter)->price << "\n";
                    cout << "order " << vec2->orderId << " " << vec2->quantity << " shares sold at price " << (*iter)->price << "\n";

                    prevPrice = (*iter)->price;
                    buy->erase(iter);
                    display();

                    return 1;
                }
            }
        }

        return 0;
    }

    void driverFunction()
    {
        // orderFile->open("orders.txt");
        // executionFile->open("execution.txt");

        *(orderFile) >> prevPrice;

        while ((*(orderFile)).eof() == 0)
        {
            order *orderObj = new order();

            char temp, temp2;

            *(orderFile) >> orderObj->orderId >> orderObj->orderType >> temp >> temp2 >> orderObj->price >> orderObj->quantity;
            if (orderObj->quantity == 0)
            {
                break;
            }
            // cout << orderObj->orderId << orderObj->orderType << temp << temp2 << orderObj->price << orderObj->quantity << endl;
            if (orderObj->orderType == 'B')
            {
                // cout << "BUY" << endl;
                if (!check(orderObj))
                {
                    insert(orderObj);
                }
            }
            else
            {
                // cout << "Sell" << endl;
                if (!check(orderObj))
                {
                    insert(orderObj);
                }
            }
            // display();
        }

        for (list<order *>::iterator iter = sell->begin(); iter != sell->end(); iter++)
        {
            (*executionFile) << "order " + (*iter)->orderId + " " << (*iter)->quantity << " shares unexecuted\n";
        }
        for (list<order *>::iterator iter = buy->begin(); iter != buy->end(); iter++)
        {
            (*executionFile) << "order " + (*iter)->orderId + " " << (*iter)->quantity << " shares unexecuted\n";
        }
    }
};

int main()
{
    cout << std::fixed << std::setprecision(2); // to print upto 2 decimal

    ifstream orderFile;
    ofstream executionFile("execution.txt");
    orderFile.open("orders.txt");

    executionFile << std::fixed << std::setprecision(2); // to print upto 2 decimal

    Stock_order stock_order_object(&orderFile, &executionFile);
    stock_order_object.driverFunction();

    executionFile.close();
    orderFile.close();
    return 0;
}
