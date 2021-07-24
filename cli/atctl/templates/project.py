
projectTemplate = '''
rootName: "autoflow-demo"
fileList: 
    - name: "linxs.py"
      content: "ZnJvbSB0aW1lIGltcG9ydCBzbGVlcAoKCmRlZiBzZXR1cCgpOgogICAgc2xlZXAoMzAwKQoKZGVmIHRlYXJkb3duKCk6CiAgICBzbGVlcCg5MCk="
    - name: "__init__.py"
subDir:
  - relativePath: "yaml"
    fileList: 
      - name: "test_demo.yaml"
        content: "Cmdsb2JhbDoKICAgaG9zdDogImh0dHBzOi8vcG9zdG1hbi1lY2hvLmNvbSIKICAgbmFtZTogIkRlbW8iCiAgIHJldHJ5OiAxCnN0ZXBzOgogICAtIHN0ZXA6CiAgICAgIHN0ZXBuYW1lOiAicG9zdEVjaG8iCiAgICAgIHJlcXVlc3Q6CiAgICAgICAgcHJlOiBbXQogICAgICAgIG1ldGhvZDogIlBPU1QiCiAgICAgICAgaG9zdDogImh0dHBzOi8vcG9zdG1hbi1lY2hvLmNvbSIKICAgICAgICB1cmxQYXRoOiAiL3Bvc3QiCiAgICAgICAgZGF0YTogTm9uZQogICAgICAgIGhlYWRlcjoKICAgICAgICAgIFVzZXItQWdlbnQ6ICIiCiAgICAgIHJlc3BvbnNlOiBbCiAgICAgICAgewogICAgICAgICAgImZpZWxkIjogImNvZGUiLAogICAgICAgICAgImFzc2VydCI6ICJlcSIsCiAgICAgICAgICAiZGVzaXJlIjogMjAwCiAgICAgICAgfSwKICAgICAgICB7CiAgICAgICAgICAiZmllbGQiOiAidXJsIiwKICAgICAgICAgICJhc3NlcnQiOiAiZXEiLAogICAgICAgICAgImRlc2lyZSI6ICJodHRwczovL3Bvc3RtYW4tZWNoby5jb20vcG9zdCIKICAgICAgICB9CiAgICAgIF0KICAgLSBzdGVwOgogICAgICBzdGVwbmFtZTogImdldFRhc2tMaXN0IiAKICAgICAgcmV0cnk6IDUKICAgICAgcmVxdWVzdDoKICAgICAgICBwcmU6IFtdCiAgICAgICAgbWV0aG9kOiAiZ2V0IgogICAgICAgIGhvc3Q6ICJodHRwczovL3Bvc3RtYW4tZWNoby5jb20iCiAgICAgICAgdXJsUGF0aDogIi9nZXQiCiAgICAgICAgZGF0YTogTm9uZQogICAgICAgIGhlYWRlcjogewogICAgICAgICAgIkNvbnRlbnQtVHlwZSI6ICJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwKICAgICAgICB9CiAgICAgIHJlc3BvbnNlOiBbCiAgICAgICAgewogICAgICAgICAgImZpZWxkIjogImNvZGUiLAogICAgICAgICAgImFzc2VydCI6ICJlcSIsCiAgICAgICAgICAiZGVzaXJlIjogMjAwCiAgICAgICAgfSwKICAgICAgICB7CiAgICAgICAgICAiZmllbGQiOiAidXJsIiwKICAgICAgICAgICJhc3NlcnQiOiAiZXEiLAogICAgICAgICAgImRlc2lyZSI6ICJodHRwczovL3Bvc3RtYW4tZWNoby5jb20vZ2V0IgogICAgICAgIH0KICAgICAgXQo="
  - relativePath: "har"
    fileList: []
  - relativePath: "logs"
    fileList: []
  - relativePath: "testcases"
    fileList: 
    - name: "test_demo.py"
      content: "ZnJvbSBzaW1hdF9jb3JlLmJhc2Uuc3VpdCBpbXBvcnQgU3VpdApmcm9tIHNpbWF0X2NvcmUuYmFzZS5zdGVwIGltcG9ydCBTdGVwCmltcG9ydCBweXRlc3QKZnJvbSBsaW54cyBpbXBvcnQgKgoKCmNsYXNzIFRlc3REZW1vKFN1aXQpOgogICAgZGVmIHNldHVwX21ldGhvZChzZWxmLCBtZXRob2QpOgogICAgICAgIHNlbGYuaW5pdF9yZXNvdXJjZShbXSkKICAgICAgICBzZWxmLnN0ZXBzID0gWwogICAgICAgICAgICBTdGVwKCooInBvc3RFY2hvIiwgImh0dHBzOi8vcG9zdG1hbi1lY2hvLmNvbS9wb3N0IiwgIlBPU1QiLCBOb25lLCB7CiAgICAgICAgICAgICAgICAnVXNlci1BZ2VudCc6ICcnCiAgICAgICAgICAgIH0sIFt7CiAgICAgICAgICAgICAgICAnZmllbGQnOiAnY29kZScsCiAgICAgICAgICAgICAgICAnYXNzZXJ0JzogJ2VxJywKICAgICAgICAgICAgICAgICdkZXNpcmUnOiAyMDAKICAgICAgICAgICAgfSwgewogICAgICAgICAgICAgICAgJ2ZpZWxkJzogJ3VybCcsCiAgICAgICAgICAgICAgICAnYXNzZXJ0JzogJ2VxJywKICAgICAgICAgICAgICAgICdkZXNpcmUnOiAnaHR0cHM6Ly9wb3N0bWFuLWVjaG8uY29tL3Bvc3QnCiAgICAgICAgICAgIH1dLCBbXSwgTm9uZSwgTm9uZSwgTm9uZSkpLAogICAgICAgICAgICBTdGVwKCooImdldFRhc2tMaXN0IiwgImh0dHBzOi8vcG9zdG1hbi1lY2hvLmNvbS9nZXQiLCAiZ2V0IiwgTm9uZSwKICAgICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICAgICAnQ29udGVudC1UeXBlJzogJ2FwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9dXRmLTgnCiAgICAgICAgICAgICAgICAgICB9LCBbewogICAgICAgICAgICAgICAgICAgICAgICdmaWVsZCc6ICdjb2RlJywKICAgICAgICAgICAgICAgICAgICAgICAnYXNzZXJ0JzogJ2VxJywKICAgICAgICAgICAgICAgICAgICAgICAnZGVzaXJlJzogMjAwCiAgICAgICAgICAgICAgICAgICB9LCB7CiAgICAgICAgICAgICAgICAgICAgICAgJ2ZpZWxkJzogJ3VybCcsCiAgICAgICAgICAgICAgICAgICAgICAgJ2Fzc2VydCc6ICdlcScsCiAgICAgICAgICAgICAgICAgICAgICAgJ2Rlc2lyZSc6ICdodHRwczovL3Bvc3RtYW4tZWNoby5jb20vZ2V0JwogICAgICAgICAgICAgICAgICAgfV0sIFtdLCA1LCBOb25lLCBOb25lKSkKICAgICAgICBdCgogICAgZGVmIHRlYXJkb3duX21ldGhvZChzZWxmLCBtZXRob2QpOgogICAgICAgIHBhc3MKCiAgICBAcHl0ZXN0Lm1hcmsuZmxha3kocmVydW5zPTIpCiAgICBkZWYgdGVzdF9EZW1vKHNlbGYpOgogICAgICAgIHNlbGYucnVuKCkK"
  - relativePath: "reports"
    fileList: []
'''


