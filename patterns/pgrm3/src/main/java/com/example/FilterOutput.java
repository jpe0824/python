package com.example;

public class FilterOutput implements Output {
    private Output delegate;
    private Predicate predicate;

    public FilterOutput(Output delegate, Predicate predicate) {
        this.delegate = delegate;
        this.predicate = predicate;
    }

    @Override
    public void write(Object o) {
        if (predicate.execute(o)) {
            delegate.write(o);
        }
    }
}
