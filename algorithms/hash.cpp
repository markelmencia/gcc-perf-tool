#include <stdio.h>     
#include <string.h>    
#include <assert.h>    

void rot13(char *s) {
    for (int i = 0; s[i]; i++) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            s[i] = 'A' + ((s[i] - 'A' + 13) % 26);
        } else if (s[i] >= 'a' && s[i] <= 'z') {
            s[i] = 'a' + ((s[i] - 'a' + 13) % 26);
        }
        printf("%s", *s);
    } 
}

static void test() {
    char test_01[] = "acjnwxkmaxklwm wadmaowdkmaowd awdpaodmmcwk ckwcamcm wkacmiowdoamcka wcmawidkjadmkw dakm dklwmdam dmawd akwdkwamdk dwadmawkodmawodmawkdma dwadmawpdmwpadma dawpdkwaopdmqpwdmalkmdklawd apdoawmdpaomd";
}

int main() {
    test(); 
    return 0;
}
