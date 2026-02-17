from mcp_client import list_mcp_tools, call_mcp_tool
from llm_ollama import call_llm
from langchain_core.messages import AIMessage
from prompt import get_prompt

class ChatAgent:
    
    def needs_tool_execution(self, llm_response: AIMessage) -> bool:
        return bool(llm_response.tool_calls)
    
    async def run(self, query: str) -> str:

        tools_response = await list_mcp_tools()
        print("tools response",tools_response)
        print("------------")
        tools = [
            {
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.inputSchema,
                },
            }
            for tool in tools_response.tools
        ]

        custom_prompt = get_prompt(query)
        llm_response = call_llm(custom_prompt, tools)
        print("Tool class size:", len(llm_response.tool_calls))
        max_iterations = 5  # Safety guard
        iterations = 0
        current_turn_results = []
        while self.needs_tool_execution(llm_response) and iterations < max_iterations:
            iterations += 1
           
           
            for tool_call in llm_response.tool_calls:
                print(f"Executing: {tool_call['name']}")
                result = await call_mcp_tool(
            tool_name=tool_call["name"],
            arguments=tool_call["args"]
           )
                print(f"Tools Result: {tool_call['name']}")
                current_turn_results.append({
            "tool_name": tool_call["name"],
            "result": result
        }) 
            print("tool result:",result ,"Iteration",iterations)
            custom_prompt = get_prompt(custom_prompt, current_turn_results)
            print("Printing custom prompt" , custom_prompt)
            llm_response = call_llm(custom_prompt, tools)

        final_answer = llm_response.content
        return final_answer
    
    

            
                
    

       
