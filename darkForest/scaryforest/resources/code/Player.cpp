#include "allegro5/allegro.h"
#include "allegro5/allegro_image.h"
#include "stdlib.h"
#include "Constants.h"
#include "Object.h"
#include "Player.h"
#include "Solid.h"

bool Collision(float lb, float tb, float rb, float bb, Object object);

Player::Player()
{
    _x = WIDTH/2;
    _y = HEIGHT/2;
    _xvel = 0;
    _yvel = 0;
    _speed = 1.5;
    _tb = 8;
    _bb = 24;
    _lb = 0;
    _rb = 16;

    //animation stuff
    frameCount=0;
    frameDelay=FPS/2;
    currFrame=0;
    currAni=0;
    maxFrame=2;
    frameWidth=16;
    frameHeight=24;
}

Player::~Player()
{
}

bool Player::Update(bool keys[], Solid solids[], int numSolids)
{
    UpdateAnimation(keys);
    return UpdateMove(keys, solids, numSolids);
}

bool Player::UpdateMove(bool keys[], Solid solids[], int numSolids)
{
    //MOVEMENT STUFF========================
    if (keys[LEFT])
        _xvel=-_speed;
    else if (keys[RIGHT])
        _xvel=_speed;
    else
        _xvel=0;

    if (keys[UP])
        _yvel=-_speed;
    else if (keys[DOWN])
        _yvel=_speed;
    else
        _yvel=0;

    //horizontal solid collisions
    for (int i=0; i<numSolids; i++)
    {
        float xspd = _x+_xvel;
        //left solid collision
        if (Collision(xspd+_lb, _y+_tb, _x+_lb, _y+_bb, solids[i]))
        {
            _xvel=0;
            while (!Collision(_x+_lb-1, _y+_tb, _x+_lb, _y+_bb, solids[i]))
                _x--;
        }
        //right solid collision
        if (Collision(_x+_rb, _y+_tb, xspd+_rb, _y+_bb, solids[i]))
        {
            _xvel=0;
            while (!Collision(_x+_rb, _y+_tb, _x+_rb+1, _y+_bb, solids[i]))
                _x++;
        }
    }
    _x+=_xvel;

    //vertical solid collisions
    for (int i=0; i<numSolids; i++)
    {
        float yspd = _y+_yvel;
        //top solid collision
        if (Collision(_x+_lb, yspd+_tb, _x+_rb, _y+_tb, solids[i]))
        {
            _yvel=0;
            while (!Collision(_x+_lb, _y+_tb-1, _x+_rb, _y+_tb, solids[i]))
                _y--;
        }
        //bottom solid collision
        if (Collision(_x+_lb, _y+_bb, _x+_rb, yspd+_bb, solids[i]))
        {
            _yvel=0;
            while(!Collision(_x+_lb, _y+_bb, _x+_rb, _y+_bb+1, solids[i]))
                _y++;
        }
    }
    _y+=_yvel;


    return true;
}

void Player::UpdateAnimation(bool keys[])
{
    if (keys[UP])
        currAni=UP;
    else if (keys[DOWN])
        currAni=DOWN;
    else if (keys[LEFT])
        currAni=LEFT;
    else if (keys[RIGHT])
        currAni=RIGHT;

    if (_xvel!=0 || _yvel!=0)
        frameDelay=FPS/4;
    else
        frameDelay=FPS/2;

    //ANIMATION================
    if (++frameCount >= frameDelay)
    {
        if (++currFrame >= maxFrame)
            currFrame = 0;
        frameCount = 0;
    }
}

