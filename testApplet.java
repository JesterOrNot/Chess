package java;

import java.awt.Graphics;
import java.awt.Font;
import java.awt.Color;

public class testApplet extends java.applet.Applet {

    public static final long serialVersionUID = 1L;
	Font f = new Font("TimesRoman", Font.BOLD, 36);

    public void paint(Graphics g) {
        g.setFont(f);
        g.setColor(Color.black);
        g.drawString("Hello world from JAVA!", 5, 40);
    }
}