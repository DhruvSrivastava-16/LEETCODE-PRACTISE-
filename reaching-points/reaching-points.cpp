class Solution {
public:
    bool reachingPoints(int sx, int sy, int tx, int ty) 
    {
        //O(log(min(tx,ty)))
        while(sx<tx and sy<ty)
        {
            if(tx<ty)
                ty%=tx;
            else
                tx%=ty;
        }
        return sx==tx and sy<=ty and !((ty-sy)%sx) or sy==ty and sx<=tx and !((tx-sx)%sy);
    }
};