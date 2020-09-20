#include "include/json.hpp"
#include <fstream>
#include <iostream>
#include <vector>
#include <iomanip>

using json = nlohmann::json;

int main(void)
{
    // variable declarations
    json obj;
    std::vector<std::string> keys;

    // get text from 'test.json' file
    std::ifstream i("./src/test.json");
    i >> obj;
    i.close();

    // get all keywords from 'test.json'
    for (int i = 0; i < obj.size(); i++)
    {
        for (int j = 0; j < obj[i]["keywords"].size(); j++)
            keys.push_back(obj[i]["keywords"][j]);  // push keyword to vector
    }

    // sort text and erase duplicate words
    std::sort( keys.begin(), keys.end() );
    keys.erase( unique( keys.begin(), keys.end() ), keys.end() );

    // recicle 'json obj' variable
    obj.clear();

    // push all keywords to json variable
    for (int i = 0; i < keys.size(); i++)
        obj.push_back(keys[i]);

    // write text to 'keywords.json' file
    std::ofstream o("./src/keywords.json");
    o << std::setw(4) << obj << std::endl;
    o.close();

    return 0;
}