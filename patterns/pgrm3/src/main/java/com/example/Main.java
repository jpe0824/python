package com.example;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.Writer;

public class Main {
    public static void main(String[] args) {
    try {
            // Prompt for a file to read, default to decorator.dat
            System.out.print("Enter the file to read (default is decorator.dat): ");
            String inputFileName = System.console().readLine();
            if (inputFileName.isEmpty()) {
                inputFileName = "./decorator.dat";
            }
            BufferedReader reader = new BufferedReader(new FileReader(inputFileName));

            // Create a StreamOutput instance to write to output.txt
            Output streamOutput = new StreamOutput(new PrintWriter(new FileWriter("./output.txt")));
            // Present a menu of decorations
            System.out.println("Select decorations:");
            System.out.println("1. BracketOutput");
            System.out.println("2. NumberedOutput");
            System.out.println("3. TeeOutput");
            System.out.println("4. FilterOutput");
            System.out.println("5. Exit");

            // Apply the selected decorators
            Output decoratedOutput = streamOutput;
            boolean exit = false;
            while (!exit) {
                System.out.print("Enter your choice: ");
                int choice = Integer.parseInt(System.console().readLine());
                switch (choice) {
                    case  1:
                        decoratedOutput = new BracketOutput(decoratedOutput);
                        break;
                    case  2:
                        decoratedOutput = new NumberedOutput(decoratedOutput);
                        break;
                    case  3:
                        System.out.print("Enter the file for TeeOutput: ");
                        Writer teeWriter = new PrintWriter(System.console().readLine());
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
                    case  5:
                        System.out.println("Exiting...");
                        exit = true;
                        break;
                    default:
                        System.out.println("Invalid choice. Please try again.");
                }
            }


            // Read the file and apply the decorators
            String line;
            while ((line = reader.readLine()) != null) {
                decoratedOutput.write(line);
            }
            // Close the reader
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}