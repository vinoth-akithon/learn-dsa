// import java.util.ArrayDeque;
// import java.util.Queue;

import java.lang.reflect.Array;
import java.util.Arrays;

public class Main {
    private int[] items = new int[5];
    private int count;

    public int shiftItemsToInsert(int item) {
        int i;
        for (i = count - 1; i >= 0; i--) {
            if (items[i] > item)
                items[i + 1] = items[i];
            else
                break;
        }
        return i + 1;
    }

    public static void main(String[] args) {

        var value = shiftItemsToInsert(10)
        // Queue<String> queue = new ArrayDeque<>();
        // queue.add("vinoth");
        // queue.add("kumar");
        // System.out.println(queue.peek());
        // System.out.println(queue);

        // int[] array = new int[5];
        // array[0] = 1;
        // array[1] = 2;
        // array[4] = 10;
        // // array[2] = 3;

        // System.out.println(Arrays.toString(array[0]));
        // int[] ints = new int[5];

        // ints[2] = 123;
        // ints[3] = 20;
        // ints[4] = 30;

        // int removeIndex = 2;
        // System.out.println(Arrays.toString(ints));
        // for(int i = removeIndex; i < ints.length -1; i++){
        // System.out.println(i);
        // System.out.println(ints[i + 1]);
        // ints[i] = ints[i + 1];

        // }
        // System.out.println(Arrays.toString(ints));

    }
}