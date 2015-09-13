#include "allegro5/allegro.h"
#include "allegro5/allegro_image.h"
#include "Object.h"

Object::Object()
{
}

Object::~Object()
{
}

void Object::UpdateAnimation()
{
    //ANIMATION================
    if (++frameCount >= frameDelay)
    {
        if (++currFrame >= maxFrame)
            currFrame = 0;
        frameCount = 0;
    }
}

void Object::Draw(ALLEGRO_BITMAP *image)
{
    al_draw_bitmap_region(image, currFrame*frameWidth, currAni*frameHeight,
            frameWidth, frameHeight, _x, _y, 0);
}

