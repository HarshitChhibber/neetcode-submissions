class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        const string = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
        let a = 0;
        let b = string.length - 1;
        
        while (a < b){
            if (string[a] !== string[b]){
                return false;
            }
            a++;
            b--;
        }
        return true;
    }
}
