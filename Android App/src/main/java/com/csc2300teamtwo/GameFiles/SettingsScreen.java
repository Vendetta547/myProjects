package com.csc2300teamtwo.GameFiles;

import android.graphics.Color;
import android.graphics.Paint;

import com.csc2300teamtwo.framework.Game;
import com.csc2300teamtwo.framework.Graphics;
import com.csc2300teamtwo.framework.Input;
import com.csc2300teamtwo.framework.Screen;

import java.util.List;


public class SettingsScreen extends Screen {


    Paint paint;



    public SettingsScreen(Game game) {
        super(game);



        paint = new Paint();
        paint.setTextSize(50);                      // paint object for drawing strings
        paint.setTextAlign(Paint.Align.CENTER);
        paint.setAntiAlias(true);
        paint.setColor(Color.BLUE);
    }

    @Override
    public void update(float deltaTime) {
        Graphics g = game.getGraphics();
        List<Input.TouchEvent> touchEvents = game.getInput().getTouchEvents();

        int len = touchEvents.size();       //handles touch events
        for (int i = 0; i < len; i++) {
            Input.TouchEvent event = touchEvents.get(i);
            if (event.type == Input.TouchEvent.TOUCH_DOWN) {    // boundaries for the back button
                if (inBounds(event, 0, 0, 80, 50)) {
                    game.setScreen(new MainMenuScreen(game));
                    return;
                }
            }

            else if (inBounds(event, 170, 110, 80, 50)) {   // boundaries for the easy checkbox
                Settings.setEasy(flipSwitch(Settings.isEasy()));
                if (Settings.isMedium() || Settings.isHard()) { // if condition checks to see if any other difficulties are selected.
                    Settings.setMedium(false);                  // if they are, it unchecks them.
                    Settings.setHard(false);                    // the next two inBounds checks work similarly.
                }
            }

            else if (inBounds(event, 170, 190, 80, 50)) {
                Settings.setMedium(flipSwitch(Settings.isMedium()));
                if (Settings.isEasy() || Settings.isHard()) {
                    Settings.setEasy(false);
                    Settings.setHard(false);
                }
            }

            else if (inBounds(event, 170, 270, 80, 50)) {
                Settings.setHard(flipSwitch(Settings.isHard()));
                if (Settings.isEasy() || Settings.isMedium()) {
                    Settings.setEasy(false);
                    Settings.setMedium(false);
                }
            }

            else if (inBounds(event, 450, 110, 80, 50)) {           // boundary checks for operator choices
                Settings.setAdd(flipSwitch(Settings.isAdd()));
            }

            else if (inBounds(event, 450, 190, 80, 50)) {
                Settings.setSub(flipSwitch(Settings.isSub()));
            }

            else if (inBounds(event, 450, 270, 80, 50)) {
                Settings.setMult(flipSwitch(Settings.isMult()));
            }

            else if (inBounds(event, 450, 350, 80, 50)) {
                Settings.setDiv(flipSwitch(Settings.isDiv()));
            }
        }
    }

    private boolean inBounds(Input.TouchEvent event, int x, int y, int width, int height) { // checks boundaries for touch events
        if (event.x > x && event.x < x + width - 1 && event.y > y
                && event.y < y + height - 1)
            return true;
        else
            return false;
    }

    private boolean flipSwitch(boolean attribute) {     // function that flips checkboxes on and off.
        if (attribute == false) {
            return true;
        } else {
            return false;
        }
    }

    @Override
    public void paint(float deltaTime) {    // draws all the settings menu information to the screen.
        Graphics g = game.getGraphics();
        g.drawImage(Assets.settings, 0, 0);         //depending on if the option is selected or not, it draws an empty checkbox or a filled one.
        g.drawImage(Assets.backbutton, 20, 20);     // e.g. if the easy difficulty is selected, it draws a filled checkbox, if not, then it draws an empty one.
        g.drawString("Difficulty", 280, 80, paint);
        g.drawString("Easy", 280, 150, paint);      //this is the basis for the rest of the class.

        if (Settings.isEasy()) {
            g.drawImage(Assets.filled, 170, 110);
        } else {
            g.drawImage(Assets.empty, 170, 110);
        }

        g.drawString("Medium", 330, 230, paint);

        if (Settings.isMedium()) {
            g.drawImage(Assets.filled, 170, 190);
        } else {
            g.drawImage(Assets.empty, 170, 190);
        }

        g.drawString("Hard", 280, 310, paint);

        if (Settings.isHard()) {
            g.drawImage(Assets.filled, 170, 270);
        } else {
            g.drawImage(Assets.empty, 170, 270);
        }

        g.drawString("Operator", 560, 80, paint);

        g.drawString("Add", 560, 150, paint);

        if (Settings.isAdd()) {
            g.drawImage(Assets.filled, 450, 110);
        } else {
            g.drawImage(Assets.empty, 450, 110);
        }

        g.drawString("Sub", 560, 230, paint);

        if (Settings.isSub()) {
            g.drawImage(Assets.filled, 450, 190);
        } else {
           g.drawImage(Assets.empty, 450, 190);
        }

        g.drawString("Mult", 560, 310, paint);

        if (Settings.isMult()) {
            g.drawImage(Assets.filled, 450, 270);
        } else {
            g.drawImage(Assets.empty, 450, 270);
        }

        g.drawString("Div", 560, 390, paint);

        if (Settings.isDiv()) {
            g.drawImage(Assets.filled, 450, 350);
        } else {
            g.drawImage(Assets.empty, 450, 350);
        }
    }

    @Override
    public void pause() {
    }

    @Override
    public void resume() {

    }

    @Override
    public void dispose() {

    }

    @Override
    public void backButton() {
        android.os.Process.killProcess(android.os.Process.myPid());

    }
}
