#include "allegro5/allegro.h"
#include "allegro5/allegro_image.h"

class Solid;

class Player : public Object
{
    private:
        //members
        float _xvel;
        float _yvel;
        float _speed;
    public:
        //method prototypes
        //gets and sets
        Player();
        ~Player();
        bool Update(bool keys[], Solid solids[], int numSolids);
        bool UpdateMove(bool keys[], Solid solids[], int numSolids);
        void UpdateAnimation(bool keys[]);
        float Xvel(){ return _xvel; }
        void Xvel(float xvel){ _xvel = xvel; }
        float Yvel(){ return _yvel; }
        void Yvel(float yvel){ _yvel = yvel; }
        float Speed(){ return _speed; }
        void Speed(float speed){ _speed = speed; }
};
