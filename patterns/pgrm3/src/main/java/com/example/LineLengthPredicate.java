package com.example;

public class LineLengthPredicate implements Predicate {
    private int maxLength;

    public LineLengthPredicate(int maxLength) {
        this.maxLength = maxLength;
    }

    @Override
    public boolean execute(Object line) {
        if (line instanceof String) {
            return ((String) line).length() <= maxLength;
        }
        return false;
    }
}