import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.ArrayList;

public class 다음수구하기 {
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i=0;i<n;i++) {
            String[] strArr = br.readLine().split("");
            ArrayList<String> list = new ArrayList<String>(Arrays.asList(strArr));
        
            int start = strArr.length - 1;
            int end = -1;
            int x = -1;
            int y = -1;
            String answer = "";
            System.out.println("start"+ start);
            while (start-1 > end) {
                for (int j=start-1;j>end;j--){
                    
                    if (Integer.parseInt(list.get(j)) < Integer.parseInt(list.get(start))){
                        if (x > 0 && end == j && Integer.parseInt(list.get(start)) > Integer.parseInt(list.get(x))){
                            break;
                        }
                    
                        x = start;
                        y = j;
                        end = j;
                        break;
                    }
                }
                start -= 1;
            }
            if (x == -1){
                answer = "BIGGEST";
            } else {
                // System.out.println('x'+ x);
                // System.out.println('y'+ y);
                System.out.println("start" + start + "end" + end);
                for (i=0;i<y;i++){
                    answer += list.get(i);
                }
                answer += list.get(y);
                for (i=0;i<x;i++){
                    answer += list.get(i);
                }
                answer += list.get(x);

                int[] time = new int[strArr.length];
                br.close();
                for (int cha=x+1;cha<strArr.length;cha++) {
                    time[cha] = Integer.parseInt(list.get(cha));
                }
                // time리스트 정렬
                Arrays.sort(time);
                for( int nextNum : time){
                    answer += Integer.toString(nextNum);
                }
            }
            System.out.println(answer);
        }
    }
}
