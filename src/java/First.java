package java;

//First.java
import java.applet.Applet;
import java.awt.Graphics;

public class First extends Applet {
    private static final long serialVersionUID = 1L;

	public void paint(Graphics g) {
        g.drawString("welcome to applet", 150, 150);
    }

}
/*
 * <applet code="First.class" width="300" height="300"> </applet>
 */