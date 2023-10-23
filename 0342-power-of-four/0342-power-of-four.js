/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function(n) {
    
    if (n < 4){
        return n == 1
    }
    
    return isPowerOfFour(n / 4)

};


