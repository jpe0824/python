package com.example;

public class BracketOutput implements Output {
    private Output delegate;

    public BracketOutput(Output delegate) {
        this.delegate = delegate;
    }

    @Override
    public void write(Object o) {
        String s = ("[" + o.toString() + "]\n");
        writeString(s);
    }

    public void writeString(String s) {
        delegate.write("[" + s + "]\n");
    }
    public void print(String s) {
        System.out.println("[" + s + "]");
    }
}
