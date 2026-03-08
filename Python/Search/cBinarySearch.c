//cc -fPIC -shared -o cBinarySearch.so cBinarySearch.c

extern int binarySearch(const int searchTerm, const int* searchList, const int listSize) {
    int left = 0;
    int right = listSize - 1;
    
    while (right > left) {
        int pointer = (left + right) / 2;
        
        if (searchList[pointer] == searchTerm) {
            return pointer;
        } else if (searchList[pointer] > searchTerm) {
            right = pointer;
        } else {
            left = pointer + 1;
        }
    }
    
    return -1;
}