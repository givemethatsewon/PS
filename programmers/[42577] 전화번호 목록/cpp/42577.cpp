#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>

using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool end;

    TrieNode() {
        end = false;
    }
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();
    }

    bool insert(const string& numbers) {
        TrieNode* curr = root;
        for (char number : numbers) {
            if (curr->children.find(number) == curr->children.end()) {
                curr->children[number] = new TrieNode();
            }
            if (curr->end == true) {
                return false;
            }
            curr = curr->children[number];
        }
        curr->end = true;
        return true;
    }
};


bool solution(vector<string> phone_book) {
    Trie phone_trie;  // 전화번호 Trie

    // 전화번호를 Trie에 집어넣기
    for (const string& phone_number : phone_book) {
        if (!phone_trie.insert(phone_number)) {
            return false;  // 접두어가 있다면 바로 False
        }
    }

    // 확인
    for (const string& phone_number : phone_book) {
        TrieNode* curr = phone_trie.root;
        for (char number : phone_number) {
            curr = curr->children[number];
        }
        if (!curr->children.empty()) {
            return false;  // 끝 숫자인데 아래 children이 있으면 접두어
        }
    }

    return true;  // 접두어가 없다면 True
}

