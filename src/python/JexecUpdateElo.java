import java.io.*;

class JexecElo{
    public void JexecElo(){}

    private String exec(String execStr){
    try{
        // run process and capture stdout
        Process p = Runtime.getRuntime().exec(execStr);
        InputStream s = p.getInputStream();

        // convert stdout to a string
        BufferedReader br = new BufferedReader(new InputStreamReader(s));
        StringBuffer sb = new StringBuffer();
        String line;
        while ((line = br.readLine()) != null) {
        sb.append(line).append("\n");
        }
        String output = sb.toString();

        p.destroy();
        return output.toString();

    }catch(Exception e){
        //actually handle the error here
        e.printStackTrace();
        return String.format("*** Running \"%s\" failed. ***",execStr);
    }
    }

    public static void main(String[] args){
    JexecElo je = new JexecElo();
    System.out.println(je.exec("python3 updateElo.py")); //in your case, you would use the output instead of just printing it
    }
}