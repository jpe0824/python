package com.example;

public class BracketOutput implements Output {
    private Output delegate;

    public BracketOutput(Output delegate) {
        this.delegate = delegate;
    }

    @Override
    public void write(Object o) {
        String s = ("[" + o.toString() + "]\n");
        delegate.write(s);
    }
}
