package java;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
public class App extends java.applet.Applet {

    private static final long serialVersionUID = 1L;
    Font f = new Font("TimesRoman", Font.BOLD, 36);

    public void paint(Graphics g) {
        g.setFont(f);
        g.setColor(Color.red);
        g.drawString("Hello again!", 5, 40);
    }
}