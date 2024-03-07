package com.example;

import java.io.BufferedReader;
import java.io.FileInputStream;
// import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.Writer;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    try {
            // Prompt for a file to read, default to decorator.dat
            Scanner inputScanner = new Scanner(System.in);
            System.out.print("Enter the file path to read (default is ./decorator.dat): ");
            String inputFileName = inputScanner.nextLine().trim();
            if (inputFileName.isEmpty()) {
                inputFileName = "./decorator.dat";
            }
            // Create a StreamOutput instance to write to output.txt
            Writer outputWriter = new FileWriter("output.txt");
            Output streamOutput = new StreamOutput(new PrintWriter(outputWriter));
            // Present a menu of decorations
            System.out.println("Select decorations:");
            System.out.println("1. BracketOutput");
            System.out.println("2. NumberedOutput");
            System.out.println("3. TeeOutput");
            System.out.println("4. FilterOutput");
            System.out.println("5. Insert on line");
            System.out.println("6. Insert Markdown");
            System.out.println("7. Exit");

            // Apply the selected decorators
            Output decoratedOutput = streamOutput;
            boolean exit = false;
            while (!exit) {
                System.out.print("Enter your choice: ");
                int choice = Integer.parseInt(inputScanner.nextLine());
                switch (choice) {
                    case  1:
                        decoratedOutput = new BracketOutput(decoratedOutput);
                        break;
                    case  2:
                        decoratedOutput = new NumberedOutput(decoratedOutput);
                        break;
                    case  3:
                        System.out.print("Enter the file for TeeOutput: ");
                        String teeFileName = inputScanner.nextLine().trim();
                        Writer teeWriter = new PrintWriter(new FileWriter(teeFileName));
                        decoratedOutput = new TeeOutput(decoratedOutput, new StreamOutput(teeWriter));
                        break;
                    case  4:
                        System.out.println("Select a predicate for FilterOutput:");
                        System.out.println("1. Filter lines containing a specific word");
                        System.out.println("2. Filter lines longer than a certain length");
                        int predicateChoice = Integer.parseInt(System.console().readLine());
                        switch (predicateChoice) {
                            case  1:
                                System.out.print("Enter the word to filter: ");
                                String word = System.console().readLine();
                                decoratedOutput = new FilterOutput(decoratedOutput, new ContainsWordPredicate(word));
                                break;
                            case  2:
                                System.out.print("Enter the maximum line length: ");
                                int maxLength = Integer.parseInt(System.console().readLine());
                                decoratedOutput = new FilterOutput(decoratedOutput, new LineLengthPredicate(maxLength));
                                break;
                            default:
                                System.out.println("Invalid predicate choice. Please try again.");
                                break;
                        }
                        break;
                    case 5:
                        System.out.print("Enter the line number to insert on: ");
                        int lineNumber = Integer.parseInt(inputScanner.nextLine());
                        System.out.print("Enter the text to insert: ");
                        String insertText = inputScanner.nextLine();
                        decoratedOutput = new InsertOnLineOutput(decoratedOutput, lineNumber, insertText);
                        break;
                    case 6:
                        System.out.print("Enter option: \n");
                        System.out.println("1. Insert Header 1");
                        System.out.println("2. Insert Header 2");
                        System.out.println("3. Insert Code Block");
                        System.out.println("4. Insert Unordered List");
                        int option = Integer.parseInt(inputScanner.nextLine());
                        System.out.print("Enter the start line: ");
                        int startLine = Integer.parseInt(inputScanner.nextLine());
                        int endLine = startLine;
                        String language = "";
                        if (option == 3) {
                            System.out.print("Enter the end line: ");
                            endLine = Integer.parseInt(inputScanner.nextLine());
                            System.out.print("Enter the language: ");
                            language = inputScanner.nextLine();
                        }

                        String insertMDText;
                        switch (option) {
                            case 1:
                                insertMDText = "# ";
                                break;
                            case 2:
                                insertMDText = "## ";
                                break;
                            case 3:
                                insertMDText = "``` " + language + " ";
                                break;
                            case 4:
                                insertMDText = "* ";
                                break;
                            default:
                                throw new IllegalArgumentException("Invalid option");
                        }

                        decoratedOutput = new InsertMarkdownOutput(decoratedOutput, option, startLine, endLine, insertMDText);
                        break;
                    case 7:
                        System.out.println("Exiting...");
                        exit = true;
                        break;
                    default:
                        System.out.println("Invalid choice. Please try again.");
                }
            }

            inputScanner.close();

            FileInputStream fstream = new FileInputStream(inputFileName);
            BufferedReader reader = new BufferedReader(new InputStreamReader(fstream));

            String line;

            while ((line = reader.readLine()) != null) {
                decoratedOutput.write(line);
            }

            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}