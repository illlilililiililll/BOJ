#include <iostream>

int main(){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    std::string line;
    while (true){
        getline(std::cin, line);
        if (line=="")
            break;
        std::cout << line << "\n";
    }

    return 0;
}