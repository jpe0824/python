package com.example;

public class ContainsWordPredicate implements Predicate {
    private String word;

    public ContainsWordPredicate(String word) {
        this.word = word;
    }

    @Override
    public boolean execute(Object line) {
        if (line instanceof String) {
            return ((String) line).contains(word);
        }
        return false;
    }
}
