#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char* argv[]) {
    if(argc < 2) {
        cout << "Filename Required!" << endl;
        return 0;
    }
    string file_name = argv[1];

    string line;
    ifstream file(file_name);

    int ans = 0, current = 50;
    while(getline(file, line)) {
        int direction = line[0] == 'L' ? -1 : 1;
        current = ((current + (direction * stoi(line.substr(1, line.length()-1)))) % 100 + 100) % 100;

        if(current == 0) ans++;
    }

    file.close();

    cout << ans << endl;
}