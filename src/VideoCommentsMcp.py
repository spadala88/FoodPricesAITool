from mcp.server.fastmcp import FastMCP
from googleapiclient.discovery import build

mcp = FastMCP()
# Your API Key (Remember to rotate this key later!)
YOUTUBE_API_KEY = "AIzaSyABFhDmNkm7Ds_ZoOn9Y1pXKi0Xl05ugjQ"

@mcp.tool(
    name="fetch_video_comments",
    description="Fetch comments from a YouTube video."
)
def fetch_video_comments(video_id: str, max_results: int = 50) -> str:
    
 try:
    # 2. Build service INSIDE the tool with cache_discovery=False
        # Note: The parameter name is 'cache_discovery', not 'static_discovery'
        youtube = build(
            "youtube", 
            "v3", 
            developerKey=YOUTUBE_API_KEY,
            cache_discovery=False 
        )

        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=max_results,
            textFormat="plainText"
        )
        response = request.execute()
        
        comments = []
        for item in response.get('items', []):
            snippet = item['snippet']['topLevelComment']['snippet']
            user = snippet['authorDisplayName']
            text = snippet['textDisplay']
            comments.append(f"[{user}]: {text}")
            
        return "\n".join(comments) if comments else "No comments found."
 except Exception as e:
    print(f"Error fetching comments: {str(e)}")
    return f"Error: {str(e)}"

def main():
    mcp.run(transport="sse")


if __name__ == "__main__":
    main()