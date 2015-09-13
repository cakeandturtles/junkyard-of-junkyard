#include "allegro5/allegro.h"
#include "allegro5/allegro_image.h"
#include "allegro5/allegro_native_dialog.h"
#include "allegro5/allegro_primitives.h"
#include "allegro5/allegro_font.h"
#include "allegro5/allegro_ttf.h"
#include "allegro5/allegro_audio.h"
#include "allegro5/allegro_acodec.h"
#include <stdio.h>
#include <string>
#include "Constants.h"
#include "Object.h"
#include "Solid.h"
#include "Player.h"

using namespace std;

//GLOBALS===============
bool keys[5] = { false, false, false, false, false };
//ALLEGRO COMPONENTS
ALLEGRO_DISPLAY *display = NULL;
ALLEGRO_TRANSFORM trans;
ALLEGRO_EVENT_QUEUE *event_queue = NULL;
ALLEGRO_TIMER *timer = NULL;
ALLEGRO_FONT *font16 = NULL;
ALLEGRO_BITMAP *playerImage = NULL;

//prototypes
bool Initialize();
bool LoadImages();
void Destroy();

int main (void)
{
    //primitives
    bool done = false;
    bool redraw = true;
    bool isPaused = false;
    bool isGameOver = false;

    //object variables
    Player player;

    //the following will be essentially the window borders
    Solid solids[] = {
        Solid(WIDTH, 0, 16, HEIGHT),
        Solid(0, -16, WIDTH, 16),
        Solid(-16, 0, 16, HEIGHT),
        Solid(0, HEIGHT, WIDTH, 16) };
    int numSolids = sizeof(solids)/sizeof(Solid);

    if (!Initialize() || !LoadImages())
    {
        Destroy();
        return 0;
    }

    //ACTUAL GAME LOOP BEGIN!+++++++++++++++++++
    while (!done)
    {
        ALLEGRO_EVENT ev;
        al_wait_for_event(event_queue, &ev);

        if (ev.type==ALLEGRO_EVENT_TIMER)
        {
            redraw = true;

            if (!isPaused && !isGameOver)
            {
                isGameOver = !player.Update(keys, solids, numSolids);
            }
        }
        else if (ev.type==ALLEGRO_EVENT_DISPLAY_CLOSE)
        {
            done = true;
        }
        else if (ev.type==ALLEGRO_EVENT_KEY_DOWN)
        {
            switch(ev.keyboard.keycode)
            {
                case ALLEGRO_KEY_ESCAPE:
                    done = true;
                    break;
                case ALLEGRO_KEY_UP:
                    keys[UP] = true;
                    break;
                case ALLEGRO_KEY_DOWN:
                    keys[DOWN] = true;
                    break;
                case ALLEGRO_KEY_LEFT:
                    keys[LEFT] = true;
                    break;
                case ALLEGRO_KEY_RIGHT:
                    keys[RIGHT] = true;
                    break;
                case ALLEGRO_KEY_ENTER:
                    if (!isGameOver)
                        isPaused = !isPaused;
                    break;
            }
        }
        else if (ev.type==ALLEGRO_EVENT_KEY_UP)
        {
            switch(ev.keyboard.keycode)
            {
                case ALLEGRO_KEY_ESCAPE:
                    done = true;
                    break;
                case ALLEGRO_KEY_UP:
                    keys[UP] = false;
                    break;
                case ALLEGRO_KEY_DOWN:
                    keys[DOWN] = false;
                    break;
                case ALLEGRO_KEY_LEFT:
                    keys[LEFT] = false;
                    break;
                case ALLEGRO_KEY_RIGHT:
                    keys[RIGHT] = false;
                    break;
            }
        }
        if (redraw && al_is_event_queue_empty(event_queue)){
            redraw = false;

            //clear the buffer screen
            al_clear_to_color(al_map_rgb(0,0,0));

            //Draw everything
            player.Draw(playerImage);
            if (isPaused)
            {
                al_clear_to_color(al_map_rgb(0,0,0));
                al_draw_textf(font16, al_map_rgb(255,255,255),80, HEIGHT/2-4, 0,
                        "GAME PAUSED");
                al_draw_textf(font16, al_map_rgb(255,255,255),8, HEIGHT-32,
                        0, "PRESS ENTER TO CONTINUE");
            }
            else if (isGameOver)
            {
                al_clear_to_color(al_map_rgb(0,0,0));
                al_draw_textf(font16, al_map_rgb(255,255,255),80, HEIGHT/2-4, 0,
                        "GAME OVER");
                al_draw_textf(font16, al_map_rgb(255,255,255),14, HEIGHT-32,
                        0, "PRESS ENTER TO RESTART");
            }

            //update display
            al_flip_display();
        }
    }

    Destroy();
    return 0;
}

