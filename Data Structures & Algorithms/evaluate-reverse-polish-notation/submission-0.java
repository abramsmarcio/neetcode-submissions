class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for(String s : tokens){
            if (s.equals("+") || s.equals("-") || s.equals("*") || s.equals("/")){
                int c2 = stack.pop();
                int c1 = stack.pop();
                if (s.equals("+")) stack.push(c1 + c2);
                else if (s.equals("-")) stack.push(c1 - c2);
                else if (s.equals("*")) stack.push(c1 * c2);
                else if (s.equals("/")) stack.push(c1 / c2);
            }
            else{
                stack.push(Integer.parseInt(s));
            }
        }
        return stack.peek();
    }
}

