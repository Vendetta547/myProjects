package com.csc2300teamtwo.framework.implementation;

import java.util.List;

import android.view.View.OnTouchListener;

import com.csc2300teamtwo.framework.Input;

public interface TouchHandler extends OnTouchListener {
    public boolean isTouchDown(int pointer);
    
    public int getTouchX(int pointer);
    
    public int getTouchY(int pointer);
    
    public List<Input.TouchEvent> getTouchEvents();
}
