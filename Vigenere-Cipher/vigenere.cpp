#include <iostream>
#include <string>
using namespace std;

// Fungsi untuk mengubah key agar sesuai panjangnya dengan teks
string generateKey(string text, string key) {
    int x = text.size();
    
    for (int i = 0; ; i++) {
        if (key.size() == text.size())
            break;
        key.push_back(key[i % key.size()]);
    }
    return key;
}

// Fungsi enkripsi Vigenere cipher
string encrypt(string text, string key) {
    string result = "";

    for (int i = 0; i < text.length(); i++) {
        char ch = text[i];

        // Untuk kapital
        if (isupper(ch)) {
            result += char(((ch - 'A') + (key[i] - 'A')) % 26 + 'A');
        }
        // Untuk huruf kecil
        else if (islower(ch)) {
            result += char(((ch - 'a') + (key[i] - 'a')) % 26 + 'a');
        }

        else {
            result += ch;
        }
    }
    return result;
}

// Fungsi dekripsi Vigenere cipher
string decrypt(string text, string key) {
    string result = "";

    for (int i = 0; i < text.length(); i++) {
        char ch = text[i];

        // Untuk kapital
        if (isupper(ch)) {
            result += char(((ch - 'A') - (key[i] - 'A') + 26) % 26 + 'A');
        }
        // Untuk huruf kecil
        else if (islower(ch)) {
            result += char(((ch - 'a') - (key[i] - 'a') + 26) % 26 + 'a');
        }

        else {
            result += ch;
        }
    }
    return result;
}

// Fungsi menu pilihan operasi
int menu() {
    int choice;
    cout << "Pilih operasi:\n";
    cout << "1. Enkripsi\n";
    cout << "2. Dekripsi\n";
    cout << "Pilihan: ";
    cin >> choice;
    return choice;
}

int main() {
    string text, key;
    int choice = menu();

    cin.ignore();
    cout << "Masukkan teks: ";
    getline(cin, text);

    cout << "Masukkan key: ";
    getline(cin, key);

    // Buat key agar sesuai panjang dengan teks
    key = generateKey(text, key);

    if (choice == 1) {
        string encryptedText = encrypt(text, key);
        cout << "Hasil enkripsi: " << encryptedText << endl;
    }

    else if (choice == 2) {
        string decryptedText = decrypt(text, key);
        cout << "Hasil dekripsi: " << decryptedText << endl;
    }

    else {
        cout << "Pilihan tidak valid." << endl;
    }

    return 0;
}
