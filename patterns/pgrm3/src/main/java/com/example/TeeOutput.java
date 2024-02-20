package com.example;

public class TeeOutput implements Output {
    private Output delegate1;
    private Output delegate2;

    public TeeOutput(Output delegate1, Output delegate2) {
        this.delegate1 = delegate1;
        this.delegate2 = delegate2;
    }

    @Override
    public void write(Object o) {
        delegate1.write(o);
        delegate2.write(o);
    }
}