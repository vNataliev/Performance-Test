#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <vector>


using namespace std;

void swap(string& line) {
    int len = line.length();
    for (int i = 0; i < len; i++) {
        if ('A' <= line[i] && line[i] <= 'Z') {
            line[i] = line[i] + 32;
        }
        else if ('a' <= line[i] && line[i] <= 'z') {
            line[i] = line[i] - 32;
        }
    }
}



int main() {

    ifstream input_file("input_2.txt"); //"input_4.txt"
    //ofstream output_file("output_swapcase_cpp_1.txt");
    string line;
    vector<string> lines;
    auto x = chrono::high_resolution_clock::now();
    auto fun_time = x - x;
    auto y = chrono::high_resolution_clock::now();
    auto loop_time = y - y;



    if (input_file.is_open())
    {
        int N = 700;
        int i = 0;
        int j = 0;
        
        while (getline(input_file, line)) {
            lines.push_back(line);
        }

        cout << "read file" << endl;

        auto start_fun = chrono::high_resolution_clock::now();
        while (i < N)
        {
            for (string l : lines) {
                swap(l);
            }
            i++;
        }
        auto end_fun = chrono::high_resolution_clock::now();
        fun_time += (end_fun - start_fun);

        i = 0;

        auto start_loop = chrono::high_resolution_clock::now();
        while (i < N)
        {
            for (string l : lines) {
                ;
            }
            i++;
        }
        auto end_loop = chrono::high_resolution_clock::now();
        loop_time += (end_loop - start_loop);
        input_file.close();
    }

    cout << "Function time: "
        << chrono::duration_cast<chrono::seconds>(fun_time).count()
        << " s" << endl;

    cout << "Loop time: "
        << chrono::duration_cast<chrono::milliseconds>(loop_time).count()
        << " ms" << endl;

    cout << "Proper time: "
        << chrono::duration_cast<chrono::seconds>(fun_time - loop_time).count()
        << " s" << endl;

    return 0;
}