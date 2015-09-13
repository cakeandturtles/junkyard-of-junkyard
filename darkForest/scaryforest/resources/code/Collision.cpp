#include "Object.h"

bool Collision(float lb, float tb, float rb, float bb, Object object)
{
    if (lb <= object.X() + object.RB() && rb >= object.X() + object.LB() &&
            tb <= object.Y() + object.BB() && bb >= object.Y() + object.TB())
        return true;
    return false;
}

