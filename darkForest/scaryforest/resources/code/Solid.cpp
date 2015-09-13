#include "Constants.h"
#include "Object.h"
#include "Player.h"
#include "Solid.h"

Solid::Solid(int x, int y, int width, int height)
{
    _x = x;
    _y = y;
    _lb = 0;
    _rb = width;
    _tb = 0;
    _bb = height;
}

Solid::~Solid()
{
}

