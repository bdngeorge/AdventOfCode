#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include "../shared.h"

using namespace std;
using namespace Shared;

// (curr + (t * new)) % 100 
//  where t = L ? -1 : 1
int main(int argc, char* argv[]) {
    if(argc < 2) {
        cout << "Filename Required!" << endl;
        return 0;
    }
    string file_name = argv[1];

    string line;
    ifstream file(file_name);

    int ans = 0, curr = 50;
    while(getline(file, line)) {
        int dir = line[0] == 'L' ? -1 : 1;
        int total_clicks = stoi(line.substr(1, line.length()-1));

        int full_rots = total_clicks / 100;
        int clicks = mod(total_clicks, 100);
        
        int dest = curr + (dir * clicks);
        if(curr != 0 && (dest < 0 || dest > 100))
            ans++;

        curr = mod(dest, 100);
        if(curr == 0) ans++;
        ans += full_rots;
    }

    file.close();

    cout << ans << endl;
}