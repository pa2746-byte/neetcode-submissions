class Solution {
public:

    double helper(double x, int n){
        if (n==0){
            return 1;
        }

        double res = helper( x*x, n/2 );

        if (n%2==0){
            return res;
        }
        else{
            return x*res;
        }
    }
    double myPow(double x, int n) {
        if (n==0){
            return 1;
        }
        if(x==0){
            return 0;
        }

        double res = helper(x,abs(n));

        if (n>0)
        {
            return res;
        }
        else
        {
            return 1/res;
        }
    }   

};
