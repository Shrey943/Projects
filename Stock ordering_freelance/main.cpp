#include <iomanip> 
#include <iostream>
#include <string>
#include <list>
#include <fstream>
using namespace std;

// struct datatype to store required fields
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
    
    // Using list to reduce time complexity, as we need to insert and delete at random positions
    list<order *> *buy; 
    list<order *> *sell;

    ifstream *orderFile;
    ofstream *executionFile;

public:
    Stock_order(ifstream *orderFile, ofstream *executionFile)
    {
        // initializing our lists
        this->buy = new list<order *>;
        this->sell = new list<order *>;
        this->orderFile = orderFile;
        this->executionFile = executionFile;
    }

    // function to display all the pending orders
    void display()
    {
        // Using Manupulators to print data accordingly

        cout << "\nLast trading price: " << prevPrice << endl;
        cout << "Buy" << setw(40) << "Sell" << endl; 
        cout << setfill('-') << setw(36) << "  "<< setw(36) << "\n";
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
                cout << setw(30)
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

    // Function to insert data in desending order of their priority
    void insert(order *orderObj)
    {
        char type = orderObj->orderType;
        list<order *> listRef;

        if (type == 'B')
        {
            typename list<order *>::iterator iter = buy->begin();
         
            if (!buy->empty())
            {
                // Using iterator to find the correct position for new order, in decreasing priority
                for (iter = buy->begin(); iter != buy->end(); iter++)
                {

                    if (orderObj->price > (*iter)->price)
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
                // Using iterator to find the correct position for new order, in decreasing priority 
                for (iter = sell->begin(); iter != sell->end(); iter++)
                {
                    
                    if ( orderObj->price < (*iter)->price)
                    {
                        break;
                    }
                }
            }
            sell->insert(iter, orderObj);
            display();
        }
    }

    // Function to check if the current order matches any pending order
    int check(order *vec2)
    {
        char type = vec2->orderType;
        list<order *> vec;

        if (type == 'B')
        {
            typename list<order *>::iterator iter = sell->begin();
            
            // Checking all pending sell orders according to their priorities
            for (iter = sell->begin(); iter != sell->end(); iter++)
            {
                // Condition for execution
                if ((*iter)->price <= vec2->price && (*iter)->quantity == vec2->quantity)
                {

                    // Writting executed order in execution.txt
                    *(executionFile) << "order " << vec2->orderId << " " << vec2->quantity << " shares purchased at price " << (*iter)->price << "\n";
                    *(executionFile) << "order " << (*iter)->orderId << " " << (*iter)->quantity << " shares sold at price " << (*iter)->price << "\n";

                    cout << "\norder " << vec2->orderId << " " << vec2->quantity << " shares purchased at price " << (*iter)->price << "\n";
                    cout << "order " << (*iter)->orderId << " " << (*iter)->quantity << " shares sold at price " << (*iter)->price << "\n";

                    prevPrice = (*iter)->price;

                    // Erasing out executed order from list
                    sell->erase(iter);
                    display();

                    return 1;
                }
                
                
            }
        }
        else
        {
            typename list<order *>::iterator iter = buy->begin();
            
            // Checking pending buy orders according to their priorities
            for (iter = buy->begin(); iter != buy->end(); iter++)
            {
                // Condition for execution
                if ((*iter)->price >= vec2->price && (*iter)->quantity == vec2->quantity)
                {

                    // Writting executed order in execution.txt
                    *(executionFile) << "order " << (*iter)->orderId << " " << (*iter)->quantity << " shares purchased at price " << (*iter)->price << "\n";
                    *(executionFile) << "order " << vec2->orderId << " " << vec2->quantity << " shares sold at price " << (*iter)->price << "\n";

                    cout << "\norder " << (*iter)->orderId << " " << (*iter)->quantity << " shares purchased at price " << (*iter)->price << "\n";
                    cout << "order " << vec2->orderId << " " << vec2->quantity << " shares sold at price " << (*iter)->price << "\n";

                    prevPrice = (*iter)->price;

                    // Erasing out executed order from list
                    buy->erase(iter);
                    display();

                    return 1;
                }
            }
        }

        return 0;
    }

    // Main fucntion to read data from the file
    void driverFunction()
    {
        // Reading out last transition
        *(orderFile) >> prevPrice;

        while ((*(orderFile)).eof() == 0)
        {
            order *orderObj = new order();

            // temporary characters to store limitied and indivisible characters 
            char temp, temp2;

            // Reading a line and storing  in respective variables
            *(orderFile) >> orderObj->orderId >> orderObj->orderType >> temp >> temp2 >> orderObj->price >> orderObj->quantity;

            if (orderObj->quantity == 0)
            {
                break;
            }
           
            if (orderObj->orderType == 'B')
            {
                // inserting in buy list only if it does not matches any pending orders
                if (!check(orderObj))
                {
                    insert(orderObj);
                }
            }
            else
            {
                // inserting in sell list bnly if it does not matches any pending orders
                if (!check(orderObj))
                {
                    insert(orderObj);
                }
            }
        }

        // Writting all unmatched orders in execution file
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
    // to set float digits upto 2 decimal places in console output
    cout << std::fixed << std::setprecision(2); 
    std::cout << "Trading begains..." << std::endl ;

    ifstream orderFile;
    ofstream executionFile("execution.txt");
    orderFile.open("orders.txt");

    // to set float digits upto 2 decimal places in execution file
    executionFile << std::fixed << std::setprecision(2); 

    Stock_order stock_order_object(&orderFile, &executionFile);
    stock_order_object.driverFunction();

    // Closing opened files
    executionFile.close();
    orderFile.close();
    return 0;
}
