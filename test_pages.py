import asyncio
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

async def test_pages_functionality():
    print("Starting test of Pages functionality...")
    try:
        # Create a connection to the MCP server
        server_params = StdioServerParameters(
            command="python",
            args=["example2.py"]
        )

        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                
                # Test opening Pages
                print("Testing open_pages...")
                result = await session.call_tool("open_pages")
                print(f"Result: {result.content[0].text}")
                
                # Wait for Pages to open
                await asyncio.sleep(2)
                
                # Test creating a new document
                print("Testing create_new_pages_document...")
                result = await session.call_tool("create_new_pages_document")
                print(f"Result: {result.content[0].text}")
                
                # Test adding text
                print("Testing add_text_to_pages...")
                result = await session.call_tool(
                    "add_text_to_pages",
                    arguments={
                        "text": "This is a test document created by the MCP server.\n\n"
                    }
                )
                print(f"Result: {result.content[0].text}")
                
                # Test saving the document
                print("Testing save_pages_document...")
                result = await session.call_tool(
                    "save_pages_document",
                    arguments={
                        "file_name": "Test_Document.pages"
                    }
                )
                print(f"Result: {result.content[0].text}")
                
                print("All Pages functionality tests completed successfully!")
                
    except Exception as e:
        print(f"Error in test: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_pages_functionality()) 