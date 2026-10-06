import os,requests
def get_demo_tool_result():
    try:r=requests.get(os.getenv('TOOL_API_URL','https://api.github.com/zen'),timeout=5);r.raise_for_status();return {'tool':'demo_external_api','status':'success','result':r.text}
    except requests.RequestException as e:return {'tool':'demo_external_api','status':'error','result':str(e)}
