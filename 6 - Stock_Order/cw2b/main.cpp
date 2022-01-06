#include <bits/stdc++.h>

using namespace std;

#define IOS ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define all(x) x.begin(), x.end()
#define pb push_back

struct order{
	string order_id;
	bool isBuy;
	bool isDivisible;
	float price;
	int quantity;
	order (){}
	order(string order_id, bool isBuy, bool isDivisble, float price, int quantity)
      : order_id(order_id), isBuy(isBuy), isDivisible(isDivisible), price(price), quantity(quantity){}
};

struct comp{ 
	bool operator()(order const& o1, order const& o2){
		if(o1.price == o2.price){
			return o1.quantity < o2.quantity;
		}
		return o1.price < o2.price;
   }
};

bool isMatching(order buy, order sell){
	if(buy.isDivisible == false && sell.isDivisible == false){
		return buy.quantity == sell.quantity && buy.price >= sell.price;
	}
	if(buy.isDivisible){
		if(!sell.isDivisible){
			return sell.quantity <= buy.quantity && buy.price >= sell.price;
		}
	}
	if(!buy.isDivisible){
		if(sell.isDivisible){
			return sell.quantity >= buy.quantity && buy.price >= sell.price;
		}
	}
	return buy.price >= sell.price;
}

vector<string> readFile(const string& filename){
    ifstream source;
    source.open(filename);
    vector<string> lines;
    string line;
    while (getline(source, line)){
        lines.pb(line);
    }
    source.close();
    return lines;
}

vector<string> splitString(string str){
	vector<string> words;
    string word = "";
    for (auto x : str) {
        if (x == ' '){
            words.pb(word);
            word = "";
        }
        else {
            word += x;
        }
    }
    words.pb(word);
    return words;
}

vector<order> processData(vector<string> data){
	cout<<"================================\n";
	cout<<"[+] Processing orders\n";
	vector<order> orders;
	for(int i = 1; i < data.size(); i++){
		vector<string> line = splitString(data[i]);
		orders.pb({line[0], line[1] == "B", line[3] == "D", stof(line[4]), stoi(line[5])});
	}
	return orders;
}

void displayOrder(string vectorName, vector<order> vals){
	cout<<"================================\n";
	cout<<"[+] Displaying " + vectorName + '\n';
	cout<<"Order_ID\tPrice\tQuantity\n";
	cout<<"--------------------------------\n";
	for(auto val : vals){
		cout<<val.order_id<<"\t\t"<<val.price<<"\t"<<val.quantity<<'\n';
	}
}

void simulateMarket(vector<string> data){
	cout<<"================================\n";
	cout<<"[+] Simulation started\n";
	float tradingPrice = stof(data[0]);
	vector<order> orders = processData(data);
	vector<order> pending;
	priority_queue<order, vector<order>, comp> Q;
	for(int i = 0; i < data.size(); i++){
		cout<<"[+] Last trading price: "<<tradingPrice<<'\n';
		vector<order> buyOrders, sellOrders;
		for(auto o : orders){
			if(o.isBuy){
				buyOrders.pb(o);
			}else{
				sellOrders.pb(o);
			}
		}
		displayOrder("Buying Orders", buyOrders);
		displayOrder("Selling Orders", sellOrders);
		vector<pair<int, order> > eligible;
		struct order curr = orders[0];
		for(int j = 1; j < orders.size(); j++){
			if(curr.isBuy){
				if(isMatching(curr, orders[j])){
					eligible.pb({j, orders[j]});
				}
			}else{
				if(isMatching(orders[j], curr)){
					eligible.pb({j, orders[j]});
				}
			}
		}
		if(eligible.size() != 0){
			orders.erase(orders.begin());
		}else{
			continue;
		}
		int thresh, index = -1, j = 0; 
		struct order buy, sell;
		bool flag = false;
		if(curr.isBuy){
			thresh = INT_MIN;
			for(auto el : eligible){
				int index = el.first;
				struct order val = el.second;
				if(val.price > thresh){
					thresh = val.price;
					index = j;
					flag = true;
				}
				j++;
			}
			if(!flag){
				orders.insert(orders.begin(), curr);
			}else{
				buy = curr;
				sell = eligible[index].second;
			}
		}else{
			thresh = INT_MAX;
			for(auto el : eligible){
				int index = el.first;
				struct order val = el.second;
				if(val.price < thresh){
					thresh = val.price;
					index = j;
					flag = true;
				}
				j++;
			}
			if(!flag){
				orders.insert(orders.begin(), curr);
			}else{
				buy = eligible[index].second;
				sell = curr;
			}
		}
		if(!flag){
			continue;
		}
		tradingPrice = buy.price;
		int val1 = buy.quantity, val2 = sell.quantity;
		buy.quantity -= min(val1, val2);
		sell.quantity -= min(val1, val2);
		if(buy.quantity != 0){
			orders.insert(orders.begin(), buy);
		}
		if(sell.quantity != 0){
			orders.insert(orders.begin(), sell);
		}
		ofstream outfile;
		outfile.open("executions.txt", ios_base::app);
		outfile << "Order " + buy.order_id + " "<<min(val1, val2)<<" shares purchased at price "<<tradingPrice<<'\n';
		outfile << "Order " + sell.order_id + " "<<min(val1, val2)<<" shares sold at price "<<tradingPrice<<'\n'; 
	}
	for(auto i : orders){
		ofstream outfile;
		outfile.open("executions.txt", ios_base::app);
		outfile << "Order " + i.order_id + " "<<i.quantity<<" shares unexecuted\n";
	}
}

int main(int argc,  char *argv[]){
	IOS
	cout<<fixed<<setprecision(2);
	string filename(argv[1]);
	vector<string> data = readFile(filename);
	simulateMarket(data);
	return 0;
}