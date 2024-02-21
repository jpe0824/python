package com.example;

public class InsertOnLineOutput implements Output {
    private Output delegate;
    private int lineNumber;
    private String insertText;
    private int currentLine = 1;

    public InsertOnLineOutput(Output delegate, int lineNumber, String insertText) {
        this.delegate = delegate;
        this.lineNumber = lineNumber;
        this.insertText = insertText;
    }

    @Override
    public void write(Object o) {
        if (currentLine == lineNumber) {
            delegate.write(insertText);
        }
        delegate.write(o);
        currentLine++;
    }
}
