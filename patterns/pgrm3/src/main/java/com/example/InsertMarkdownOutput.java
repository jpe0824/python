package com.example;

public class InsertMarkdownOutput implements Output {
    private Output delegate;
    private int option;
    private int startLine;
    private int endLine;
    private String insertText;
    private int currentLine = 1;

    public InsertMarkdownOutput(Output delegate, int option, int startLine, int endLine, String insertText) {
        this.delegate = delegate;
        this.option = option;
        this.startLine = startLine;
        this.endLine = endLine;
        this.insertText = insertText;
    }

    @Override
    public void write(Object o) {
        switch (option) {
            case 1:
            case 2:
            case 4:
                if (currentLine == startLine) {
                    delegate.write(insertText + o.toString());
                }
                break;
            case 3:
                if (currentLine == startLine) {
                    delegate.write(insertText + o.toString());
                } else if (currentLine == endLine) {
                    delegate.write("```");
                }
                break;
        }
        delegate.write(o);
        currentLine++;
    }
}