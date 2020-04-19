#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);
#define Max 10000000
int s[4*Max];
int lazy[4*Max];

void shift(int id, int l, int r)
{
    lazy[id<<1] += lazy[id];
    lazy[id<<1|1] += lazy[id];

    s[id<<1] += lazy[id];
    s[id<<1|1] += lazy[id];

    lazy[id] = 0;
}

void update(int x, int y, int v,
    int id, int l, int r)
{
    if(x > r || l > y)
        return;
    if(x <= l && r <= y)
    {
        s[id] += v;
        lazy[id] += v;
        return;
    }

    shift(id, l, r);

    int mid = (l + r) >> 1;
    update(x, y, v, id<<1, l , mid);
    update(x, y, v, id<<1|1, mid + 1 , r);
    s[id] =  max(s[id<<1], s[id<<1|1]);

}


int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string nm_temp;
    getline(cin, nm_temp);

    vector<string> nm = split_string(nm_temp);

    int n = stoi(nm[0]);

    int m = stoi(nm[1]);

    vector<vector<int>> q(m);
    for (int i = 0; i < m; i++) {
        q[i].resize(3);

        for (int j = 0; j < 3; j++) {
            cin >> q[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        update(q[i][0], q[i][1], q[i][2],
            1, 1, n);
        for(int i = 0; i < 4*n; i++)
        {
            cout<< s[i] << ' ';
        }
    }

    //fout << s[1] << "\n";
    cout << s[1] << "\n";
    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}