//LOADING AND INITIALIZING FUNCTIONS
bool Initialize()
{
    //Initialize allegro
    if (!al_init()){
        al_show_native_message_box(display, "Error", "Error",
                "Failed to initialize allegro!", NULL,
                ALLEGRO_MESSAGEBOX_ERROR);
        return false;
    }

    //allows images to be properly loaded
    if (!al_init_image_addon()){
        al_show_native_message_box(display, "Error", "Error",
                "Failed to initialize image addon!", NULL,
                ALLEGRO_MESSAGEBOX_ERROR);
        return false;
    }

    if (!al_install_audio()){
        al_show_native_message_box(display, "Error", "Error",
                "Failed to initialize audio!", NULL,
                ALLEGRO_MESSAGEBOX_ERROR);
        return false;
    }

    if (!al_init_acodec_addon()){
        al_show_native_message_box(display, "Error", "Error",
                "Failed to initialize audio codecs!", NULL,
                ALLEGRO_MESSAGEBOX_ERROR);
        return false;
    }

    timer = al_create_timer(1.0 / FPS);
    if (!timer){
        al_show_native_message_box(display, "Error", "Error",
                "Failed to create timer!", NULL,
                ALLEGRO_MESSAGEBOX_ERROR);
        return false;
    }

    display = al_create_display(WIDTH*2, HEIGHT*2);
    if (!display){
        al_show_native_message_box(display, "Error", "Error",
                "Failed to create display!", NULL,
                ALLEGRO_MESSAGEBOX_ERROR);
        return false;
    }
    //scale the display
    al_identity_transform(&trans);
    al_scale_transform(&trans, 2, 2);
    al_use_transform(&trans);

    event_queue = al_create_event_queue();
    if (!event_queue){
        al_show_native_message_box(display, "Error", "Error",
                "Failed to create event queue!", NULL,
                ALLEGRO_MESSAGEBOX_ERROR);
        return false;
    }

    if (!al_init_primitives_addon()){
        al_show_native_message_box(display, "Error", "Error",
                "Failed to initialize primitives!", NULL,
                ALLEGRO_MESSAGEBOX_ERROR);
        return false;
    }

    if (!al_install_keyboard()){
        al_show_native_message_box(display, "Error", "Error",
                "Failed to install keyboard!", NULL,
                ALLEGRO_MESSAGEBOX_ERROR);
        return false;
    }

    al_init_font_addon();
    al_init_ttf_addon();
    font16 = al_load_font("resources/04B_03.ttf", 24, 0);
    if (!font16){
        al_show_native_message_box(display, "Error", "Error",
                "Failed to load '04B_03.ttf'!", NULL,
                ALLEGRO_MESSAGEBOX_ERROR);
        return false;
    }


    al_register_event_source(event_queue, al_get_keyboard_event_source());
    al_register_event_source(event_queue, al_get_timer_event_source(timer));
    al_register_event_source(event_queue, al_get_display_event_source(display));
    srand(time(NULL));

    //DONT FORGET TO START THE TIMER!!!
    al_start_timer(timer);
    return true;
}

void Destroy()
{
    //make sure you destroy all the bitmaps you created
    //in the initialization function
    //bro.
    al_destroy_bitmap(playerImage);

    al_destroy_event_queue(event_queue);
    al_destroy_timer(timer);
    al_destroy_font(font16);
    al_destroy_display(display);
}

bool LoadImages()
{
    string fileName;
    string errorMessage;

    fileName="resources/images/playerSheet.png";
    errorMessage="Failed to load '"+fileName+"'!";
    playerImage = al_load_bitmap(fileName.c_str());
    if (!playerImage){
        al_show_native_message_box(display, "Error", "Error",
                errorMessage.c_str(), NULL, ALLEGRO_MESSAGEBOX_ERROR);
        return false;
    }

    //set sprite transparencies
    al_convert_mask_to_alpha(playerImage, al_map_rgb(255, 0, 255));

    return true;
}
