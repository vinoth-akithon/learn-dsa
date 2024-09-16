#include <stdio.h>

int main() {
    int nums[5] = {1,2};
    nums[1] = 10;
    for (int i=0; i< 5; i++) {
        if (i != 4) {
            printf("%d, ", nums[i]);
        } else {
            
            printf("%d", nums[i]);
        }
    }
}