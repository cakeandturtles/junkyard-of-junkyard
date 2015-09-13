#include "allegro5/allegro.h"
#include "allegro5/allegro_image.h"

class Object
{
    protected:
        //members
        float _x;
        float _y;
        int _tb;
        int _bb;
        int _lb;
        int _rb;
    public:
        //method prototypes
        //gets and sets
        Object();
        ~Object();
        void UpdateAnimation();
        void Draw(ALLEGRO_BITMAP *image);
        float X(){ return _x; }
        void X(float x){ _x = x; }
        float Y(){ return _y; }
        void Y(float y){ _y = y; }
        int TB(){ return _tb; }
        int BB(){ return _bb; }
        int LB(){ return _lb; }
        int RB(){ return _rb; }

        //animation members
        int frameCount;
        int frameDelay;
        int currFrame;
        int currAni;
        int maxFrame;
        int frameWidth;
        int frameHeight;
};

