# Mac Pages Integration for MCP

This extension adds functionality to interact with the Mac Pages application from the MCP (Model Control Protocol) server.

## Features

The following tools have been added to interact with Pages:

1. **open_pages()**: Opens the Pages application on macOS
2. **create_new_pages_document()**: Creates a new document in Pages
3. **add_text_to_pages(text)**: Adds text to the current Pages document
4. **save_pages_document(file_name)**: Saves the current document with the specified filename

## Requirements

- macOS (Darwin) operating system
- Pages application installed
- Python 3.6+
- MCP library
- python-dotenv package

## Setup

### Environment Variables

The application uses a `.env` file to store sensitive information like API keys. Create a `.env` file in the root directory with the following content:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace `your_gemini_api_key_here` with your actual Gemini API key.

## Usage

### In talk2mcp.py

The talk2mcp.py script has been modified to use Pages instead of Paint when displaying final results. When a calculation is complete, it will:

1. Open Pages
2. Create a new document
3. Add the final answer and all iteration responses to the document
4. Save the document as "Math_Result.pages" in the Documents folder

### Testing

You can test the Pages functionality independently by running:

```bash
python test_pages.py
```

This will:
1. Open Pages
2. Create a new document
3. Add some test text
4. Save the document as "Test_Document.pages" in the Documents folder

## Implementation Details

The Pages integration uses:
- `subprocess` to run system commands
- AppleScript (via `osascript`) to control the Pages application
- Platform detection to ensure the code only runs on macOS

## Troubleshooting

If you encounter issues:

1. Ensure Pages is installed on your Mac
2. Check that you have permission to run AppleScript
3. Verify that the Documents folder is accessible
4. Check the console output for error messages
5. Make sure your `.env` file is properly set up with the Gemini API key

## Limitations

- This functionality only works on macOS
- The AppleScript commands may need adjustment for different versions of Pages
- The document is saved in the user's Documents folder 