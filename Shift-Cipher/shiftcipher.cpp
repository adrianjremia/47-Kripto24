/*
Nama    : Adrian Jeremia Kurniawan
NPM     : 140810220047
Kelas   : A
Program : Shift Cipher
*/

#include <iostream>
#include <string>
using namespace std;

// Fungsi enkripsi shift cipher
string encrypt(string text, int shift) {
    string result = "";

    for (int i = 0; i < text.length(); i++) {
        char ch = text[i];

        // Untuk kapital
        if (isupper(ch)) {
            result += char(int(ch + shift - 65) % 26 + 65);
        }
        // Untuk huruf kecil
        else if (islower(ch)) {
            result += char(int(ch + shift - 97) % 26 + 97);
        }

        else {
            result += ch;
        }
    }
    return result;
}

// Fungsi dekripsi shift cipher
string decrypt(string text, int shift) {
    return encrypt(text, 26 - shift);
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
    string text;
    int shift;
    int choice = menu();

    cin.ignore(); 
    cout << "Masukkan teks: ";
    getline(cin, text);

    cout << "Masukkan key (shift): ";
    cin >> shift;

    if (choice == 1) {
        string encryptedText = encrypt(text, shift);
        cout << "Hasil enkripsi: " << encryptedText << endl;
    }

    else if (choice == 2) {
        string decryptedText = decrypt(text, shift);
        cout << "Hasil dekripsi: " << decryptedText << endl;
    }

    else {
        cout << "Pilihan tidak valid." << endl;
    }

    return 0;
}
