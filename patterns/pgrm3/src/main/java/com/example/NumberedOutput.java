package com.example;

public class NumberedOutput implements Output {
    private Output delegate;
    private int lineNumber =   1;

    public NumberedOutput(Output delegate) {
        this.delegate = delegate;
    }

    @Override
    public void write(Object o) {
        String line = String.format("%5d: %s", lineNumber++, o.toString());
        delegate.write(line);
        delegate.write("\n");
    }
}