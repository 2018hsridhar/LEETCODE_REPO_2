/*
393. UTF-8 Validation
URL := https://leetcode.com/problems/utf-8-validation/
- 7 bit unicode only for 1 byte characters? others NOT unicode based?

Is data a valid UTF-8 encoding
1 or n byte character rules
    1 -> 4 byte characters
    Octet sequence basis

2 most sig bits always a 0 -> huh 
Integert input only least significant 8 bits stores data ( ignore 24 bits to the left ) 

May operate on bitsets or bits directly -> use C++
So wait ... all values in data are technically 8 bits ( 1 byte ) 
Goal : can the data stream BE a UTF-8 encoding?

Pointers problem : 2-3-4 bit validation ( test this based on MSB being a one ) 
Bitmasking basis
- continuation byte testing ( with the start of 10 ) 


*/
class Solution {
public:
    bool validUtf8(vector<int>& data) {
        bool isValidUtf8 = true;
        // https://stackoverflow.com/questions/19353686/multiple-assignment-in-one-line
        // Right->left assignment with normal expressions
        // Embedded C style
        int ptr1,ptr2,ptr3,ptr4;
        ptr1 = ptr2 = ptr3 = ptr4 = 0;
        int n = data.size();
        while(ptr1 < n) {
            ptr2 = ptr1 + 1;
            ptr3 = ptr1 + 2;
            ptr4 = ptr1 + 3;
            int val1 = data[ptr1];
            int byteType = getByteType(val1);
            switch(byteType) {
                case 1:
                    ptr1++;
                    break;
                case 2:
                    if(ptr2 < n) {
                        int val2 = data[ptr2];
                        if(passTwoBitsTest(val2)){
                            ptr1 += 2;
                         } else {
                             return false;
                         } 
                    } else {
                        return false;
                    }
                    break;
                case 3:
                    if(ptr2 < n && ptr3 < n) {
                        int val2 = data[ptr2];
                        int val3 = data[ptr3];
                        if(passTwoBitsTest(val2) && passTwoBitsTest(val3)){
                            ptr1 += 3;
                        } else {
                            return false;
                        }
                    } else {
                        return false;
                    }
                    break;
                case 4:
                    if(ptr2 < n && ptr3 < n && ptr4 < n) {
                        int val2 = data[ptr2];
                        int val3 = data[ptr3];
                        int val4 = data[ptr4];
                        if(passTwoBitsTest(val2) && passTwoBitsTest(val3) && passTwoBitsTest(val4)){
                            ptr1 += 4;
                        } else {
                            return false;
                        }

                    } else {
                        return false;
                    }
                    break;
                default:
                    // fmt.Printf("Should not be in default case.");
                    return false;
            }
        }
        return isValidUtf8;
    }

    // No narrowing allowed from int to unsigned long long
    // gaaaah
    bool passTwoBitsTest(int data){
        // Int -> ULL well defined in C standard too :-)
        unsigned long long ull = data;
        std::bitset<8> dataBits{ull};
        // std::bitset<8> twoBitsTest{"11111111"};
        // auto testRes = dataBits & twoBitsTest;
        return (dataBits.test(7) && !dataBits.test(6));
        // return (testRes == 0b10000000);
    }

    // Thank god for the bitset in stdLib
    int getByteType(int data) {
        // Binary String constructor for bitset and templation
        unsigned long long ull = data;
        std::bitset<8> dataBits{ull};
        // std::bitset<8> oneMask{"11111111"}; 
        // std::bitset<8> twoMask{"11111111"}; 
        // std::bitset<8> threeMask{"11111111"}; 
        // std::bitset<8> fourMask{"11111111"};
        // auto oneTest = dataBits & oneMask;
        // auto twoTest = dataBits & twoMask;
        // auto threeTest = dataBits & threeMask;
        // auto fourTest = dataBits & fourMask;
        // if(oneTest == 0b00000000){
        if(dataBits.test(7) == false){
            return 1;
        }
        // if(twoTest.test(7) ==  == 0b11000000){
        if(dataBits.test(7) && dataBits.test(6) && !dataBits.test(5)){
            return 2;
        }
        // if(threeTest == 0b11100000){
        if(dataBits.test(7) && dataBits.test(6) && dataBits.test(5) && !dataBits.test(4)){
            return 3;
        }
        // if(fourTest == 0b11110000){
        if(dataBits.test(7) && dataBits.test(6) && dataBits.test(5) && dataBits.test(4) && !dataBits.test(3)){
            return 4;
        }
        return 0;
    }
};
