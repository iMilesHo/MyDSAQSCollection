import java.lang.String;
import java.util.*;
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs==null || strs.length==0){
            return "";
        }
        String prefix = strs[0];
        for(int i=1;i<strs.length;i++){
            while(strs[i].indexOf(prefix)!=0){
                prefix =prefix.substring(0,prefix.length()-1);
            }
        }

        return prefix;
    }
}


public class Main {

    public static void main(String[] args) {
//        Solution s = new Solution();
//        s.longestCommonPrefix(new String[]{"abc", "efg", "abcdefg"});
//        System.out.println("Hello world!");

        String a = "";
        String b = "";
        System.out.println(a.indexOf(b));
    }
}