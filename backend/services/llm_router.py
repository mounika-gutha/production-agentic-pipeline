import os
try: from openai import OpenAI
except ImportError: OpenAI=None
try: from anthropic import Anthropic
except ImportError: Anthropic=None
class LLMRouter:
    def __init__(self):
        self.ok=os.getenv('OPENAI_API_KEY',''); self.ak=os.getenv('ANTHROPIC_API_KEY',''); self.om=os.getenv('OPENAI_MODEL','gpt-4o-mini'); self.am=os.getenv('ANTHROPIC_MODEL','claude-3-5-haiku-latest')
    def choose(self,wanted):
        a=[]
        if self.ok and OpenAI:a.append('openai')
        if self.ak and Anthropic:a.append('claude')
        return wanted if wanted in a else (a[0] if a else 'demo')
    def generate(self,msg,history,provider='auto'):
        p=self.choose(provider)
        if p=='openai':
            c=OpenAI(api_key=self.ok); m=[{'role':x['role'],'content':x['content']} for x in history]+[{'role':'user','content':msg}]; r=c.chat.completions.create(model=self.om,messages=m); return {'provider':p,'response':r.choices[0].message.content}
        if p=='claude':
            c=Anthropic(api_key=self.ak); m=[{'role':x['role'],'content':x['content']} for x in history]+[{'role':'user','content':msg}]; r=c.messages.create(model=self.am,max_tokens=1000,messages=m); return {'provider':p,'response':r.content[0].text}
        return {'provider':'demo','response':'Demo response: add an OpenAI or Anthropic API key in .env to enable a real LLM.'}
